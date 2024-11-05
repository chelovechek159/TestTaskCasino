import json

from from_root import from_root


def get_config():
    with open(f"{from_root()}/config.json") as f:
        return json.load(f)
