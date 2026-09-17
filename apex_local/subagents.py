from __future__ import annotations
import threading
from dataclasses import dataclass
from typing import Any, Callable

@dataclass
class SubagentTask:
    name:str; fn:Callable[[],Any]; result:Any=None; error:str|None=None; done:bool=False

class SubagentPool:
    def __init__(self): self._tasks={}; self._threads=[]
    def add(self,name,fn): self._tasks[name]=SubagentTask(name,fn)
    def run_all(self):
        def wrap(t):
            try:t.result=t.fn()
            except Exception as e:t.error=str(e)
            finally:t.done=True
        for t in self._tasks.values():
            th=threading.Thread(target=wrap,args=(t,),daemon=True); self._threads.append(th); th.start()
        for th in self._threads: th.join()
        return self._tasks
