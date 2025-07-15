
---

## 🗺️ Chapitre 5 — Cartographier les usages : typologie des situations et des rôles

> Concevoir avec un LLM, ce n’est pas appliquer une méthode linéaire. C’est **naviguer dans un espace d’interactions possibles**, qui varie selon le contexte, l’intention, le niveau de maturité. Ce chapitre propose une **carte de ces usages**.

---

### 🧭 Pourquoi ce chapitre ?

Nous avons exploré :

* des **motifs conversationnels** (Chapitre 3),
* les **postures et rôles** qui émergent (Chapitre 4).

Il est temps maintenant de **cartographier les situations** dans lesquelles ces éléments s’activent. L’objectif : aider chacun à **reconnaître où il se trouve** dans la pratique, et à choisir les motifs ou postures les plus adaptés.

---

## 🧩 Typologie des situations

Nous proposons ici six situations-types, fréquentes dans le travail logiciel augmenté par les LLM.

| Situation           | Intention principale                           | Rôle/posture activé(e)       | Motifs typiques                             |
| ------------------- | ---------------------------------------------- | ---------------------------- | ------------------------------------------- |
| **Exploration**     | Découvrir un domaine, une techno, une approche | Explorateur                  | Exploration guidée, Miroir                  |
| **Cadrage**         | Clarifier un besoin flou ou implicite          | Formulateur, facilitateur    | Question socratique, Décomposition          |
| **Refactorisation** | Améliorer un existant                          | Analyste, critiqueur         | Spécification inversée, Contre-exemple      |
| **Documentation**   | Générer ou reconstruire du sens                | Synthétiseur, documentaliste | Spécification inversée, Résumé ciblé        |
| **Validation**      | Vérifier une solution, tester un raisonnement  | Curateur, relecteur          | Prompt piloté par les tests, Contre-exemple |
| **Co-conception**   | Créer à plusieurs avec un LLM comme partenaire | Facilitateur, co-concepteur  | Miroir, Clarification, Synthèse             |

---

## 🧭 Exemple 1 — Situation “Exploration”

> **Contexte** : un développeur fullstack découvre le pattern CQRS.

**Posture** : explorateur, apprenant actif
**Prompt** : « Explique-moi CQRS étape par étape, avec un exemple Node.js. »
**Motifs activés** :

* *Exploration guidée* (pour la découverte)
* *Contre-exemple* (pour tester la compréhension)
* *Miroir* (CQRS vs CRUD)

---

## 🧭 Exemple 2 — Situation “Cadrage flou”

> **Contexte** : une équipe reçoit une demande métier mal formalisée.

**Posture** : facilitateur, analyste
**Prompt** : « Voici les éléments métier reçus. Peux-tu aider à formaliser une user story complète avec critères d’acceptation ? »
**Motifs activés** :

* *Question socratique*
* *Spécification inversée*
* *Reformulation par test*

---

## 🧭 Exemple 3 — Situation “Refactorisation guidée”

> **Contexte** : un dev reprend une fonction critique non testée ni commentée.

**Posture** : critiqueur, nettoyeur
**Prompt** : « Que fait ce code ? Quelle serait une version plus claire, avec tests associés ? »
**Motifs activés** :

* *Spécification inversée*
* *Contre-exemple*
* *Miroir de style*

---

## 🗺 Vers une carte d’usage dynamique

On peut imaginer cette cartographie comme une **matrice vivante**, dans laquelle :

* Chaque **situation** active une combinaison de postures et de motifs.
* Ces combinaisons peuvent **évoluer avec l’expérience**.
* Certaines équipes documentent leurs propres cartes d’usage (quels motifs pour quelles tâches ?), pour **faciliter l’onboarding ou les revues**.

---

## 🧪 Cas d’équipe : usages hybrides

Dans une startup, deux développeuses utilisent un LLM pour concevoir un microservice d’authentification. Elles alternent :

* **Exploration** de l’approche OAuth2
* **Co-conception** d’un middleware
* **Documentation** des choix
* **Validation** par génération de tests

Elles changent de posture selon l’étape. Le LLM devient une **surface partagée** de réflexion.

---

## ✏️ En résumé

* Les situations-types offrent un **repère pratique** pour mobiliser les bons motifs.
* Les rôles et postures ne sont pas figés : on **circule entre eux selon le moment.**
* Cartographier ses usages, c’est aussi **prendre conscience de sa maturité d’interaction.**

> Ce que vous faites avec un LLM dépend moins de l’outil… que de votre intention, votre posture, et votre capacité à choisir le bon motif au bon moment.

