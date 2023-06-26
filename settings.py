from pathlib import Path

# Создание пути к файлу с трансакциями, независимого от файловой системы
ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = Path.joinpath(ROOT, 'cw3', 'fixture')
DATA_PATH = Path.joinpath(FIXTURE_PATH, 'operations.json')