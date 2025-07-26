
---

## 🎯 Chapitre 1 — Anatomie d’un bon prompt : précision, contexte et intention

> Le prompt n’est pas une commande. C’est une interface de pensée. Il structure le dialogue, oriente la réponse, et conditionne la qualité de la collaboration.

### Pourquoi ce chapitre ?

Dans tout échange avec un LLM, **le prompt est le point d’entrée**. C’est lui qui définit le cadre, la tâche, le niveau de détail attendu. Mais un bon prompt ne se résume pas à une question bien formulée. C’est un acte de design.  
Il combine trois dimensions fondamentales : la **précision**, le **contexte** et l’**intention**.  
Il s’apparente à une interface entre deux intelligences : humaine et artificielle.

Dans ce chapitre, nous proposons une grille simple mais robuste pour concevoir des prompts utiles, exploitables et adaptés aux situations réelles de développement logiciel.

---

### Trois dimensions fondamentales d’un prompt efficace

#### 1. **Précision : clarifier ce que vous attendez**

Un prompt vague produit une réponse vague.

> ❌ *« Donne-moi un code de trie. »*  
> ✅ *« Écris une fonction Python qui trie une liste de dictionnaires par la clé ‘date’, en ordre décroissant. »*

Soyez explicite. Précisez la tâche, le niveau de détail, le langage.  
Définissez les frontières de la réponse attendue.

#### 2. **Contexte : donner au modèle de quoi raisonner juste**

Un LLM ne connaît pas l'ensemble de votre projet, ni vos contraintes. C’est à vous de les formuler.

> *« Je développe une API REST en Node.js, dans un environnement de microservices conteneurisés via Docker. »*

Fournir le bon contexte, c’est permettre une réponse plus ciblée, plus pertinente, plus réaliste.

<div class="pb-A4"></div>

#### 3. **Intention : dire pourquoi vous posez la question**

La qualité de l’échange dépend de la clarté du but visé.

> *« Je veux que même un stagiaire puisse exécuter ce script sans risque d’erreur. »*

Nommer l’intention, c’est guider la forme, le ton, et le niveau de complexité de la réponse.

---

### 🗨️ Le prompt est une conversation amorcée

Il est utile de voir le prompt non comme une requête, mais comme la **première phrase d’un échange**. Un bon prompt **ouvre l’espace de dialogue**, il invite à l’itération, à la reformulation, au rebond. Il pose un cadre… mais laisse de la place à la co-construction.

---

### 🧭 Typologie des formes de prompts

Voici quelques formats fréquents que vous retrouverez dans la bibliothèque de motifs (chapitre 4) :

| Type de prompt          | Exemple                                                                                    | Usage typique                                 |
|-------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------|
| **Contexte + Tâche**    | « Dans le cadre d’un service d’authentification OAuth2 en Go, écris un middleware... »     | Implémentation ciblée                         |
| **Exemple + Variation** | « Voici une fonction JS. Peux-tu proposer une version plus performante avec `reduce` ? »   | Refactor, optimisation                        |
| **Roleplay**            | « Agis comme un expert Django senior. Quelles étapes pour refactorer cette application ? » | Conseil spécialisé, expertise simulée         |
| **Pas-à-pas**           | « Explique étape par étape comment sécuriser une API contre les attaques CSRF. »           | Pédagogie, onboarding, formation              |
| **Cascade**             | « Ajoute un système de trace des actions dans des logs spécifiques »                       | Implémentation ciblée, Refactor, optimisation |

---

<div class="pb-A4"></div>

### ✅ Bonnes pratiques

* Formatez vos prompts avec des **puces, blocs de code ou titres** pour structurer la pensée.
* Ajoutez des **exemples** : ils guident le modèle et clarifient vos attentes.
* Soyez explicite sur :
  * le langage et la version utilisés ;
  * le style ou niveau attendu ;
  * les contraintes spécifiques (techniques, fonctionnelles, organisationnelles).

---

### ❌ Erreurs fréquentes à éviter

* Empiler plusieurs demandes dans un seul prompt.
* Employer des termes flous : “améliore”, “rends ça plus propre”… sans critère.
* Oublier de formuler l’objectif réel derrière la tâche demandée.

---

### 🧪 Exemple comparatif

#### Prompt faible :

> *« Fais-moi une API Node. »*

🔁 Résultat : réponse générique, peu exploitable.

#### Prompt amélioré :

> *« Je veux créer une API REST en Node.js avec Express. Elle doit gérer des utilisateurs stockés dans MongoDB. Je souhaite une architecture modulaire, sans ORM, avec séparation claire des responsabilités. Peux-tu proposer une structure de fichiers et le code de base ? »*

✅ Résultat : réponse structurée, contextualisée, directement exploitable.

---

### 🛠 Fiche-outil — Structure d’un bon prompt

| Élément            | Exemple                                                                 |
|--------------------|-------------------------------------------------------------------------|
| **Contexte**       | « Je travaille sur une API FastAPI en Python déployée sur AWS Lambda… » |
| **Tâche claire**   | « Je veux une fonction qui valide un token JWT dans les headers HTTP. » |
| **Contraintes**    | « Sans ORM, logs clairs en cas d’échec, Python 3.10. »                  |
| **Intention**      | « Le but est que ce soit compréhensible pour un développeur junior. »   |
| **Format attendu** | « Exemple commenté + tests unitaires. »                                 |

---

<div class="pb-A4"></div>

### ✏️ En résumé

Un bon prompt, c’est :

* 🎯 une demande claire,
* 🧱 un contexte explicite,
* 🧠 une intention formulée,
* 📦 un format de réponse attendu.

C’est la base de toute collaboration fructueuse avec un LLM.

> « Ce n’est pas l’IA qui est floue. C’est souvent notre manière de lui parler. » *ChatGPT*
