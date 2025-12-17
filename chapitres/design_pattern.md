
---
<a id="design_pattern"></a>
## 🏠 Chapitre 15 — Repenser les design patterns à l’ère des LLM

> *Et si les patterns devenaient des dialogues vivants plutôt que des recettes figées ?*

---

### 🤝 Pourquoi ce chapitre ?

Les *design patterns* ont longtemps été des repères pour les développeur·ses. Mais leur apprentissage reste souvent théorique, figé, difficile à contextualiser. Et si les LLM permettaient de transformer ces savoirs abstraits en dialogues pratiques ?

Ce chapitre propose une nouvelle manière d'explorer les patterns, non comme des solutions imposées, mais comme des points d'appui pour dialoguer avec une IA, tester des idées, clarifier une architecture, et documenter les choix collectifs.

---

### 📈 Les patterns classiques : force, limite, défi

Les *design patterns* (GoF, GRASP, DDD, EIP...) apportent un vocabulaire commun. Mais dans la pratique :

* ils sont souvent appris sans lien au contexte,
* leur mise en œuvre est jugée verbeuse ou prématurée,
* ils vieillissent mal dans un code qui évolue.

Les LLM permettent de :

* **générer des variantes** contextuelles,
* **détecter** leur présence ou absence dans un code,
* **argumenter** un choix de pattern,
* **illustrer** de manière dynamique leur effet.

---

### 🖊️ Patterns classiques revisites avec l’IA

#### ✨ Le pattern “Strategy”

**But** : encapsuler des algorithmes interchangeables.

**Prompt augmenté** :

> "Voici trois façons de calculer un score utilisateur. Propose une structure qui permet de les sélectionner dynamiquement selon le contexte, et explique ton choix."

**Apports du LLM** :

* propose une implémentation basee sur des interfaces,
* identifie les critères de choix entre stratégies,
* peut simuler un test A/B par contexte.

**Attention** : peut proposer une généricité excessive si les données contextuelles ne sont pas explicites.

---

#### ✨ Le pattern “Observer”

**But** : notifie des composants dépendants lorsqu’un événement se produit.

**Prompt augmenté** :

> "Je veux que mon module envoie une notification chaque fois que l'état change, mais je ne veux pas coupler les modules. Quel pattern s’applique ?"

**Réponse typique d’un LLM** :

* décrit le pattern observer,
* génère une implémentation en TypeScript ou Python,
* propose une alternative via des événements / pub-sub.

**Bénéfice** : l’IA peut présenter plusieurs formes du pattern, et attirer l’attention sur le couplage indirect créé.

---

#### ✨ Le pattern “Factory”

**But** : déléguer la création d’objets à une fonction/fabrique.

**Prompt augmenté** :

> "J'ai plusieurs implémentations d'un service selon l'environnement (prod, test, mock). Propose un design testable et extensible."

**Dialogue possible** :

* l'IA propose un Factory ou Service Locator,
* suggère une injection de dépendance,
* met en garde contre le pattern Singleton abusif.

**→ Réflexion induite** : quel est le degré de configurabilité nécessaire ? quel impact sur les tests ?

---

<div class="pb-A4"></div>

#### ✨ Le pattern “Decorator”

**But** : ajouter dynamiquement des comportements à un objet.

**Prompt augmenté** :

> "J'ai un service de logging, mais je veux y ajouter des fonctionnalités optionnelles (ex. : mise en cache, métriques) sans modifier le code existant."

**Apports du LLM** :

* identifie le pattern Decorator,
* propose une version chaînée des responsabilités,
* illustre la combinaison possible des comportements.

**Attention** : risque de chaîne de dépendance difficile à maintenir si les comportements sont trop imbriqués.

---

#### ✨ Le pattern “Command”

**But** : encapsuler une action sous forme d’objet.

**Prompt augmenté** :

> "Je veux pouvoir annuler ou replanifier certaines opérations utilisateur. Quelle structure adopter ?"

**Dialogue possible** :

* le LLM identifie Command,
* propose une interface `execute()` / `undo()` / `redo()`,
* peut suggérer des mémoires tampon ou files d'attente.

**Effet intéressant** : aide à penser en termes d'état réversible.

---

#### ✨ Le pattern “Adapter”

**But** : faire correspondre une interface attendue avec une implémentation existante.

**Prompt augmenté** :

> "J'ai une API externe avec des noms différents des miens. Comment l’intégrer sans toucher au code client ?"

**Ce que propose le LLM** :

* interface d'adaptation simple,
* mise en garde sur les coûts de transformation ou de latence,
* alternative avec un mapping via une couche d'orchestration.

**Bénéfice** : rapide à déployer, bonne capacité à tester.

---

#### ✨ Le pattern “Proxy”

**But** : contrôler l'accès à un objet (paresse, sécurité, journalisation).

**Prompt augmenté** :

> "Je veux protéger l'accès à une ressource distante avec des logs et de la mémorisation. Quelle structure proposer ?"

**Ce que propose le LLM** :

* identifie Proxy (avec variantes : virtual, remote, protective),
* décrit les cas d'usage typiques,
* propose une implémentation avec injection du sujet réel.

