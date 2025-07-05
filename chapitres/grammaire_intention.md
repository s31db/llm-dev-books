
---

## Chapitre — La grammaire de l’intention : penser et formuler avec un LLM

> Au-delà des bons mots, c’est la qualité du dialogue qui compte. Ce chapitre vous propose une nouvelle grammaire pour interagir avec un LLM comme avec un partenaire de conception.

Avant même de parler de prompts ou d’outils, il nous faut revenir à la nature même de la collaboration entre humain et LLM. À quoi ressemble une bonne interaction ? Comment reconnaître une dérive, une ambiguïté, une impasse ? Comment transformer une simple commande en un véritable dialogue productif ?

Un LLM ne pense pas. Il infère, il complète, il modélise des suites probables de mots. Ce fonctionnement statistique peut générer des perles… ou des absurdités. Le rôle de l’humain devient alors celui d’un médiateur du sens : il guide, corrige, affine, reformule. Ce rôle est loin d’être passif. Il implique une écoute attentive, une capacité à reformuler des attentes, une exigence dans la précision des formulations et une vigilance continue face aux biais ou aux incohérences possibles.

Imaginons une séance de conception entre deux développeurs, sauf que l’un d’eux est un LLM. Ce partenaire connaît tout le Web, mais ignore votre contexte exact. Il est rapide, mais naïf. Il est créatif, mais oublie parfois ce qu’il vient de dire. La grammaire de cette interaction, c’est l’ensemble des règles implicites et explicites que vous mettez en place pour que la collaboration reste productive. Ces règles ne sont pas figées : elles s’adaptent selon les outils, les objectifs et les habitudes des personnes impliquées.

Voici quelques principes émergents :

* Toujours recontextualiser.
* Poser une question à la fois.
* Demander des justifications.
* Réinjecter les décisions importantes dans la suite du dialogue.


<p style="text-align: center;">
    <img src="../images/collaboration.png" width="50%" />
</p>

Exemple : dans un projet d’application de gestion de stock, une équipe a utilisé un LLM pour explorer les choix entre architecture en microservices ou en monolithe modulaire. Le prompt initial était vague. Le LLM a généré un comparatif généraliste. En affinant, en injectant des contraintes spécifiques (taille de l’équipe, fréquence des déploiements, besoin d’évolutivité horizontale), les réponses sont devenues beaucoup plus pertinentes. C’est cette capacité à dialoguer, à cadrer, à itérer, qui fait la qualité de la collaboration. Le LLM devient alors un partenaire de simulation, un interlocuteur technique, voire un copilote décisionnel.

Ce chapitre introduit ainsi les grands gestes de cette grammaire nouvelle : cadrer, questionner, reformuler, résumer, contrôler. Cela suppose également une posture d’écoute active et de vigilance critique : il ne suffit pas d’obtenir une réponse, encore faut-il en interroger la pertinence, la source, la cohérence avec le reste du projet. Une équipe travaillant sur une application bancaire a ainsi développé une habitude utile : chaque fois qu’un LLM proposait une solution, l’un des développeurs reformulait cette solution sous forme de diagramme ou de cas d’usage, puis la soumettait au modèle pour validation ou extension. Cette méthode, fondée sur la reformulation visuelle et le questionnement continu, s’est révélée très efficace pour détecter des erreurs subtiles ou des raccourcis dangereux. Elle invite à articuler langage technique et visualisation pour renforcer la robustesse des idées générées.

Un autre exemple intéressant vient d’un atelier de conception participative, où un LLM était utilisé comme facilitateur d’idéation. Les participants posaient chacun leur tour une question au modèle, puis débattaient des propositions émises. Loin de figer la discussion, l’IA servait ici de catalyseur, rendant visibles des pistes implicites ou relançant la créativité collective. Certains motifs proposés par le LLM ont même été repris et raffinés collectivement, montrant une hybridation fertile entre intelligence humaine et intelligence artificielle. Cela montre bien que la grammaire de l’interaction n’est pas une technique froide, mais un art de l’ajustement : ajustement du langage, des intentions, des formats de réponse attendus, et surtout ajustement mutuel entre ce que l’on cherche et ce que l’outil peut offrir. Chaque motif à venir s’inscrit dans ce mouvement, avec une attention particulière à la manière dont le langage façonne l’outil, et inversement. Comprendre cette grammaire, c’est poser les fondations d’un partenariat fructueux avec les LLM.
