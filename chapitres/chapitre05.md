
---

## Chapitre 5 — Cartographier les usages : typologie des interactions LLM-développeur

Dans ce chapitre, nous proposons une lecture transversale des motifs précédemment présentés en les reliant à des **situations-types** que rencontrent les développeurs dans leur quotidien. Il ne s’agit plus uniquement de parler en termes de « patterns » abstraits, mais de comprendre **quand et pourquoi** tel ou tel motif s’active, en fonction de l’intention du moment, du contexte de travail, ou encore du niveau de maturité de l’utilisateur avec les LLM.

Nous allons ainsi esquisser une **cartographie des usages** qui aide à naviguer dans les interactions avec les modèles de langage. Cette typologie offre aux équipes une meilleure lecture de leurs pratiques et permet aux formateurs, coaches et tech leads d’identifier les compétences associées à chaque posture.

### 1. L’explorateur 🧭 — Interagir pour comprendre un domaine

> **Objectif :** recueillir des informations, structurer une compréhension initiale, identifier des angles d’approche.

L’explorateur formule des questions larges, cherche à définir un périmètre, à obtenir une vue d’ensemble d’un sujet. Il active souvent les motifs « Question Socratique » ou « Reformulation Itérative ». Ce type d’interaction est fréquent en début de projet, en phase de cadrage ou lors de l’arrivée sur un domaine inconnu (nouvelle techno, architecture existante à auditer, etc.).

**Exemple** : « Quels sont les principaux types de base de données NoSQL et dans quels cas les utiliser ? »

---

### 2. Le praticien opérationnel 🛠️ — Résoudre un problème concret

> **Objectif :** générer ou corriger du code, automatiser une tâche, proposer une implémentation.

Cette posture est la plus répandue. L’utilisateur cherche une solution immédiate à un blocage technique, une aide à l’écriture, ou un gain de temps. Il utilise souvent les motifs « Co-écriture par reformulation », « Contre-exemple » ou « Prompt Contexte + Tâche ».

**Exemple** : « Génère une fonction Python qui détecte les doublons dans une liste de dictionnaires. »

---

### 3. Le concepteur structurant 🧱 — Faire émerger une architecture ou un design

> **Objectif :** co-construire une vision technique cohérente à partir d’éléments épars.

Ici, le LLM est utilisé comme partenaire de réflexion. Le développeur ne cherche pas une solution, mais une structure, une articulation d’idées. Cela implique un travail en itérations, avec évaluation d’alternatives, scénarios, et documentation. Les motifs « Design Dialogué », « Exploration Parallèle » ou « Hiérarchie Intentionnelle » (chapitres suivants) y sont fréquents.

**Exemple** : « Quels modèles d’architecture sont adaptés à une application de messagerie sécurisée en temps réel ? »

---

### 4. Le pédagogue réflexif 👨‍🏫 — Se former ou former à travers le dialogue

> **Objectif :** utiliser le LLM comme outil d’apprentissage, de transmission ou de formalisation.

Ce profil s’adresse souvent aux enseignants, mentors, ou aux développeurs en formation. Le LLM est utilisé pour expliquer, reformuler, illustrer, simuler des erreurs. Les motifs comme « Question Socratique », « Cas Limite », ou « Décomposition Progressive » sont ici clés.

**Exemple** : « Explique-moi pourquoi le mot-clé `await` est obligatoire dans une boucle for async en JavaScript. »

---

> 🗺️ **Carte synthétique à venir : correspondance motifs ↔ postures ↔ situations**

Cette cartographie permet d’identifier la pluralité des approches et de mieux comprendre que les LLM ne sont pas simplement des outils « génériques », mais des partenaires capables d’adapter leur réponse à la posture intellectuelle de l’utilisateur. Il devient alors possible de développer une véritable **intelligence d’usage**, c’est-à-dire une capacité à activer le bon levier au bon moment.
