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
      ],
      "comments": [
        { "author": "rcompain", "content": "Bloqué sur le C03", "created_at": "2026-09-10T16:30:32.843808+00:00" }
      ]
    }
  ]
}
```

## Créer un commentaire sur un piscineux

`POST http://localhost:8000/auth/comment/<login>/` (faut être connecté)

Body JSON attendu :
```json
{ "content": "Le texte du commentaire" }
```

Pas besoin d'envoyer l'auteur — déterminé automatiquement à partir du tuteur connecté.

Réponses : `200` `{"message": "Comment created."}` · `401` pas connecté · `400` `content` manquant · `404` login inconnu.

```js
fetch("http://localhost:8000/auth/comment/nvieille/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  credentials: "include",
  body: JSON.stringify({ content: "Bloqué sur le C03" }),
})
  .then(res => res.json())
  .then(data => console.log(data));
```

Le commentaire apparaît ensuite dans `comments` via `GET /auth/api/profils/`.
