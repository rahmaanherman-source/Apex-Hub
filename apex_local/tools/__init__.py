from __future__ import annotations
from .fs import read_file, list_dir, write_file, edit_file
from .shell import run_shell
from .search import search, glob

TOOL_SPECS = [
    {"name":"read_file","description":"Read a file inside the workspace.","parameters":{"path":"string"}},
    {"name":"list_dir","description":"List a directory inside the workspace.","parameters":{"path":"string"}},
    {"name":"write_file","description":"Create or replace a file.","parameters":{"path":"string","content":"string"}},
    {"name":"edit_file","description":"Replace text in a file.","parameters":{"path":"string","old":"string","new":"string"}},
    {"name":"run_shell","description":"Run a shell command in the workspace.","parameters":{"cmd":"string"}},
    {"name":"search","description":"Regex-search file contents.","parameters":{"pattern":"string","path":"string"}},
    {"name":"glob","description":"Glob filenames.","parameters":{"pattern":"string"}},
]

def dispatch(tool_name: str, args: dict, sandbox) -> dict:
    try:
        if tool_name == "read_file": return read_file(sandbox,args.get("path",""))
        if tool_name == "list_dir": return list_dir(sandbox,args.get("path","."))
        if tool_name == "write_file": return write_file(sandbox,args["path"],args.get("content",""))
        if tool_name == "edit_file": return edit_file(sandbox,args["path"],args["old"],args["new"])
        if tool_name == "run_shell": return run_shell(sandbox,args["cmd"])
        if tool_name == "search": return search(sandbox,args["pattern"],args.get("path","."))
        if tool_name == "glob": return glob(sandbox,args["pattern"])
        return {"ok":False,"error":f"unknown tool: {tool_name}"}
    except Exception as e:
        return {"ok":False,"error":str(e)}
