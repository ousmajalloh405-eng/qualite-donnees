# Qualité des données

> Pipeline de validation et de nettoyage de données (détection d’erreurs, rejet des lignes invalides, stockage des données propres).

**Statut** : 🟢 Réalisé  
**Catégorie** : 🛡️ Qualité des données  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## 1. Problème métier

Des données clients arrivent avec des erreurs (emails invalides, âges aberrants, montants négatifs…). Il faut les détecter, les rejeter ou les corriger avant analyse.

## 2. Architecture

```
generate.py → clients_bruts.csv (avec erreurs)
      │
      ▼
 extract.py → validate.py → load.py → clients.db
                  │
                  ▼
            Rapport d'erreurs
```

## 3. Contrôles effectués

- Nom manquant
- Email invalide
- Âge hors limites (0-120)
- Ville manquante
- Montant négatif ou non numérique

## 4. Technologies

- Python 3
- Bibliothèque standard
- SQLite

## 5. Installation et exécution

```bash
git clone https://github.com/ousmajalloh405-eng/qualite-donnees.git
cd qualite-donnees
python3 main.py
```

## 6. Compétences pour le CV

Mise en place d’un pipeline de qualité des données : génération de données erronées, validation de règles métier, rejet des lignes invalides et chargement des données propres.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
