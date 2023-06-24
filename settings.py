from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = Path.joinpath(ROOT, 'cw3', 'fixture')
DATA_PATH = Path.joinpath(FIXTURE_PATH, 'operations.json')