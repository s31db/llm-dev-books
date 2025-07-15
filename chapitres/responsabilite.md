
---

## ⚖️ Chapitre 7 — Responsabilité, transparence et limites : une éthique du développement augmenté

> Utiliser un LLM dans le développement, ce n’est pas seulement une opportunité. C’est aussi une responsabilité.
> Il ne suffit pas que le résultat fonctionne. Il faut **pouvoir expliquer comment il a été produit, et à quelles conditions**.

---

## 🧭 Pourquoi ce chapitre ?

Dans un contexte où :

* des outils proposent du code sans auteur clair,
* des équipes intègrent des blocs générés sans les comprendre,
* des décisions d’architecture sont prises à l’aide de suggestions IA,

la **documentation des interactions avec les LLM** devient un enjeu majeur. Non pas pour tout consigner… mais pour **rendre visible ce qui a été généré, validé, interprété**.

---

## 📘 Partie 1 — Documenter l’usage des LLM

### 1.1 Pourquoi documenter ?

* Pour garder une trace des choix faits avec l’aide de l’IA.
* Pour éviter la **dette générative** : du code produit trop vite, sans explication.
* Pour pouvoir réexaminer un raisonnement ou un prompt dans six mois.
* Pour outiller les relecteurs et les équipes QA.

> La documentation d’un prompt n’est pas un luxe. C’est **une condition de la maintenabilité.**

---

### 1.2 Que documenter ?

| Élément                         | Objectif                                                      |
| ------------------------------- | ------------------------------------------------------------- |
| **Prompt source**               | Comprendre l’intention initiale                               |
| **Version du LLM utilisé**      | Évaluer les limites, biais ou hallucinations potentielles     |
| **Réponse générée**             | Historiser l’itération utilisée                               |
| **Validation humaine apportée** | Identifier le rôle de l’humain dans l’acceptation du résultat |
| **Hypothèses contextuelles**    | Préserver la logique derrière la génération                   |

---

### 1.3 Formats possibles

* Annotation en commentaire dans le code
* Historique dans l’outil LLM (chat, snapshot, fichier `.prompt.md`)
* Documentation à part (Wiki, PR, fichier `prompts/`)
* Modèle structuré (ex. Fiche Prompt + Tests d’intention associés)

---

### 1.4 Exemple concret

```js
// Fonction générée à partir d’un prompt GPT-4 le 12/04/2025
// Prompt : “Écris une fonction en JavaScript qui valide une adresse mail avec une RegExp simple”
// Réponse modifiée pour :
  // - Ajouter la gestion des caractères spéciaux
  // - Remplacer l'alerte par une exception explicite
```

---

## ⚖️ Partie 2 — Enjeux éthiques et responsabilité

### 2.1 LLM = responsabilité partagée

> Ce n’est pas parce qu’un LLM a proposé un code que vous en êtes moins responsable.
> Vous êtes responsable **de ce que vous comprenez, validez, intégrez**.

Les modèles sont puissants, mais :

* ne donnent aucune garantie de fiabilité,
* peuvent reproduire des biais,
* peuvent générer du contenu non conforme ou juridiquement risqué,
* ne sont pas capables de refuser une tâche inappropriée par eux-mêmes.

> **Un bug venu d’un exemple convaincant**
>
> Un développeur a récemment intégré un snippet de code généré par LLM pour l’authentification OAuth. Le code était syntaxiquement parfait, commenté, et semblait sécurisé… sauf qu’il utilisait une bibliothèque obsolète et vulnérable. L’audit de sécurité a révélé une faille critique. Le LLM avait simplement “recopié” un exemple daté, sans signaler de mise en garde. Résultat : plusieurs jours perdus, et une prise de conscience utile.

---

### 2.2 Risques fréquents

| Risque                        | Exemple                                                                  |
|-------------------------------|--------------------------------------------------------------------------|
| **Hallucination de fonction** | Fonction plausible mais non existante dans un langage donné              |
| **Copie involontaire**        | Reproduction d’un bout de code protégé issu du corpus d’entraînement     |
| **Biais implicite**           | Stéréotypes dans les exemples ou réponses générées                       |
| **Surconfiance**              | Prise de décision sans relecture ni test, sur la base d’un prompt unique |
| **Manque de traçabilité**     | Code généré sans indication de son origine ni de sa validation           |

---

### 2.3 Questions à se poser (checklist éthique)

1. Ai-je compris ce que le modèle a produit ?
2. Puis-je expliquer à quelqu’un pourquoi cette solution est valable ?
3. Ai-je testé ou vérifié ce code ?
4. Ai-je signalé qu’il a été généré ?
5. Le modèle a-t-il produit une réponse biaisée ou discutable ?
6. Cette interaction pourrait-elle être mal interprétée ou mal réutilisée par quelqu’un d’autre ?
7. Est-ce que j’assumerais cette décision en production ?

> Si la réponse est “non” à deux questions ou plus, il est **trop tôt pour valider cette contribution IA.**

---

## 🔍 Vers une culture de la transparence

* Rendre visible l’usage des LLM n’est pas une contrainte. C’est **un levier de confiance collective.**
* Cela permet de relire, de corriger, de transmettre.
* Cela constitue une **preuve de diligence technique** en cas de litige ou d’incident.
* Cela alimente une culture d’équipe où l’IA **stimule le raisonnement plutôt qu’elle ne le remplace**.

---

> **Le “Journal du dialogue”**
>
> Dans une startup du secteur santé, chaque interaction avec un LLM pour des sujets critiques (protocoles, anonymisation, sécurité) est archivée sous forme de journal. Ce journal inclut : prompt initial, itérations, choix retenus, évaluation humaine, et justification des décisions. Ce dispositif améliore la transparence interne, facilite les audits, et cultive une posture réflexive.

---


## 🔐 Protéger les données, même dans le dialogue

> *Tout ce que vous envoyez à un LLM n’est pas neutre — ni invisible.*

Les interactions avec un LLM peuvent exposer involontairement des données sensibles, confidentielles ou personnelles : noms de clients, extraits de code propriétaire, exemples de production, ou encore décisions stratégiques.

Même lorsque l’outil semble local ou « sécurisé », il est essentiel d’adopter une posture de prudence active :

* **Filtrer en amont** les données transmises, comme on le ferait pour une publication publique.
* **Éviter les copier-coller aveugles** issus de documents confidentiels ou de bases internes.
* **Utiliser des environnements contrôlés**, capables de garantir la non-exploitation des données (LLM auto-hébergés, mode entreprise, clauses contractuelles explicites).
* **Anonymiser les données** utilisées dans les prompts, dès que possible.
* **Former les équipes** aux risques liés à la fuite involontaire d’information via un prompt mal formulé.

Enfin, se poser une question simple avant chaque envoi :

> *“Aurais-je le droit d’envoyer ceci par email à une tierce personne extérieure à mon organisation ?”*
> Si la réponse est non, alors le prompt doit être retravaillé.

Ce souci de **protection des données** s’inscrit dans une éthique plus large : celle d’un développement **responsable, traçable et conscient de ses impacts** — techniques, sociaux et légaux.

## ✏️ En résumé

* La documentation des prompts et des interactions est une **bonne pratique technique** et un **geste éthique.**
* Les LLM déplacent la responsabilité, mais ne la dissolvent pas.
* Seule une **pratique transparente et partagée** peut garantir la qualité, la robustesse et l’éthique des conceptions assistées par IA.

> Les LLM ne pensent pas. Ils complètent.
> Mais vous, vous **pensez avec eux** — et cela vous engage.
