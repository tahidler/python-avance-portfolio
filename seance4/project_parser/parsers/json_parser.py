import json
from typing import Any


def parse_json(path: str) -> Any:
    """Parser un fichier JSON vers des données Python."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
