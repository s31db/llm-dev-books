
---
<a id="cadre"></a>
## 🔬 Chapitre 9 — Cadres de mise en œuvre : ateliers, méthodes et rituels pour une pratique augmentée

> Voici le terrain d’expérimentation : des formats pour apprendre ensemble, explorer, tester, documenter et transmettre les usages de l’IA dans vos équipes.

Après avoir exploré les motifs, les principes et les scénarios du développement augmenté, ce chapitre propose des **formats concrets** pour intégrer ces pratiques dans la réalité quotidienne des équipes. Ateliers, rituels, canevas, jeux sérieux : il s’agit de rendre tangibles les apports des LLM dans des dynamiques collectives, sécurisées et apprenantes.

---

### ✍️ 1. Atelier “Design de prompt en équipe”

> **Objectif :** Apprendre à formuler, reformuler et tester des prompts collectivement pour explorer un sujet réel et améliorer la qualité des interactions avec les LLM.

---

**🕒 Durée :** 1h30 à 2h

**👥 Participants :** 3 à 6 personnes (développeur·ses, PO, UX, QA, facilitateur·ice…)

**🧰 Matériel :** accès à un LLM, canevas de prompt (papier ou Miro), espace de visualisation des réponses

---

**🔁 Déroulé type**

#### Introduction et cadrage (10 min)

Présentation de l’objectif de l’atelier :
  *“Explorer collectivement comment mieux formuler nos prompts pour un cas concret.”*

Brève explication des postures attendues : ouverture, itération, non-jugement  

Choix collectif du sujet ou cas réel :

* découpage de module
* formulation d’un test
* choix technique
* reformulation d’un besoin utilisateur

---

#### Prompt initial (15 min)

Écriture d’un **premier prompt naïf**, ensemble : “Que demanderait-on à un LLM dans ce contexte ?”

<div class="pb-A4"></div>  

Lecture de la réponse générée

Identification des problèmes potentiels :

* flous, ambiguïtés, imprécisions
* termes trop techniques ou mal définis
 * intention implicite non dite

---

#### Itérations et reformulations (30 à 40 min)

Reformulation du prompt selon différents angles ou stratégies :

* rôle explicite (ex. “Tu es un architecte logiciel…”)
* pas à pas
* version structurée / bullet points
* version critique / exploratoire / générative

Pour chaque version :

* LLM génère une réponse
* Discussion rapide : en quoi est-elle différente ? plus utile ? biaisée ?

Si utile : comparaison directe de plusieurs formulations avec un même modèle.

---

#### Extraction d’un patron de prompt (15 à 20 min)

À partir des versions testées, formaliser ensemble un **patron de prompt réutilisable** :

* structure de base
* variantes ou modules facultatifs
* conditions d’usage
* erreurs à éviter

Documenter le tout dans un canevas ou bibliothèque de l’équipe.

---

#### Rétrospective et apprentissages (10 à 15 min)

Tour de table rapide :

* Ce que j’ai appris
* Ce que je réutiliserai demain
* Ce que j’aimerais encore tester

Décision éventuelle :

* publier une version nettoyée du prompt
* tester ce prompt sur d’autres cas similaires
* faire émerger un **motif d’interaction** à ajouter au pattern language

---

<div class="pb-A4"></div>

> **🧠 Résumé :**
>
> * Atelier structurant pour développer la capacité collective à bien formuler
> * Permet de comparer, critiquer et améliorer les interactions LLM
> * Génère des prompts utiles, réutilisables et adaptés à l’équipe

> ⚠️ **Pièges à éviter :**
>
> * Se focaliser sur une “bonne réponse” au lieu de tester des variations
> * Ne pas nommer les intentions cachées derrière un prompt
> * Laisser une seule personne écrire pendant que les autres observent


---

### 🗣️ 2. Rituel “Daily du dialogue”

> **Objectif :** Instaurer un rituel court, informel et régulier où chaque membre d’équipe partage ses interactions marquantes avec un LLM. Favorise l’apprentissage collectif, la vigilance et l’inspiration.

---

**🕒 Durée :** 5 à 10 minutes

**👥 Participants :** toute l’équipe (dev, PO, UX, QA, facilitateur·ice…)

**📆 Fréquence :** quotidienne ou bi-hebdomadaire (à adapter selon rythme et usages)

