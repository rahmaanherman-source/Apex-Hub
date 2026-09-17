import importlib
import time
from contextlib import AbstractContextManager
from apex.config import load_yaml, env
from apex.models import local


class CloudWindow(AbstractContextManager):
    """Short-lived authorization window for a configured cloud provider.

    The provider secret is read only when the window opens. The window never
    caches the secret and cannot silently fall back from local inference.
    """
    def __init__(self, provider_cfg):
        self.cfg = provider_cfg
        self.opened_at = None
        self._key = None

    def __enter__(self):
        mode = self.cfg.get('mode', 'disabled')
        if mode != 'on_demand':
            raise RuntimeError(f"Cloud provider mode is '{mode}', not on_demand")

        key_name = self.cfg.get('key_env')
        self._key = env(key_name) if key_name else ''
        if not self._key:
            raise RuntimeError(f'{key_name} missing from vault')

        if self.cfg.get('require_confirm', True):
            answer = input(
                f"Open cloud window to {self.cfg.get('model', 'configured provider')}? (y/N): "
            ).strip().lower()
            if answer != 'y':
                self._key = None
                raise RuntimeError('User declined cloud access')

        self.opened_at = time.monotonic()
        print(
            f"[cloud] window OPEN -> {self.cfg.get('model')} "
            f"({self.cfg.get('window_seconds', 60)}s max)"
        )
        return self._key

    def expired(self):
        if self.opened_at is None:
            return True
        return time.monotonic() - self.opened_at >= float(self.cfg.get('window_seconds', 60))

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = 0 if self.opened_at is None else time.monotonic() - self.opened_at
        self._key = None
        self.opened_at = None
        print(f'[cloud] window CLOSED after {elapsed:.1f}s')
        return False


class Orchestrator:
    def __init__(self, config_dir=None):
        self.models = load_yaml('models.yaml')
        self.skills = load_yaml('skills.yaml')
        self.security = load_yaml('security.yaml')

    def route(self, task_type='general'):
        return self.models.get('routing', {}).get(task_type, 'local.default')

    def _local_model(self, route):
        _, key = route.split('.', 1)
        return self.models['local'].get(key, self.models['local']['default'])

    def _cloud_config(self, route):
        _, provider = route.split('.', 1)
        cfg = self.models.get('cloud', {}).get(provider)
        if not cfg:
            raise RuntimeError(f'Cloud provider not configured: {provider}')
        return provider, cfg

    def run(self, prompt, task_type='general'):
        route = self.route(task_type)
        provider, _ = route.split('.', 1)

        if provider == 'local':
            return local.run(prompt, model=self._local_model(route))

        if provider != 'cloud':
            raise RuntimeError(f'Unknown provider class: {provider}')

        provider_name, cfg = self._cloud_config(route)
        with CloudWindow(cfg) as key:
            # Provider adapters are intentionally explicit. No generic adapter
            # is allowed to guess a vendor API contract or silently transmit data.
            raise RuntimeError(
                f'Cloud window authorized for {provider_name}, but its provider adapter '
                f'is not installed yet. The circuit is open only for an explicit adapter call.'
            )

    def execute_skill(self, skill_name, operation, params, approved=False):
        skill = self.skills.get('skills', {}).get(skill_name)
        if not skill or not skill.get('enabled'):
            raise ValueError(f'Skill {skill_name} not available')
        op = next((o for o in skill.get('operations', []) if o['name'] == operation), None)
        if not op:
            raise ValueError(f'Operation {operation} not found')
        if op.get('requires_approval') and not approved:
            return {'status': 'approval_required', 'skill': skill_name, 'operation': operation}
        mod = importlib.import_module(skill['handler'])
        return getattr(mod, operation)(**params)
