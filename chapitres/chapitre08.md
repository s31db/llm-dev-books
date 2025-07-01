
---

## Chapitre 8 — Responsabilité, transparence et limites : une éthique du développement augmenté

Le recours aux LLM dans le développement logiciel ne pose pas uniquement des questions de productivité ou d’efficacité. Il soulève aussi des enjeux éthiques profonds : qui est responsable du code généré ? Comment éviter les biais ? Que faire lorsqu’un modèle propose une solution trompeuse, non sécurisée ou inadaptée ? Ce chapitre aborde la dimension éthique de cette co-construction avec des intelligences statistiques, pour une pratique plus consciente et plus responsable.

### La tentation de la délégation

La qualité apparente des réponses générées par les LLM peut créer une illusion de maîtrise ou d'autorité. Pourtant :

* Les modèles n'ont **ni compréhension réelle** ni conscience du contexte métier ou humain.
* Ils peuvent générer des réponses fausses avec une grande assurance linguistique.
* Ils sont **sensibles aux biais présents dans leurs données d'entraînement**, souvent invisibles à l'œil nu.

> **Encadré : Un bug venu d’un exemple convaincant**
>
> Un développeur a récemment intégré un snippet de code généré par LLM pour l’authentification OAuth. Le code était syntaxiquement parfait, commenté, et semblait sécurisé… sauf qu’il utilisait une bibliothèque obsolète et vulnérable. L’audit de sécurité a révélé une faille critique. Le LLM avait simplement “recopié” un exemple daté, sans signaler de mise en garde. Résultat : plusieurs jours perdus, et une prise de conscience utile.

### Qui est responsable ?

Face à ce genre de situation, plusieurs questions deviennent centrales :

* Le développeur qui copie-colle un code généré sans le tester est-il responsable ?
* L’équipe doit-elle tracer les morceaux de code issus d’une IA ?
* Peut-on considérer un LLM comme une source de documentation ou comme un contributeur anonyme ?
* Que deviennent les exigences de conformité réglementaire (ex. : RGPD, cybersécurité, accessibilité) dans un monde de suggestions automatiques ?

Une approche responsable repose sur **l’explicitation des intentions, des choix et des arbitrages humains** à chaque étape. L’IA est un outil, pas un auteur.

### Des pratiques pour une éthique active

Voici quelques pratiques émergentes pour renforcer l’éthique dans les usages :

* **Tracer l’origine des suggestions IA** dans les revues de code ou les commit messages.
* **Demander systématiquement des justifications** aux réponses générées : “Pourquoi cette solution plutôt qu’une autre ?”
* **Inclure des tests, validations ou relectures humaines** pour tout code ou contenu produit par IA.
* **Favoriser la diversité des points de vue** en confrontant les propositions IA à celles de l’équipe.
* **Documenter les prompts sensibles** ou ayant un impact critique (sécurité, données, logique métier complexe).

> **Encadré : Le “Journal du dialogue”**
>
> Dans une startup du secteur santé, chaque interaction avec un LLM pour des sujets critiques (protocoles, anonymisation, sécurité) est archivée sous forme de journal. Ce journal inclut : prompt initial, itérations, choix retenus, évaluation humaine, et justification des décisions. Ce dispositif améliore la transparence interne, facilite les audits, et cultive une posture réflexive.

### Les limites des LLM : mieux les connaître pour mieux les utiliser

Il est essentiel de garder à l’esprit certaines limites structurelles des modèles de langage actuels :

* **Ils ne raisonnent pas** : ils extrapolent des séquences probables.
* **Ils n’ont pas de mémoire de long terme** sans l’ajout explicite de contexte.
* **Ils peuvent halluciner** (inventions crédibles mais fausses), notamment dans les domaines techniques pointus.
* **Ils sont sensibles à la formulation** : un même problème mal posé peut produire une réponse erronée ou biaisée.

Connaître ces limites n’est pas un obstacle, mais une condition pour construire une relation saine et maîtrisée avec l’IA.
