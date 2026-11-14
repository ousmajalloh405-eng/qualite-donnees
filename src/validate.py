"""Validation et nettoyage de la qualité des données."""

from typing import List, Dict, Tuple
import re

def valider_et_nettoyer(lignes: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """Retourne (données propres, rapport d'erreurs)."""
    propres = []
    erreurs = []

    for ligne in lignes:
        problemes = []
        propre = ligne.copy()

        if not ligne.get("nom") or not ligne["nom"].strip():
            problemes.append("nom manquant")
        else:
            propre["nom"] = ligne["nom"].strip().title()

        email = ligne.get("email", "")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            problemes.append("email invalide")

        try:
            age = int(ligne["age"])
            if not (0 < age < 120):
                problemes.append("age hors limites")
            else:
                propre["age"] = age
        except (ValueError, TypeError):
            problemes.append("age invalide")

        ville = ligne.get("ville", "").strip()
        if not ville:
            problemes.append("ville manquante")
        else:
            propre["ville"] = ville.title()

        try:
            montant = float(ligne["montant"])
            if montant < 0:
                problemes.append("montant négatif")
            else:
                propre["montant"] = round(montant, 2)
        except (ValueError, TypeError):
            problemes.append("montant invalide")

        if problemes:
            erreurs.append({"id": ligne.get("id"), "problemes": ", ".join(problemes)})
        else:
            propres.append(propre)

    return propres, erreurs
