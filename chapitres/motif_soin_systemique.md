
---

### 🟣 Motif 8 — **Soin systémique** : *Investiguer les causes profondes d’un problème*

**🎯 Contexte**
Un problème persiste dans un projet ou une équipe. Il peut s’agir d’un bug récurrent, d’une démotivation latente, d’un retard accumulé, ou d’une tension interpersonnelle. Ce n’est pas simplement un défaut technique ou organisationnel isolé : **quelque chose coince en profondeur**, mais sans cause évidente.

**🚧 Problème**
Le réflexe est souvent de chercher une solution rapide, locale, technique. Or, en s’arrêtant au symptôme visible, on risque de **passer à côté des vraies causes** — souvent multiples, croisées, systémiques. Le LLM, s’il est mal sollicité, proposera des rustines plutôt qu’un diagnostic structuré.

**✅ Solution**
Mobiliser le LLM comme **partenaire d’investigation systémique**. Ne pas lui demander une solution directe, mais l’**aider à vous aider à creuser** :

* explorer les causes possibles d’un problème,
* croiser les angles de vue (technique, humain, organisationnel),
* proposer des pistes d’action ciblées et cohérentes avec la cause réelle.

> Exemples de prompts :
>
> * « Voici un problème récurrent dans l’équipe. Quelles causes possibles vois-tu, côté technique, relationnel, process ? »
> * « Peux-tu me guider dans une session de type 5 Pourquoi / 9 Pourquoi pour en explorer la racine ? »
> * « Propose un arbre logique des causes et sous-causes. »

> 🧭 **Les Neuf Pourquoi : creuser le sens pour mieux agir**
>
> Inspiré des **Liberating Structures**, le canevas des *Nine Whys* propose un rituel simple, mais puissant : poser neuf fois de suite la question **« Pourquoi est-ce important pour toi ? »** à partir d’un sujet donné.
>
> Loin d’être un interrogatoire, c’est un **chemin de clarification progressive**, où chaque réponse devient la base de la question suivante. On ne cherche pas une cause unique, mais une **profondeur de sens** : ce qui motive vraiment l’action, ce qui fonde les choix, ce qui compte profondément.
>
> Dans le cadre du développement logiciel, cet outil devient précieux quand :
>
> * une décision semble évidente mais suscite du flou ou de la résistance,
> * un problème technique récurrent cache des tensions humaines ou systémiques,
> * une équipe veut aligner ses efforts sur ce qui a du sens.
>
> 👉 Le LLM peut ici jouer un rôle de **facilitateur de questionnement** : en proposant des formulations de relance, en structurant les réponses, ou en révélant des contradictions implicites.
>
> > Exemples de prompts :
> >
> > *« Peux-tu m’aider à simuler une session de Nine Whys sur ce problème : \[décrire la situation] ? »*
> > *« À chaque réponse, propose une reformulation de "Pourquoi est-ce important ?" en changeant légèrement l’angle (valeurs, impact, émotion, système…). »*

**📌 Conséquences**

* Permet de **poser un diagnostic partagé** avant d’agir.
* Prévient les actions prématurées ou mal orientées.
* Favorise l’intelligence collective et la réflexivité.
* Crée des solutions mieux ancrées dans le réel.
* Apporte de la lucidité là où règne parfois l’agitation.

**💡 Exemple d’usage**
Une équipe ressent une **démotivation diffuse** autour d’un module critique.
Prompt initial :

> *« Comment remotiver l’équipe ? »*

Réponses : un peu génériques (célébrer les victoires, changer d’environnement…).
Le Scrum Master reformule :

> *« Pourquoi cette démotivation, selon toi ? Peux-tu explorer plusieurs causes possibles, en croisant les dimensions technique, humaine et organisationnelle ? »*

Le LLM propose :

* dette technique anxiogène,
* flou sur les critères de qualité,
* manque de reconnaissance des efforts.

L’équipe creuse ces causes une à une, et en tire **trois actions concrètes** : clarification des règles de qualité, rituel de reconnaissance des avancées, refactoring progressif encadré.

**🌀 Variantes utiles**

* **Arbre des causes** : diagramme arborescent des causes/symptômes.
* **Multi-perspectives** : demander au LLM d’analyser la situation selon le point de vue d’un dev, d’un PO, d’un manager.
* **Hypothèses contradictoires** : pousser le modèle à générer plusieurs explications différentes d’un même symptôme.

> Prompt-type :
> *« Donne-moi trois hypothèses opposées sur les causes probables de cette situation. »*

**🛠️ Outils associés**

* Modèles d’analyse systémique (5 Pourquoi, 9 Pourquoi, Ishikawa, diagrammes de boucle causale).
* Canevas d’enquête partagée avec le LLM comme facilitateur de questionnement.
* Revue de sprint augmentée par exploration des causes racines (cf. chapitre 8).

**🧠 Posture recommandée**
Refuser la précipitation. Prendre le temps de **comprendre avant d’agir**. Solliciter l’IA non comme oracle, mais comme **co-investigateur systémique**. Cela demande écoute, nuance, et capacité à laisser surgir des causes non techniques dans un monde souvent technique.

**💬 Prompt-type à mémoriser**

> *« Voici un problème qui revient souvent. Peux-tu m’aider à en explorer les causes racines selon plusieurs angles, sans proposer tout de suite une solution ? »*
