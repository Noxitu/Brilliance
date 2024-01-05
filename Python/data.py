import json
from pathlib import Path
import sys


def _init():
    root = Path(__file__).parent / 'data'
    module = sys.modules[__name__]

    for path in root.glob("*.json"):
        name = path.stem.lstrip('_').upper()
        with open(path, encoding='utf-8') as fd:
            data = json.load(fd)
            setattr(module, name, data)

_init()
