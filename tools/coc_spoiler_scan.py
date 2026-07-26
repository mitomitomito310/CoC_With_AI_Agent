#!/usr/bin/env python3
"""Heuristic public-output leakage gate; human semantic review remains required."""
from __future__ import annotations
import argparse,json
from pathlib import Path

def scan(text:str,canaries:list[str])->list[str]: return [c for c in canaries if c and c.casefold() in text.casefold()]
def main():
 p=argparse.ArgumentParser(); p.add_argument('public'); p.add_argument('canaries'); a=p.parse_args(); hits=scan(Path(a.public).read_text(),json.loads(Path(a.canaries).read_text())); print(json.dumps({'safe':not hits,'hits':hits},ensure_ascii=False)); raise SystemExit(bool(hits))
if __name__=='__main__': main()
