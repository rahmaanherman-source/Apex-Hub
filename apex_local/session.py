from __future__ import annotations
import json, time, uuid
from pathlib import Path
from .providers import ChatMessage

class Session:
    def __init__(self,root:Path,session_id=None):
        self.root=root; self.root.mkdir(parents=True,exist_ok=True); self.id=session_id or uuid.uuid4().hex[:12]; self.path=root/f"{self.id}.jsonl"; self.messages=[]
    def append(self,msg:ChatMessage):
        self.messages.append(msg)
        with self.path.open("a",encoding="utf-8") as f: f.write(json.dumps({"ts":time.time(),"role":msg.role,"content":msg.content,"name":msg.name})+"\n")
    def context(self,max_messages=40): return self.messages[-max_messages:]
    @classmethod
    def load(cls,root,session_id):
        s=cls(root,session_id)
        if s.path.exists():
            for line in s.path.read_text(encoding="utf-8").splitlines():
                try:
                    r=json.loads(line); s.messages.append(ChatMessage(r["role"],r["content"],r.get("name")))
                except Exception: pass
        return s
    @classmethod
    def list_sessions(cls,root): return sorted(p.stem for p in root.glob("*.jsonl")) if root.exists() else []
