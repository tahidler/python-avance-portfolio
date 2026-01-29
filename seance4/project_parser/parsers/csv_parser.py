import csv
from typing import List, Dict, Any


def parse_csv(path: str) -> List[Dict[str, Any]]:
    """Parser un fichier CSV en une liste de dictionnaires."""
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [row for row in reader]
