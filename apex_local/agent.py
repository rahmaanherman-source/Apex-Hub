from __future__ import annotations
import json
from dataclasses import dataclass
from pathlib import Path
from .config import APEXConfig
from .sandbox import Sandbox
from .permissions import PermissionGate, Mode, Decision
from .router import Router
from .providers import ChatMessage, GenerateRequest
from .tools import dispatch, TOOL_SPECS

SYSTEM_PROMPT = """You are APEX Local, a terminal agent. Prefer reading/searching before writing. Keep shell commands short and reversible. Never invent file contents."""

@dataclass
class TurnResult:
    text: str
    tool_trace: list[dict]
    finished: bool

class Agent:
    def __init__(self, config: APEXConfig, auto_yes: bool=False, interactive: bool=True):
        self.config=config
        self.workspace=Path(config.workspace).expanduser().resolve()
        self.sandbox=Sandbox(str(self.workspace))
        self.router=Router(config.current_profile())
        self.gate=PermissionGate(Mode(config.mode),auto_yes)
        self.interactive=interactive

    def _ask(self,q):
        if not self.interactive: return False
        try: return input(f"\n[permission] {q} [y/N] ").strip().lower() in ("y","yes")
        except EOFError: return False

    def run(self,user_message:str,max_steps:int=12)->TurnResult:
        provider=self.router.pick(); messages=[ChatMessage("system",SYSTEM_PROMPT),ChatMessage("user",user_message)]; trace=[]
        for _ in range(max_steps):
            resp=provider.generate(GenerateRequest(messages=messages,tools=TOOL_SPECS,temperature=.2))
            if not resp.tool_calls: return TurnResult(resp.text,trace,True)
            for call in resp.tool_calls:
                name=call.get("name",""); args=call.get("args",{}) or {}; decision=self.gate.check(name,args)
                if decision==Decision.DENY: result={"ok":False,"error":f"denied by mode={self.config.mode}"}
                elif decision==Decision.ASK and not self._ask(f"{name}({json.dumps(args)[:140]}) ?"): result={"ok":False,"error":"user denied"}
                else: result=dispatch(name,args,self.sandbox)
                trace.append({"tool":name,"args":args,"result":result}); messages.append(ChatMessage("tool",json.dumps(result)[:4000],name=name))
        return TurnResult(f"[stopped after {max_steps} steps]",trace,True)
