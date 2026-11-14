"""Génération de données avec problèmes de qualité."""

import csv
import random
from pathlib import Path

def generer_donnees_sales(n: int = 300, fichier: Path = Path("data/clients_bruts.csv")) -> None:
    fichier.parent.mkdir(parents=True, exist_ok=True)
    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "nom", "email", "age", "ville", "montant"])
        for i in range(1, n + 1):
            nom = random.choice(["Diallo", "Ndiaye", "Fall", "Sow", "Ba", ""])
            email = f"user{i}@example.com" if random.random() > 0.05 else "email_invalide"
            age = random.randint(18, 80) if random.random() > 0.04 else random.choice([-5, 150, ""])
            ville = random.choice(["Dakar", "Thiès", "Saint-Louis", "dakar", "DAKAR", ""])
            montant = round(random.uniform(10, 500), 2) if random.random() > 0.03 else random.choice([-100, "", "abc"])
            writer.writerow([i, nom, email, age, ville, montant])
    print(f"{n} lignes générées (avec erreurs) dans {fichier}")