**🧰 Support (optionnel) :** mur des prompts, Slack dédié, tableau partagé

---

**🔁 Déroulé type (par séance)**

#### Introduction (1 min)

Petit mot d’ouverture (facilitateur·ice ou volontaire) :
  “Qu’est-ce que l’IA nous a appris aujourd’hui ?”

Rappel des **3 questions guides** (affichées ou rappelées) :

* **🧪 Qu’ai-je tenté avec un LLM ?**
* **😲 Qu’est-ce qui m’a surpris, aidé, déçu ?**
* **📌 Qu’est-ce que j’en retiens ou que je voudrais essayer ?**

---

#### Partages spontanés ou tournants (5 à 8 min)

Une à trois personnes partagent brièvement une interaction notable :

* succès ou échec
* prompt intéressant
* biais observé
* réponse étrange ou brillante
* usage détourné du LLM

Les autres peuvent rebondir, questionner ou ajouter une anecdote.

> 📍 *Si personne ne partage spontanément, tirer au sort un motif ou une carte “prompt du jour” pour inspirer.*

---

#### Clôture et captation (1 à 2 min)

L’équipe choisit un ou deux points à **retenir ou capitaliser** :

* Ajouter une carte au “grimoire des prompts”
* Noter une erreur fréquente ou une bonne pratique
* Proposer un test pour le prochain sprint

Mise à jour éventuelle du support partagé :

* Tableau de bord des expérimentations
* Fil Slack “#daily-llm”
* Carnet de bord Miro / Notion

---

> **🧠 Résumé :**
>
> * Rituel simple, léger, sans préparation
> * Fait émerger les usages réels, les pièges, les idées nouvelles
> * Alimente la capitalisation continue de l’équipe
> * Encourage une culture d’expérimentation et d’apprentissage horizontal

> ⚠️ **Pièges à éviter :**
>
> * Le transformer en stand-up statique ou en tour de table forcé
> * Dériver vers le jugement ou la compétition entre “bons prompts”
> * Ne pas connecter les apprentissages à l’action (tests, documentation, etc.)
> * Ne pas prévoir de lieu pour capitaliser les récits utiles

---

### 🗺️ 3. Atelier “Cartographie des motifs de dialogue”

> **Objectif :** Identifier les motifs d’interaction avec un LLM les plus utiles, fréquents ou désirables pour l’équipe, et en faire une base partagée pour orienter les usages futurs.

---

**🕒 Durée :** 1h30 à 2h

**👥 Participants :** 4 à 8 personnes (développeur·ses, PO, UX, test, facilitateur·ices…)

**🧰 Matériel :**

* Cartes ou fiches de motifs (issus du livre ou des pratiques locales)
* Tableau à double entrée (fréquence / utilité)
* Espace de collecte (Miro, paperboard, wiki…)

---

<div class="pb-A4"></div>

**🔁 Déroulé de l’atelier**

#### Introduction & cadrage (10 min)

Rappel de ce qu’est un **motif d’interaction LLM** : une forme récurrente d’usage avec intention, structure et effet.  
Pourquoi les cartographier ? *Pour mieux se repérer, s’inspirer, transmettre, progresser.*  
Présentation du support de cartographie : une matrice à double entrée *(axe X : fréquence d’usage ; axe Y : utilité perçue)*

---

#### Réactivation des motifs connus (15 min)

Lecture rapide ou présentation visuelle de 6 à 10 motifs existants.  
Pour chaque motif :

* L’équipe dit si elle le connaît
* Si elle l’a déjà utilisé, et dans quel contexte

**Exemples de motifs :**

Reformulation d’une idée floue  
Génération de cas de tests  
Exploration d’alternatives d’architecture  
Traduction d’un besoin métier en user story  
Explication pas à pas d’un comportement

---

#### Cartographie collective (30 min)

> Placer les motifs sur la matrice en deux temps

**Travail individuel ou binôme (10 min)**
   Chaque participant place les motifs sur la matrice selon :

* Fréquence dans son quotidien
* Utilité ressentie

**Discussion de groupe (20 min)**

* Confrontation des positions
* Consensus ou dispersion : où y a-t-il accord ou divergence ?
* Noter les questions ouvertes ou motifs sous-exploités

---

<div class="pb-A4"></div>

#### Génération de nouveaux motifs (20 min)

À partir des usages récents, ou de “trous” dans la matrice :

