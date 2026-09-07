# API auth42

## Se connecter
Rediriger vers : `http://localhost:8000/auth/login/`

## Savoir qui est connecté
`GET http://localhost:8000/auth/me/`

## Récupérer les piscineux + leur progression
`GET http://localhost:8000/auth/api/profils/` (faut être connecté)

Retourne :
```json
{
  "profils": [
    {
      "login": "nvieille",
      "email": "nvieille@student.42angouleme.fr",
      "first_name": "Noah",
      "last_name": "Vieillevillle",
      "image_url": "https://cdn.intra.42.fr/...",
      "lvl": 0.0,
      "projects": [
        { "name": "C Piscine C 00", "slug": "c-piscine-c-00", "valid": true, "note": 60 }
      ]
    }
  ]
}
```
