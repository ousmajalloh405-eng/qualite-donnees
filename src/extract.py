"""Extraction des données brutes."""

import csv
from pathlib import Path
from typing import List, Dict

def extraire(fichier: Path) -> List[Dict]:
    with open(fichier, encoding="utf-8") as f:
        return list(csv.DictReader(f))
