import importlib
from pathlib import Path
from apex.config import load_yaml
from apex.models import local

class Orchestrator:
    def __init__(self, config_dir=None):
        self.models = load_yaml('models.yaml')
        self.skills = load_yaml('skills.yaml')
        self.security = load_yaml('security.yaml')

    def route(self, task_type='general'):
        route = self.models.get('routing', {}).get(task_type, 'local.default')
        provider, key = route.split('.', 1)
        if provider == 'local':
            return self.models['local'].get(key, self.models['local']['default'])
        cfg = self.models.get('cloud', {}).get(key, {})
        if cfg.get('enabled') and __import__('os').getenv(cfg.get('key_env','')):
            return cfg['model']
        return self.models['local']['default']

    def run(self, prompt, task_type='general'):
        return local.run(prompt, model=self.route(task_type))

    def execute_skill(self, skill_name, operation, params, approved=False):
        skill = self.skills.get('skills', {}).get(skill_name)
        if not skill or not skill.get('enabled'):
            raise ValueError(f'Skill {skill_name} not available')
        op = next((o for o in skill.get('operations', []) if o['name'] == operation), None)
        if not op:
            raise ValueError(f'Operation {operation} not found')
        if op.get('requires_approval') and not approved:
            return {'status':'approval_required','skill':skill_name,'operation':operation}
        mod = importlib.import_module(skill['handler'])
        return getattr(mod, operation)(**params)
