from __future__ import annotations
import argparse, json
from pathlib import Path
from . import __version__
from .config import APEXConfig
from .agent import Agent


def main(argv=None):
    p=argparse.ArgumentParser(prog="apex",description="APEX Local — terminal agent")
    p.add_argument("--version",action="version",version=f"apex {__version__}")
    sub=p.add_subparsers(dest="cmd",required=True)
    i=sub.add_parser("init"); i.add_argument("--workspace",default=None); i.add_argument("--profile",default=None)
    s=sub.add_parser("status")
    pr=sub.add_parser("profiles")
    r=sub.add_parser("run"); r.add_argument("prompt",nargs="?"); r.add_argument("--workspace",default=None); r.add_argument("--profile",default=None); r.add_argument("--mode",choices=["ask","accept-edits","read-only"],default=None); r.add_argument("--auto-yes",action="store_true"); r.add_argument("--headless",action="store_true")
    args=p.parse_args(argv); cfg=APEXConfig.load()
    if args.cmd=="init":
        if args.workspace: cfg.workspace=args.workspace
        if args.profile: cfg.profile=args.profile
        cfg.save(); print(f"Initialized APEX at {Path(cfg.workspace).resolve()}"); return 0
    if args.cmd=="status":
        prof=cfg.current_profile(); print(json.dumps({"version":__version__,"profile":prof.name,"provider":prof.provider,"model":prof.model,"mode":cfg.mode,"workspace":str(Path(cfg.workspace).resolve()),"profiles":list(cfg.profiles)},indent=2)); return 0
    if args.cmd=="profiles":
        for n,pf in cfg.profiles.items(): print(("*" if n==cfg.profile else " ")+f" {n:10s} provider={pf.provider:8s} model={pf.model}"); return 0
    if args.workspace: cfg.workspace=args.workspace
    if args.profile: cfg.profile=args.profile
    if args.mode: cfg.mode=args.mode
    agent=Agent(cfg,auto_yes=args.auto_yes,interactive=not args.headless)
    if args.prompt: print(agent.run(args.prompt).text); return 0
    print("APEX Local — type Ctrl-D to quit")
    while True:
        try: line=input("apex> ").strip()
        except (EOFError,KeyboardInterrupt): print(); break
        if line: print(agent.run(line).text)
    return 0

if __name__=="__main__": raise SystemExit(main())
