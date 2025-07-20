
---

### 🟣 Motif 3 — **Spécification inversée** : *Remonter aux intentions à partir du code*

**🎯 Contexte**
Vous devez comprendre un code existant, souvent ancien, mal documenté, ou écrit par quelqu’un d’autre. Vous arrivez *après* la conception. Il n’y a pas de user stories, de documentation claire, ni d’intention explicite. Vous devez pourtant refactorer, auditer, tester, ou réexpliquer ce code.

**🚧 Problème**
Le code vous montre *comment* une chose est faite, mais pas *pourquoi*. Sans les intentions d’origine, les contraintes métier ou les hypothèses implicites, vous êtes obligé de deviner. Cela rend la tâche longue, risquée, frustrante.

**✅ Solution**
Utiliser le LLM comme **détecteur d’intention rétroactif**. Lui soumettre des portions de code, et lui demander de :

* reformuler les intentions fonctionnelles implicites,
* expliciter les règles métier,
* suggérer les user stories probables,
* identifier les hypothèses ou présupposés du développeur initial.

> Exemples de prompts :
>
> * « Que fait ce code ? »
> * « Quelles règles métier cela semble-t-il implémenter ? »
> * « Quelle user story pourrait correspondre à ce bloc de code ? »
> * « Quelles hypothèses implicites sur les données ou le contexte ce code semble-t-il faire ? »

**📌 Conséquences**

* Raccourcit l’analyse d’un code inconnu.
* Produit une **documentation rétroactive**.
* Fait émerger des biais ou angles morts.
* Sert de support à la revue de code, à la transmission ou à la refonte.
* Réconcilie code et métier, implémentation et intention.

**💡 Exemple d’usage**
Lors d’un audit, une équipe hérite d’un module PHP de 800 lignes, sans test ni doc.
Au lieu d’une lecture ligne à ligne, elle découpe le fichier en blocs logiques et utilise ce prompt :

> *« Quelles règles métier ce bloc semble-t-il implémenter ? »*

Le LLM détecte :

* La détection de doublons,
* Le contrôle de TVA,
* L’arrondi conditionnel,
* Des cas particuliers non mentionnés dans la doc.

Ce travail itératif permet de reconstruire les intentions d’origine, de documenter les cas d’usage, et de planifier une refonte sans tout casser.

#### **🌀 Variantes utiles**

* **3.1 — Reconstruction d’User Stories**

Au lieu de demander uniquement *ce que fait le code*, on pousse le LLM à reformuler les intentions en *termes fonctionnels utilisateur*. Exemple de prompt :

> *« En supposant que ce code corresponde à une fonctionnalité d’un produit, quelle user story pourrait-on en déduire ? »*

**Usage** : utile dans des projets où le code a été produit avant la formalisation des besoins (souvent le cas dans des prototypes ou des phases de hackathon).

* **3.2 — Déduction d’hypothèses implicites**

Demandez au LLM :

> *« Quelles hypothèses implicites ce code semble-t-il faire sur les données, les contextes d’exécution ou les droits d’accès ? »*

**Usage** : précieux pour détecter des biais implicites, des présupposés sur les inputs, ou des angles morts en sécurité.

* **3.3 — Contrat d’interface implicite**

Demandez au LLM :

> *« Peux-tu expliciter un contrat d’interface pour cette fonction / ce module (types d’entrées, sorties, erreurs gérées) ? »*

**Usage** : aide à produire des *Design by Contract* à posteriori, ou à documenter des API sans doc initiale.

**🛠️ Outils associés**

* Intégration dans IDE via plugin d’analyse augmentée.
* Prompt-routine de revue de code (cf. chapitre 9).
* Documentation générée à partir du code source, enrichie par LLM.

**🧠 Posture recommandée**
Le LLM ne remplace pas votre lecture du code, il **l’oriente**. Utilisez ses propositions comme **hypothèses de travail**, pas comme vérité. Croisez avec votre intuition, les tests existants, les retours métier.

**💬 Prompt-type à mémoriser**

> *« Voici une fonction sans documentation. Peux-tu expliciter ce qu’elle fait, pourquoi, et quelles hypothèses elle semble faire ? »*
