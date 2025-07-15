
---

## 🎓 Chapitre 11 — Usages de l’IA dans l’apprentissage

## L’IA comme tuteur et partenaire pédagogique

L’un des usages les plus immédiats des LLM est **l’auto-formation guidée**. Le développeur ou la développeuse peut interroger le modèle comme un mentor disponible à tout moment : pour demander une explication, une analogie, un exemple de code, ou une reformulation.

> **Exemple :**
> – *« Peux-tu m’expliquer les closures en JavaScript comme si j’avais 12 ans ? »*
> – *« Montre-moi trois variantes de cette fonction, du plus simple au plus optimisé. »*

Cela permet à chacun·e d’apprendre à son rythme, de combler des lacunes rapidement, et de mieux consolider ses connaissances. Le LLM devient alors un **compagnon d’apprentissage** permanent, personnalisable et sans jugement.

De nombreuses équipes encouragent déjà cet usage comme un réflexe naturel : ne pas rester bloqué·e, mais “demander à l’IA” avant de déranger un collègue — ou au contraire, pour préparer un échange plus ciblé.

---

### 2. Génération assistée de documentation

La production de documentation est souvent négligée ou reportée. Avec l’IA, il devient possible de la générer **de manière incrémentale et contextuelle**, à partir :

* de la lecture d’un fichier source ;
* d’un historique de commits ou de tickets ;
* d’un échange de chat technique ;
* d’une démonstration enregistrée.

> **Exemples :**
> – Générer automatiquement des docstrings à partir du code.
> – Proposer un résumé technique d’un module ou d’un ticket.
> – Synthétiser un document Markdown à partir d’un échange Slack ou Notion.

Ce type de documentation “sur demande” réduit la friction cognitive, et permet une mise à jour plus régulière. Il devient aussi plus facile de partager cette documentation avec des profils non techniques (PO, UX, métiers…).

---

### 3. Prompts comme artefacts à versionner

Un des concepts les plus innovants dans ce nouveau paradigme est celui de **prompt comme artefact documentaire**. Autrement dit : un prompt bien formulé peut devenir une *ressource à part entière*, au même titre qu’un test unitaire ou qu’un ticket Jira.

> **Exemple :**
> Un prompt utilisé pour générer un plan de test automatisé ou un gabarit de composant peut être stocké, versionné, relu, partagé, adapté à d’autres projets.

Cela implique :

* de conserver une trace des prompts importants (dans Git, dans un wiki, dans une base de prompts) ;
* d’y associer leur contexte (besoin, objectif, contraintes) ;
* de relire ces prompts collectivement (comme une revue de code).

Certains outils émergent déjà autour de cette idée : *prompt repositories*, *prompt templates*, *prompt linters*, etc. Cela crée une culture de **transparence et de partage de la pensée design**, là où beaucoup de décisions étaient auparavant implicites.

---

### 4. Ateliers d’équipe, learning loops et coaching augmenté

L’IA peut aussi enrichir les dynamiques d’équipe, en nourrissant des **rituels collectifs d’apprentissage**. Voici quelques formats efficaces :

#### Atelier “Prompt Clinic”

Chaque membre apporte un prompt qu’il ou elle a utilisé, et l’équipe discute de :

* sa clarté ;
* sa robustesse ;
* les résultats obtenus ;
* les possibilités d’amélioration.

Cela permet de partager des pratiques de formulation et de cultiver une posture réflexive.

#### Learning Loop augmentée

Une mini-boucle d’apprentissage guidée par IA, par exemple :

1. Formulation d’un besoin flou.
2. Première réponse IA.
3. Reformulation humaine.
4. Affinement IA.
5. Documentation du processus.

L’équipe en tire un enseignement formel (nouveau motif, décision d’architecture, exemple à conserver).

#### Coaching augmenté

Les coachs techniques ou agiles peuvent s’appuyer sur l’IA pour :

* reformuler des points techniques pendant les revues ;
* proposer des ressources adaptées aux profils juniors ;
* modéliser différentes stratégies de résolution d’un même problème.

Cela favorise une montée en compétences rapide, sans alourdir la charge humaine de transmission.

> **Prompt Book : un nouveau type de livrable**
> 
>De plus en plus d’équipes documentent leurs pratiques LLM dans un “*prompt book*” ou “*carnet de design dialogué*” : une collection structurée de prompts testés, commentés, adaptés à leur contexte métier. Ce format devient un **patrimoine collectif**, précieux pour l’onboarding, la mémoire projet, et la montée en compétence.