**Effet clé** : rend visibles les intentions de contrôle d'accès et de métriques.

---

#### ✨ Le pattern “Composite”

**But** : permettre de traiter une hiérarchie d’objets comme une seule entité.

**Prompt augmenté** :

> "Je veux appliquer la même opération à un groupe d'éléments, certains étant eux-mêmes des groupes."

**Dialogue IA** :

* propose le pattern Composite,
* structure un exemple arborescent,
* explique les bénéfices en termes de récursivité et polymorphisme.

**Bénéfice** : permet de simuler des comportements complexes avec une interface unifiée.

---

#### ✨ Le pattern “Builder”

**But** : construire progressivement des objets complexes.

**Prompt augmenté** :

> "J'ai un objet avec beaucoup de paramètres optionnels, comment le construire sans avoir un constructeur illisible ?"

**Apports du LLM** :

* propose un Builder fluent,
* montre comment éviter les erreurs de configuration,
* propose une version immuable.

**Mise en garde** : attention à la multiplication des classes inutiles.

---

<div class="pb-paper"></div>

#### ✨ Le pattern “Event Sourcing”

**But** : conserver l’historique complet des changements d’état sous forme d’événements.

**Prompt augmenté** :

> "Je veux pouvoir rejouer l’historique des décisions métier et auditer l’évolution d’un objet dans le temps."

**Dialogue IA** :

* propose Event Sourcing,
* explicite la séparation `Command`, `Event`, `Projection`,
* met en garde sur la gestion de version des événements.

**Effet clé** : fiabilité, auditabilité, mais nécessite une culture d’équipe.

---

#### ✨ Le pattern “CQRS” (Command Query Responsibility Segregation)

**But** : séparer les modèles de lecture et d’écriture pour optimiser chacun.

**Prompt augmenté** :

> "Je veux un système capable de répondre très vite aux lectures, tout en conservant une logique métier robuste à l’écriture."

**Ce que le LLM propose** :

* structure `CommandHandler`, `QueryModel`, `ReadStore`,
* identifie les cas propices : systèmes hautement lisibles, scalables,
* met en garde sur la complexité accrue.

**Utilité** : très clair pour les LLM, qui peuvent simuler les échanges de commandes et états.

---

<div class="pb-A4"></div>

#### ✨ Le pattern “Circuit Breaker”

**But** : éviter qu’un système défaillant ne surcharge le reste de l’application.

**Prompt augmenté** :

> "Comment isoler un service instable sans impacter tout le système ?"

**Réponse LLM** :

* propose Circuit Breaker avec états (`Closed`, `Open`, `Half-Open`),
* montre son intégration avec des appels HTTP,
* peut même générer des métriques de seuils configurables.

**Bénéfice** : les LLM aident à tester des seuils, des scénarios de fallback, voire à jouer un chaos engineering assisté.

---

<div class="pb-paper"></div>

### 🎮 Nouveaux motifs de dialogue architectural

| Motif | Intention | Prompt-type | Risque |
|-------|-----------|-------------|--------|
| Comparaison | Choisir un pattern parmi plusieurs | "Compare Factory, Builder et AbstractFactory pour ce besoin" | Biais vers une solution par défaut |
| Refactoring guidé | Repenser un bloc de code avec un pattern            | "Refactore ce module avec le pattern stratégie"              | Erreur de contexte                 |
| Diagnostic        | Détecter un anti-pattern ou un problème de structure | "Vois-tu un God Object ici ?"                                | Faux positifs                      |
| Argumentation     | Expliquer un choix architectural                    | "Pourquoi utiliser CQRS ici plutôt que CRUD ?"               | Hallucination d’avantages          |
| Synthèse          | Comparer deux structures côte à côte                | "Compare ces deux modèles pour ce besoin fonctionnel"        | Comparaison superficielle          |

---

### 🎓 Atelier : le dilemme architectural augmenté

#### Objectif :

S’entraîner à faire dialoguer architecture humaine et IA dans un cadre collectif.

<div class="pb-paper"></div>

#### Déroulé :

1. Une situation complexe est posée (ex : conception d’un module de paiement).
2. Chaque binôme humain+LLM propose une structure + justification.
3. Comparaison croisee, puis vote argumenté.
4. Élaboration collective d’une version hybride avec les meilleures idées.

#### Bénéfices :

* expose la diversité des chemins,
* invite à questionner les implicites,
* ancre les patterns dans un raisonnement réel.

---

### 🕵️ Vigilances

* **Ne pas idolâtrer le pattern** : un LLM peut surestimer leur utilité.
* **Documenter le choix** : pourquoi ce pattern ici, et pas un autre ?
* **Valider humainement** : tout pattern est une décision collective, pas une réponse automatique.

---

### 🌐 En résumé

Les *design patterns* sont de formidables outils d’architecture. Mais ils deviennent vivants quand ils servent de support à un **dialogue augmenté**, entre humains, et avec l’IA.

> “Un pattern bien utilisé est une conversation entre contexte, intention et conséquence.”

Avec les LLM, nous pouvons apprendre à documenter ces conversations, les enrichir, les tester... et parfois, les contredire.
