from __future__ import annotations

class SlashCommands:
    def __init__(self, agent): self.agent=agent
    def dispatch(self,text:str)->str:
        parts=text.strip().split(); cmd=parts[0] if parts else "/help"; args=parts[1:]
        if cmd=="/help": return "/help /status /permissions /mode /profile /capabilities /guarantees /limitations /sessions /exit"
        if cmd=="/status":
            p=self.agent.config.current_profile(); return f"profile={p.name} provider={p.provider} model={p.model} mode={self.agent.config.mode} workspace={self.agent.workspace}"
        if cmd=="/permissions": return f"mode={self.agent.config.mode}"
        if cmd=="/mode" and args:
            self.agent.config.mode=args[0]; from .permissions import Mode; self.agent.gate.mode=Mode(args[0]); return f"mode set to {args[0]}"
        if cmd=="/profile" and args:
            if args[0] not in self.agent.config.profiles: return f"unknown profile: {args[0]}"
            self.agent.config.profile=args[0]; from .router import Router; self.agent.router=Router(self.agent.config.current_profile()); return f"profile set to {args[0]}"
        if cmd=="/capabilities": from .capabilities import Capabilities; return str(Capabilities().as_dict())
        if cmd=="/guarantees": from .capabilities import Guarantees; return str(Guarantees().as_dict())
        if cmd=="/limitations": from .capabilities import Limitations; return str(Limitations().as_dict())
        if cmd=="/sessions": from .session import Session; return ", ".join(Session.list_sessions(self.agent.workspace/".apex"/"sessions")) or "(none)"
        if cmd=="/exit": return "bye."
        return f"Unknown command: {cmd}. Try /help."