* Quels types d’interaction manquent à la cartographie ?
* Qu’avons-nous vu fonctionner sans encore le formaliser ?

Chaque participant ou sous-groupe esquisse un **nouveau motif** sur une fiche vierge :

* Intention
* Structure de prompt
* Exemples
* Limites ou pièges

---

#### Consolidation et capitalisation (15 min)

* Recueil de toutes les cartes/motifs sur un support commun (mur, board numérique)
* Proposition de tri ou regroupement par famille : *exploration*, *réduction*, *contrôle*, *création*, etc.
* Accord sur ce qui est à publier / partager / tester davantage

---

#### Bonus (optionnel)

* Donner un nom original à chaque motif (« Le pédagogue socratique », « Le contre-exemple malin », etc.)
* Voter pour les motifs à formaliser dans la bibliothèque de l’équipe ou le référentiel

---

> **🧠 Résumé :**
>
> * Crée une vue partagée des formes utiles de dialogue avec un LLM
> * Fait émerger les usages dominants… et les angles morts
> * Donne un point de départ pour des motifs à formaliser ou diffuser

> ⚠️ **Pièges à éviter :**
>
> * Ne parler que des motifs techniques (ou que fonctionnels)
> * Sous-estimer les postures (ex : curiosité, prudence, critique…)
> * Réduire la cartographie à un classement de “bons prompts”
> * Sous-estimer le besoin de reformuler collectivement

---

<div class="pb-A4"></div>

### 🎲 4. Le jeu des prompts absurdes

> **Objectif :** Expérimenter les limites, les paradoxes, les hallucinations et les biais des modèles de langage — avec humour et esprit critique.

---

**🕒 Durée :** 1h à 1h30

**👥 Participants :** 4 à 10 personnes

**🧰 Matériel :** Accès à un LLM, post-its ou tableau partagé, outil de capture (Miro, Notion, paperboard…)

---

**🔁 Déroulé type**

#### Introduction (10 min)

* Présenter l’objectif de l’atelier : *“Jouer avec les limites pour mieux les comprendre.”*
* Expliquer les règles : on crée des prompts absurdes, le LLM répond sérieusement, puis on analyse.
* Rappeler les postures attendues : bienveillance, curiosité, critique constructive, pas de moquerie des personnes.

---

#### Échauffement collectif (10 min)

* Chaque participant invente un **prompt absurde, contradictoire ou flou** (ex. : “Écris une poésie sur un langage de programmation qui n’existe pas mais qui a des bugs.”)
* Lecture à haute voix de quelques exemples.
* Le groupe choisit 2 ou 3 à soumettre au LLM pour lancer la dynamique.

---

#### Création et sélection des prompts (15 à 20 min)

Chaque personne écrit 2 prompts :

* un volontairement paradoxal ou fallacieux
* un inspiré d’une erreur ou mauvaise formulation déjà rencontrée

Mise en commun : les participants lisent leurs propositions à voix haute.

Le groupe sélectionne 3 à 5 prompts à tester, selon :

* leur potentiel de dérapage ou de surprise
* leur lien avec des situations professionnelles réalistes

---

<div class="pb-A4"></div>

#### Dialogue avec le LLM (20 à 30 min)

Soumettre les prompts un par un au LLM.  
À chaque réponse :

* Lecture collective
* Débrief guidé :

  * Qu’a tenté de faire le modèle ?  
  * Qu’est-ce que cela révèle de son fonctionnement ?  
  * Est-ce un bug ou une logique trop obéissante ?  
  * Quels risques si ce type de réponse était pris au sérieux ?

---

#### Synthèse collective (15 min)

En groupe ou en binômes : quels types d’erreurs avons-nous observé ?

* Hallucinations ?
* Réponses absurdes mais crédibles ?
* Obéissance aveugle à des ordres incohérents ?
* Manque de filtre éthique ou logique ?

Capitalisation sur un tableau partagé :

* « Ce que cela m’apprend sur les LLM »
* « Ce que cela m’apprend sur ma manière de formuler »

---

#### (Optionnel) Variante pédagogique

Créer une fiche “Erreur fictive mais plausible” :

* Prompt initial
* Réponse absurde
* Risque si pris au sérieux
* Bon réflexe de relecture ou reformulation


> **🧠 Résumé :**
>
> * Atelier ludique pour aiguiser son regard critique
> * Permet de discuter des failles des LLM sans pression
> * Crée une culture du doute et de la reformulation dans l’équipe

