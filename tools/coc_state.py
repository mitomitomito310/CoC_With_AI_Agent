#!/usr/bin/env python3
"""Scenario lifecycle rules with auditable transitions."""
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

TRANSITIONS = {
 "importing":{"preparing","blocked"}, "preparing":{"ready","blocked"},
 "blocked":{"preparing","archived"}, "ready":{"active","archived"},
 "active":{"paused","completed"}, "paused":{"active","completed","archived"},
 "completed":{"archived"}, "archived":set(),
}

def transition(doc:dict, target:str, reason:str, *, now:str|None=None)->dict:
 current=doc.get("status")
 if target not in TRANSITIONS.get(current,set()):
  raise ValueError(f"invalid scenario transition: {current} -> {target}")
 if target=="ready" and doc.get("blocking_issues"):
  raise ValueError("blocked scenario cannot become ready")
 if target=="active" and not doc.get("opening",{}).get("scene_id"):
  raise ValueError("active scenario requires an opening scene")
 out=json.loads(json.dumps(doc)); out["status"]=target; out["status_reason"]=reason
 out["updated_at"]=now or datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
 if target=="active" and not out.get("current_scene_id"): out["current_scene_id"]=out["opening"]["scene_id"]
 return out

def main():
 p=argparse.ArgumentParser(); p.add_argument('scenario'); p.add_argument('target'); p.add_argument('--reason',required=True); p.add_argument('--write',action='store_true'); a=p.parse_args()
 path=Path(a.scenario); result=transition(json.loads(path.read_text()),a.target,a.reason)
 if a.write: path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 else: print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
