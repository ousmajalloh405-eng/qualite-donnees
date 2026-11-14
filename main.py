"""Pipeline Qualité des données."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from generate import generer_donnees_sales
from extract import extraire
from validate import valider_et_nettoyer
from load import initialiser_base, charger


CSV_PATH = Path(__file__).parent / "data" / "clients_bruts.csv"
DB_PATH = Path(__file__).parent / "data" / "clients.db"


def main():
    print("=== Pipeline Qualité des données ===\n")

    generer_donnees_sales(300, CSV_PATH)

    brut = extraire(CSV_PATH)
    print(f"Lignes brutes : {len(brut)}")

    propres, erreurs = valider_et_nettoyer(brut)
    print(f"Lignes valides : {len(propres)}")
    print(f"Lignes rejetées : {len(erreurs)}")

    if erreurs:
        print("\nExemples d'erreurs :")
        for e in erreurs[:5]:
            print(f"  ID {e['id']} : {e['problemes']}")

    conn = initialiser_base(DB_PATH)
    nb = charger(conn, propres)
    print(f"\nLignes chargées dans {DB_PATH} : {nb}")

    ca = conn.execute("SELECT ROUND(SUM(montant), 2) FROM clients").fetchone()[0]
    print(f"Montant total des clients valides : {ca}")

    conn.close()
    print("\nPipeline terminé.")


if __name__ == "__main__":
    main()
