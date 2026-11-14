"""Chargement des données propres dans SQLite."""

import sqlite3
from pathlib import Path
from typing import List, Dict

def initialiser_base(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            nom TEXT,
            email TEXT,
            age INTEGER,
            ville TEXT,
            montant REAL
        )
    """)
    conn.commit()
    return conn

def charger(conn: sqlite3.Connection, data: List[Dict]) -> int:
    conn.execute("DELETE FROM clients")
    for c in data:
        conn.execute(
            "INSERT INTO clients (id, nom, email, age, ville, montant) VALUES (?, ?, ?, ?, ?, ?)",
            (c["id"], c["nom"], c["email"], c["age"], c["ville"], c["montant"]),
        )
    conn.commit()
    return len(data)
