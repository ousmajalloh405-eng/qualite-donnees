# Architecture — Qualité des données

## Flux

```
Données brutes (avec erreurs)
          │
          ▼
     extract.py
          │
          ▼
    validate.py
   (règles métier)
          │
     ┌────┴────┐
     ▼         ▼
Données     Rapport
propres    d'erreurs
     │
     ▼
  load.py → clients.db
```

## Règles de validation

| Champ | Règle |
|-------|-------|
| nom | Non vide |
| email | Format valide |
| age | Entre 1 et 119 |
| ville | Non vide |
| montant | Nombre ≥ 0 |
