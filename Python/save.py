import json
from pathlib import Path


ROOT = Path(__file__).parent.parent / 'Brilliance Datapack'


def save(path, item=None):
    path = ROOT / path
    path.parent.mkdir(exist_ok=True, parents=True)

    if item is None:
        return open(path, "wt", encoding="utf-8")

    if path.suffix == ".json":
        with open(path, "wt", encoding="utf-8") as fd:
            json.dump(item, fd, indent=4)

    else:
        path.write_text(item)