> ⚠️ **Pièges à éviter :**
>
> * Rire des erreurs des collègues au lieu d’analyser les formulations
> * Croire que ce jeu remplace une pratique sérieuse de test
> * Oublier d’en tirer des leçons applicables dans les contextes réels

---

<div class="pb-A4"></div>

### 📘 5. Référentiel d’équipe “LLM Ready”

> **Objectif :** Co-construire un guide d’usage du LLM adapté à l’équipe, fondé sur l’expérience, les besoins réels et les apprentissages collectifs.

---

**🕒 Durée :** 2h (fractionnable en 2 sessions d’1h)

**👥 Participants :** toute l’équipe ou un sous-groupe volontaire (4 à 8 personnes)

**🧰 Matériel :**

* Miro / paperboard ou mur physique
* Accès à un historique d’interactions LLM (si disponible)
* Modèle de référentiel (Notion, markdown, wiki…)

---

**🔁 Déroulé de l’atelier**

#### Introduction et objectifs (10 min)

Pourquoi faire un référentiel ? *Capitaliser, transmettre, sécuriser, gagner du temps*  
Rappel de la posture : ce n’est **pas une norme figée**, mais un **support évolutif**  
Présentation rapide des sections possibles : prompts types, règles, pièges, niveaux de validation…

---

#### Partage d’usages concrets (20 min)

> Quelles interactions LLM vous ont été vraiment utiles, ou au contraire problématiques ?

Chaque personne partage **1 à 2 exemples marquants** (réussites ou échecs)  
Écriture rapide en binôme ou post-its :

* Contexte
* Prompt
* Résultat
* Enseignement

Classement collectif en 3 colonnes :

* 🔁 À reproduire
* ⚠️ À adapter
* 🛑 À éviter

---

<div class="pb-A4"></div>

#### Construction du référentiel (45 min)

> Constitution des sections à partir des récits réels.

##### **Prompts types**

Extraire les formulations efficaces réutilisables  
Organiser par usage : rédaction, analyse de code, transformation, exploration…

##### **Critères de qualité des réponses**

Proposer une **grille commune** :

* Pertinence
* Robustesse
* Transparence
* Sécurité
* Cohérence avec les standards de l’équipe

##### **Règles d’usage**

Définir ensemble des règles claires et simples :

* Quand utiliser un LLM
* Quand valider avec un humain
* Quand documenter la réponse

##### **Liste noire / pièges fréquents**

Capitaliser les erreurs rencontrées : prompts flous, hallucinations crédibles, surconfiance, etc.

---

#### Mise en forme et diffusion (15 min)

Choix du format de publication : Notion, README, Miro, page Confluence…  
Attribution de rôles :

* 1 référent·e du vivant du référentiel
* 1 ou 2 gardiens de l’évolution (ex : sprint review, retro)

---

#### Rétrospective & engagement (10 min)

Tour de table :

* “Ce que j’ai appris”
* “Ce que je veux tester maintenant”
* “Ce que j’aimerais retrouver dans la prochaine version”

Rappel : un référentiel n’est **jamais terminé**, il est **en co-évolution** avec l’équipe.


> **🧠 Résumé :**
>
> * Atelier structurant pour stabiliser les bonnes pratiques IA dans l’équipe
> * Crée un référentiel utile, évolutif et approprié
> * Renforce la réflexivité collective et la qualité des usages

> ⚠️ **Pièges à éviter :**
>
> * Rédiger un référentiel “théorique” sans lien avec les usages réels
> * Le figer comme un standard rigide
> * Le laisser vieillir sans revue régulière (prévoir un rythme d’actualisation)

---

### Une ingénierie augmentée est aussi une ingénierie sociale

Ces formats montrent que le développement augmenté ne se résume pas à l’outillage. Il repose sur :

* une culture du dialogue (avec l’IA et entre humains),
* une capacité à expliciter nos raisonnements,
* une pratique réflexive qui transforme l’équipe autant que les livrables.

> 🧵 **À retenir :**
> Ce chapitre est une boîte à outils ouverte. Chaque format proposé peut être adapté, combiné, détourné. L’important n’est pas de les appliquer “à la lettre”, mais de s’en emparer pour créer vos propres chemins vers une pratique du code augmentée, collective et responsable.
