#!/usr/bin/env python3
"""
loopguard.py — stop the conversation when it starts repeating itself.

Signals:
  1. semantic similarity between recent assistant turns
  2. distinctive phrases recurring across turns
  3. "Would you like me to...?" tails on consecutive turns

Two of three tripping = LOOP. Prints a verdict with a forced fork.

  python tools/loopguard.py add "text..."   # log an assistant turn
  python tools/loopguard.py add -           # read turn from stdin
  python tools/loopguard.py check           # check; exit 2 if looping
  python tools/loopguard.py reset
"""
from __future__ import annotations
import sys, re, json, argparse
from pathlib import Path
from collections import Counter

LOG = Path("loopguard.jsonl")
WINDOW = 6                     # turns to inspect
SIM_THRESHOLD = None           # set below based on embedder
PHRASE_MIN_TURNS = 3           # a phrase must appear in >= this many turns
META_MIN_TURNS = 3             # meta-offers in >= this many of last WINDOW

STOP = set("""a an the and or but if then than that this these those is are was were be been
being of in on at to for from by with without into over under about as it its i you we they
he she do does did doing have has had having will would shall should can could may might must
not no nor so such only own same too very just also there here when where why how what which
who whom me my our your their his her them us""".split())

META_RE = re.compile(
    r"(would you like|do you want|shall we|want me to|should i|"
    r"do you want me to|next step[:?])\b.*\?",
    re.I | re.S,
)

# --- embedder (optional, better) ----------------------------------------
try:
    from sentence_transformers import SentenceTransformer
    _M = SentenceTransformer("all-MiniLM-L6-v2")
    SIM_THRESHOLD = 0.82
    def similarity(a: str, b: str) -> float:
        va, vb = _M.encode([a, b], normalize_embeddings=True)
        return float(va @ vb)
    MODE = "embeddings(MiniLM)"
except Exception:
    SIM_THRESHOLD = 0.35
    def _cw(t: str) -> set[str]:
        return {w for w in re.findall(r"[a-z][a-z\-]+", t.lower())
                if w not in STOP and len(w) > 3}
    def similarity(a: str, b: str) -> float:
        wa, wb = _cw(a), _cw(b)
        return len(wa & wb) / len(wa | wb) if wa and wb else 0.0
    MODE = "jaccard(fallback)"

def content_tokens(text: str) -> list[str]:
    return [t for t in re.findall(r"[a-z][a-z\-]+", text.lower())
            if t not in STOP and len(t) > 2]

def ngrams(tokens: list[str], n: int) -> set[str]:
    return {" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)}

def load() -> list[str]:
    if not LOG.exists():
        return []
    turns = []
    for line in LOG.read_text().splitlines():
        try:
            turns.append(json.loads(line)["text"])
        except Exception:
            pass
    return turns

def save_turn(text: str) -> None:
    with LOG.open("a") as f:
        f.write(json.dumps({"text": text}) + "\n")

def extract_phrases(turn: str) -> set[str]:
    toks = content_tokens(turn)
    return ngrams(toks, 2) | ngrams(toks, 3)

def check() -> dict:
    turns = load()[-WINDOW:]
    n = len(turns)
    if n < 3:
        return {"looping": False, "reason": f"only {n} turn(s) logged"}

    # signal 1 — pairwise similarity between the last two turns
    sim = similarity(turns[-1], turns[-2])
    sim_fired = sim >= SIM_THRESHOLD

    # signal 2 — phrases recurring across >= PHRASE_MIN_TURNS turns
    counter = Counter()
    for t in turns:
        for p in extract_phrases(t):
            counter[p] += 1
    recurring = [p for p, c in counter.most_common(12)
                 if c >= PHRASE_MIN_TURNS]
    phrase_fired = len(recurring) >= 2

    # signal 3 — meta-offers on many recent turns
    metas = sum(1 for t in turns if META_RE.search(t[-500:]))
    meta_fired = metas >= META_MIN_TURNS

    fired = sum([sim_fired, phrase_fired, meta_fired])
    looping = fired >= 2

    return {
        "looping": looping,
        "signals": {"similarity": sim_fired, "phrases": phrase_fired,
                    "meta_offers": meta_fired},
        "similarity": sim,
        "recurring_phrases": recurring[:8],
        "meta_count": metas,
        "window": n,
        "mode": MODE,
    }

def explain(v: dict) -> str:
    s = v["signals"]
    lines = [f"LOOP DETECTED across the last {v['window']} turns.", ""]
    lines.append(f"  [{'x' if s['similarity'] else ' '}] "
                 f"similarity {v['similarity']:.2f}  "
                 f"(threshold {SIM_THRESHOLD})")
    lines.append(f"  [{'x' if s['phrases'] else ' '}] "
                 f"recurring phrases: {', '.join(repr(p) for p in v['recurring_phrases'])}")
    lines.append(f"  [{'x' if s['meta_offers'] else ' '}] "
                 f"meta-offers on {v['meta_count']}/{v['window']} turns")
    lines += ["",
        "What this usually means: the model is elaborating on its own previous",
        "output rather than answering a new question. New words, same ideas.",
        "",
        "Fork — pick one before sending another prompt:",
        "  [r] Restate the actual goal in one sentence. Then continue.",
        "  [s] Ask for a concrete artifact (code, file, decision), not a design.",
        "  [d] Drop the thread. Open a new one with the goal as the first message.",
    ]
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("text")
    sub.add_parser("check")
    sub.add_parser("reset")
    args = ap.parse_args()

    if args.cmd == "add":
        text = sys.stdin.read() if args.text == "-" else args.text
        save_turn(text.strip())
        print(f"logged ({len(text)} chars)")
    elif args.cmd == "reset":
        LOG.unlink(missing_ok=True)
        print("cleared")
    elif args.cmd == "check":
        v = check()
        if not v["looping"]:
            print(f"ok ({v.get('reason') or v['mode']})")
            return
        print(explain(v))
        sys.exit(2)

if __name__ == "__main__":
    main()
