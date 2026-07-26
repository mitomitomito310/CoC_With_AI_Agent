#!/usr/bin/env python3
"""Generate or normalize auditable CoC D100 components."""
from __future__ import annotations
import argparse, json, secrets

def value(ones:int,tens:int)->int:
 if not 0<=ones<=9 or not 0<=tens<=9: raise ValueError('dice digits must be 0..9')
 return 100 if ones==0 and tens==0 else tens*10+ones

def select(ones:int,tens:list[int],modifier:int=0)->dict:
 if modifier not in (-1,0,1): raise ValueError('modifier must be -1, 0, or 1')
 if len(tens) < (2 if modifier else 1): raise ValueError('modifier requires two tens candidates')
 candidates=[value(ones,t) for t in tens]
 chosen=min(candidates) if modifier==1 else max(candidates) if modifier==-1 else candidates[0]
 return {'ones':ones,'tens_candidates':tens,'candidates':candidates,'selected':chosen,'modifier':modifier}

def roll(modifier:int=0)->dict:
 return select(secrets.randbelow(10),[secrets.randbelow(10) for _ in range(2 if modifier else 1)],modifier)
def main():
 p=argparse.ArgumentParser(); p.add_argument('--modifier',type=int,choices=[-1,0,1],default=0); p.add_argument('--ones',type=int); p.add_argument('--tens',type=int,nargs='+'); a=p.parse_args()
 print(json.dumps(select(a.ones,a.tens,a.modifier) if a.ones is not None else roll(a.modifier)))
if __name__=='__main__': main()
