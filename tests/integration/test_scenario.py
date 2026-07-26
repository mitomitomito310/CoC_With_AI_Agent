import hashlib,json
from pathlib import Path
from tools.coc_validate import validate_scenario
from tools.coc_spoiler_scan import scan
ROOT=Path(__file__).parents[2]
def test_fixture_integrity(): assert validate_scenario(ROOT/'tests/fixtures/minimal_original/scenario.json')==[]
def test_source_immutable_checksum():
 d=json.loads((ROOT/'tests/fixtures/minimal_original/scenario.json').read_text()); src=ROOT/'tests/fixtures/minimal_original'/d['source'][0]['path']; assert hashlib.sha256(src.read_bytes()).hexdigest()==d['source'][0]['sha256']
def test_spoiler_canary():
 assert scan('開始できます。',['時計は展示台の裏','佐伯'])==[]
 assert scan('佐伯が隠した',['佐伯'])==['佐伯']
