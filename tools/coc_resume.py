#!/usr/bin/env python3
"""Build deterministic, audience-separated resume projections from current state."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def projections(current:dict)->dict:
 required={'scenario_id','state_version','public','keeper','npcs'}
 missing=required-current.keys()
 if missing: raise ValueError(f'missing current fields: {sorted(missing)}')
 base={'scenario_id':current['scenario_id'],'state_version':current['state_version'],
       'last_checkpoint_id':current.get('last_checkpoint_id')}
 public={**base,'public':current['public']}
 keeper={**base,'public':current['public'],'keeper':current['keeper'],'npcs':current['npcs']}
 npcs={npc_id:{**base,'public':current['public'],'knowledge':knowledge}
       for npc_id,knowledge in current['npcs'].items()}
 return {'public':public,'keeper':keeper,'npcs':npcs}


def render_markdown(view:dict,audience:str)->str:
 payload=json.dumps(view,ensure_ascii=False,indent=2,sort_keys=True)
 return f'# Resume: {audience}\n\n<!-- generated from committed current state; do not edit -->\n\n```json\n{payload}\n```\n'


def write_projections(current_path:Path,output_dir:Path)->list[Path]:
 views=projections(json.loads(current_path.read_text())); output_dir.mkdir(parents=True,exist_ok=True); written=[]
 for audience in ('public','keeper'):
  path=output_dir/f'{audience}.md'; path.write_text(render_markdown(views[audience],audience)); written.append(path)
 npc_dir=output_dir/'npcs'; npc_dir.mkdir(exist_ok=True)
 for npc_id,view in views['npcs'].items():
  if '/' in npc_id or npc_id in {'.','..'}: raise ValueError('unsafe npc_id')
  path=npc_dir/f'{npc_id}.md'; path.write_text(render_markdown(view,f'npc:{npc_id}')); written.append(path)
 return written


def main():
 p=argparse.ArgumentParser(); p.add_argument('current',type=Path); p.add_argument('output',type=Path)
 a=p.parse_args(); print('\n'.join(str(x) for x in write_projections(a.current,a.output)))


if __name__=='__main__': main()
