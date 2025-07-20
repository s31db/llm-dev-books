
---

## 🗺️ Chapitre 5 — Cartographier les usages : typologie des situations et des rôles

> Concevoir avec un LLM, ce n’est pas appliquer une méthode linéaire. C’est **naviguer dans un espace d’interactions possibles**, qui varie selon le contexte, l’intention, et le niveau de maturité. Ce chapitre propose une **carte de ces usages**, à la fois pour mieux s’orienter et pour enrichir sa pratique.

---

### 🧭 Pourquoi ce chapitre ?

Nous avons exploré :

* des **motifs conversationnels** (Chapitre 3) — les gestes de base de l’interaction avec un LLM,
* des **rôles et postures** qui émergent dans les équipes (Chapitre 4) — les transformations en cours.

Il est maintenant temps de **connecter ces dimensions au terrain** : à ce que l’on fait concrètement avec un LLM, dans des situations précises.

> L’objectif n’est pas d’exhaustivement modéliser tous les cas d’usage, mais d’**offrir une boussole** : pour reconnaître où l’on est, choisir un motif adapté, et évoluer vers des pratiques plus fluides et conscientes.

---

### 🧩 Typologie des situations

Voici une première **typologie de six situations-types** fréquemment rencontrées dans le travail logiciel augmenté par un LLM. Chaque situation est décrite par :

* une **intention centrale** (ce que l’on cherche à faire),
* des **postures activées** (comment on interagit avec le LLM),
* des **motifs associés** (les gestes conversationnels les plus utiles).

| 🧩 Situation        | 🎯 Intention principale                        | 👤 Posture(s) activée(s)     | 🧠 Motifs typiques                              |
| ------------------- | ---------------------------------------------- | ---------------------------- | ----------------------------------------------- |
| **Exploration**     | Découvrir un domaine, une techno, une approche | Explorateur, apprenant       | Exploration guidée, Modèle miroir               |
| **Cadrage**         | Clarifier un besoin flou ou implicite          | Formulateur, facilitateur    | Question socratique, Décomposition, Spéc. inv.  |
| **Refactorisation** | Améliorer un existant                          | Analyste, critiqueur         | Spécification inversée, Contre-exemple          |
| **Documentation**   | Générer ou reconstruire du sens                | Synthétiseur, documentaliste | Spécification inversée, Résumé ciblé, Relecture |
| **Validation**      | Vérifier une solution ou un raisonnement       | Curateur, relecteur          | Prompt piloté par les tests, Contre-exemple     |
| **Co-conception**   | Créer à plusieurs avec un LLM comme partenaire | Facilitateur, co-designer    | Miroir, Clarification, Synthèse, Exploration    |

> Ces situations ne sont ni exclusives ni rigides. Une même activité peut traverser plusieurs zones : on commence par explorer, on clarifie, on valide, on documente. C’est **un parcours, pas une case à cocher.**

---

### 🧭 Situation-type 1 — Exploration

> *Contexte :* un développeur fullstack découvre le pattern CQRS, qu’il n’a jamais utilisé.

**Posture** : explorateur, apprenant actif
**Prompt** :
« Explique-moi CQRS étape par étape, avec un exemple Node.js. »
**Motifs activés** :

* *Exploration guidée* : pour cadrer l’apprentissage par étapes
* *Contre-exemple* : pour mettre à l’épreuve la compréhension
* *Modèle miroir* : comparaison CQRS vs CRUD pour situer les usages

> Ici, le LLM devient un **tuteur patient et adaptable**, qui répond au rythme de la découverte.

---

### 🧭 Situation-type 2 — Cadrage flou

> *Contexte :* une équipe reçoit une demande métier très vague, avec des fragments d’intention mais aucune user story claire.

**Posture** : facilitateur, analyste
**Prompt** :
« Voici les éléments métier reçus. Peux-tu m’aider à formuler une user story complète avec des critères d’acceptation ? »
**Motifs activés** :

* *Question socratique* : pour affiner ce qui manque
* *Spécification inversée* : reconstituer des règles implicites
* *Reformulation visuelle ou par test* : pour stabiliser l’intention

> Dans ce type de situation, le LLM aide à **transformer du flou en structure**, à condition d’un guidage progressif.

---

### 🧭 Situation-type 3 — Refactorisation guidée

> *Contexte :* une fonction ancienne, non testée ni commentée, doit être réécrite sans en casser la logique.

**Posture** : critiqueur, nettoyeur
**Prompt** :
« Que fait ce code ? Propose une version plus lisible avec tests associés. »
**Motifs activés** :

* *Spécification inversée* : pour inférer la logique métier
* *Contre-exemple* : pour tester les limites ou bugs potentiels
* *Modèle miroir* : pour proposer plusieurs styles ou approches

> L’accent est ici sur la **rétro-ingénierie assistée** : comprendre avant de modifier.

---

### 🧭 Situation-type 4 — Co-conception

> *Contexte :* deux devs imaginent ensemble l’architecture d’un nouveau module, en dialogue avec un LLM.

**Posture** : facilitateur, co-concepteur
**Prompts enchaînés** :
« Quels sont les patterns possibles pour ce type de traitement ? » →
« Compare event-driven et pub/sub dans ce cas précis. » →
« Aide-nous à rédiger un plan d’implémentation en trois étapes. »
**Motifs activés** :

* *Exploration guidée*
* *Modèle miroir*
* *Clarification progressive*
* *Synthèse assistée*

> Le LLM agit ici comme **surface de pensée partagée**, soutenant un dialogue humain étendu.

---

### 🗺 Une carte vivante, pas une grille figée

Ce que cette typologie révèle, ce n’est pas une méthode, mais un **champ d’interactions possibles**. Elle peut devenir :

* un **outil réflexif individuel** : “Dans quelle situation suis-je ? Quel motif serait utile ?”
* un **cadre d’atelier collectif** : pour cartographier les usages de l’équipe et les enrichir
* un **levier d’apprentissage progressif** : en rendant visibles les zones encore peu explorées

Certaines équipes tiennent à jour leur propre **carte d’usage**, où elles relient tâches, prompts, motifs et rôles. C’est une manière de **documenter leur culture IA**, vivante, située, évolutive.

---

### 🧪 Cas d’équipe : trajectoire hybride

> *Contexte :* une startup développe un microservice d’authentification OAuth2.

Deux développeuses alternent les postures :

* **Exploration** : compréhension du protocole
* **Co-conception** : choix d’architecture
* **Documentation** : génération des guides internes
* **Validation** : test des cas limites via le LLM

Le LLM devient ici un **partenaire modulable** : il s’adapte au niveau de clarté, au moment du processus, à la posture humaine. L’équipe apprend à **orchestrer la conversation** autant qu’à produire du code.

---

### ✏️ En résumé

* Les **situations-types** sont des repères, pas des cases : elles aident à **s’orienter dans la pratique**.
* Les **postures et motifs** associés sont des leviers de progression, de réflexivité, d’apprentissage.
* **Cartographier ses usages**, seul ou en équipe, c’est une manière de **gagner en conscience, en fluidité, en maturité**.

> Ce que vous faites avec un LLM dépend moins de l’outil… que de votre intention, votre posture, et votre capacité à choisir le bon geste au bon moment.
> Comme dans tout art du dialogue.
