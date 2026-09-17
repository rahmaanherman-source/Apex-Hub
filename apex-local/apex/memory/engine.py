from pathlib import Path
import sqlite3, json, time
class Memory:
 def __init__(self,path='data/apex_memory.sqlite3'):
  self.path=Path(path);self.path.parent.mkdir(parents=True,exist_ok=True);self.db=sqlite3.connect(self.path);self.db.execute('CREATE TABLE IF NOT EXISTS memory(id INTEGER PRIMARY KEY, namespace TEXT, content TEXT, metadata TEXT, created_at REAL)');self.db.commit()
 def add(self,content,namespace='default',metadata=None):
  self.db.execute('INSERT INTO memory(namespace,content,metadata,created_at) VALUES(?,?,?,?)',(namespace,content,json.dumps(metadata or {}),time.time()));self.db.commit()
 def search(self,term,namespace=None,limit=20):
  q='SELECT id,namespace,content,metadata,created_at FROM memory WHERE content LIKE ?';args=[f'%{term}%']
  if namespace:q+=' AND namespace=?';args.append(namespace)
  q+=' ORDER BY created_at DESC LIMIT ?';args.append(limit);return self.db.execute(q,args).fetchall()
