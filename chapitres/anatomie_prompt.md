
---

## Chapitre — Anatomie d’un bon prompt : précision, contexte et intention

> Le prompt est au cœur de toute interaction réussie avec un LLM. Avant d’explorer les motifs, découvrons comment formuler des demandes claires, contextualisées et orientées vers un but précis.

Les performances des modèles de langage ne dépendent pas uniquement de leur puissance technique, mais surtout de **la qualité de l’interaction** qu’on construit avec eux. Et au cœur de cette interaction se trouve l’art du *prompt*. Ce chapitre propose une plongée dans la construction de bons prompts, en analysant leurs composants essentiels, en montrant des exemples concrets, et en définissant des motifs récurrents d’écriture.

### Pourquoi ce chapitre ?

Trop souvent, on pense qu’un prompt est une simple question. Mais un bon prompt est en réalité un **acte de design**, une manière de structurer la pensée, de poser le cadre, de transmettre une intention. Il s’apparente à une interface entre deux intelligences : humaine et artificielle.

### Trois dimensions fondamentales

1. **Précision** : éviter les formulations vagues, ambigües ou multi-interprétables.
   → Ex : "Donne-moi un code Python" → **trop large**
   ✅ Préférer : "Écris une fonction Python qui trie une liste de dictionnaires par une clé 'date', en ordre décroissant."

2. **Contexte** : fournir les éléments utiles pour cadrer la réponse : langage, environnement, style, contraintes métier…
   → Ex : "Je développe une API REST en Node.js dans un contexte de microservices gérés par Docker."

3. **Intention** : exprimer clairement le *but* visé, pas seulement la tâche.
   → Ex : "Je veux un script Shell pour automatiser le déploiement, afin que même un stagiaire puisse l’exécuter sans rien casser."

> 📌 **Encadré — Le prompt n’est pas une requête, c’est une conversation dirigée**
>
> Il est utile de penser le prompt comme une amorce de conversation, pas comme un ordre. Le prompt bien conçu contient souvent une *dynamique* : il prépare la suite du dialogue. Un bon prompt anticipe les rebonds, les vérifications, les approfondissements. Il ouvre l’espace d’échange au lieu de le fermer.

---

### Typologie des prompts efficaces

Nous proposons ici une typologie structurée, illustrée de motifs que l’on retrouvera tout au long du livre :

* **Prompt "Contexte + Tâche"** :

  > "Dans le cadre d’un service d’authentification OAuth2 en Go, écris un middleware qui vérifie la présence d’un token JWT valide."

* **Prompt "Exemple + Variation"** :

  > "Voici une fonction JavaScript pour filtrer un tableau. Peux-tu proposer une version plus performante avec `reduce` ?"

* **Prompt "Roleplay"** :

  > "Agis comme un expert Django senior. Donne-moi les étapes clés pour refactorer une app monolithique en microservices."

* **Prompt "Pas-à-pas"** :

  > "Explique-moi étape par étape comment sécuriser une API avec des jetons CSRF, comme à un étudiant de niveau bac+2."

---

### Bonnes pratiques et erreurs fréquentes

✅ **Bonnes pratiques** :

* Être explicite sur les contraintes : langage, version, bibliothèque cible.
* Utiliser le formatage (listes, bullet points, code blocks) pour structurer la demande.
* Préciser le niveau de détail attendu : résumé, tutoriel, snippet, code complet, benchmark ?

❌ **Erreurs fréquentes** :

* Poser plusieurs questions en une.
* Employer des termes vagues : "optimiser", "simplifier", "améliorer" — sans dire ce qu’on entend par là.
* Oublier le *pourquoi* de la demande.

---

### Exemple comparatif

**Prompt faible :**

> "Fais-moi une API Node."

**Résultat :** réponse générique, non contextualisée.

**Prompt amélioré :**

> "Je veux créer une API REST en Node.js avec Express. Elle doit permettre de créer, lire, mettre à jour et supprimer des utilisateurs stockés dans une base MongoDB. Je veux du code modulaire, avec une bonne séparation des responsabilités, sans ORM. Peux-tu me proposer la structure de fichiers et le code de base pour démarrer proprement ?"

**Résultat :** réponse structurée, adaptée, directement exploitable.

---

### 🧰 Fiche-outil — Anatomie d’un bon prompt

#### 🎯 Objectif

Concevoir un prompt efficace pour interagir avec un LLM dans un contexte de développement logiciel, en maximisant la pertinence et l’utilité des réponses.

---

#### 📐 Structure type d’un prompt efficace

| Élément            | Description                                              | Exemple                                                                           |
|--------------------| -------------------------------------------------------- |-----------------------------------------------------------------------------------|
| **Contexte**       | Donne le cadre technique, fonctionnel ou organisationnel | "Je travaille sur une API REST en Python avec FastAPI, déployée sur AWS Lambda…"  |
| **Tâche claire**   | Décrit précisément ce que vous attendez                  | "…je veux une fonction pour vérifier un JWT dans les headers d’une requête HTTP." |
| **Contraintes**    | Précise les choix technos, limites ou préférences        | "Sans utiliser d’ORM, et avec des logs clairs en cas d’échec de validation."      |
| **Intention**      | Fait apparaître le *pourquoi* de la demande              | "Je veux que ce soit simple à comprendre pour un développeur junior."             |
| **Format attendu** | Indique le type de réponse souhaitée                     | "Peux-tu me donner un exemple commenté + les tests unitaires correspondants ?"    |

---

#### 📎 Astuces pratiques

* **Soyez spécifique** : un prompt générique donne une réponse générique.
* **Pensez séquence** : un bon prompt n’est que le premier pas d’un échange.
* **Nommez vos contraintes** : langage, bibliothèque, niveau de détail.
* **Ajoutez des exemples** : un exemple concret inspire une meilleure réponse.

---

#### ⚠️ À éviter

* ❌ Phrases trop générales : "fais-moi un code", "aide-moi avec ce bug"
* ❌ Absence de contexte : pas de langage, pas d’architecture, pas de but
* ❌ Prompts fourre-tout : trop d’idées mélangées, pas de hiérarchisation

---

#### 🧪 Exemple comparé

| Prompt faible                            | Prompt amélioré                                                                                                                                                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Donne-moi un code pour une API Node.js" | "Crée une API REST en Node.js avec Express, qui gère des utilisateurs stockés dans MongoDB. Structure le code en suivant une architecture MVC, sans ORM. J’ai besoin des routes CRUD, d’une validation d’entrée, et de quelques tests unitaires." |
