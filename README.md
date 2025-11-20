# Assistant par mots-clés — Projet NSI (Atil Idriss & Abou Shade Jonathan)

Résumé
Ce projet implante un petit site web assistant capable de recevoir des messages utilisateur, d'analyser le texte pour y détecter des mots‑clés, puis d'exécuter des actions associées (par exemple : si le message contient "météo" et "gap", l'assistant récupère la météo de Gap). L'idée est de proposer un assistant simple à la manière d'un "mini‑Google Assistant" centré sur des mots‑clés et actions prédéfinies.

Contenu du dépôt
- Programme SQL : script SQL contenant schéma et/ou données (tables) pour le projet.
- README.md : cette documentation.

Fonctionnalités envisagées
- Endpoint web recevant des messages en POST.
- Détection de mots‑clés et mapping vers des "actions" (ex : fetch météo, ouvrir un lien, renvoyer une information).
- Système de configuration des mots‑clés / actions (fichier JSON ou base de données).
- Exemple d'action implémentée : récupération de la météo via une API publique.
