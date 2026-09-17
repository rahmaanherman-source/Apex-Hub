from __future__ import annotations
from typing import Callable

EVENTS=("session_start","session_end","before_tool","after_tool","before_write")
class HookRegistry:
    def __init__(self): self._hooks={}
    def on(self,event:str,fn:Callable)->None: self._hooks.setdefault(event,[]).append(fn)
    def emit(self,event:str,**payload)->None:
        for fn in self._hooks.get(event,[]):
            try: fn(**payload)
            except Exception: pass
