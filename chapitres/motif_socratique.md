
---

### 🟣 Motif 1 — **Question Socratique** : *Reformuler pour comprendre*

<p style="text-align: center;">
    <img src="../images/motif_socratique.png" width="50%" />
</p>

**🎯 Contexte**
Un besoin est exprimé de façon floue, incomplète, ou imprécise — que ce soit par vous-même, un collègue, un client ou un utilisateur. Vous entrez dans une zone d'incertitude : la formulation initiale du prompt est insuffisante pour guider une réponse utile. Cela peut se produire au début d’un projet, dans une phase d’exploration, ou lors d’un échange interdisciplinaire.

**🚧 Problème**
Un prompt flou génère une réponse générique, stéréotypée, ou hors-sujet. Le LLM comble les vides par des hypothèses implicites — souvent différentes de vos intentions réelles. Cela entraîne perte de temps, mauvaise orientation de la discussion ou illusion de progrès.

**✅ Solution**
Adopter une posture de **questionnement socratique** : poser des **questions ciblées, progressives et ouvertes** pour affiner la compréhension de l’intention réelle. Vous invitez le modèle à vous aider à **mieux formuler votre propre besoin**. Ce faisant, vous explorez les contours de la demande avant d'attendre une réponse structurée.

> Exemples de relances utiles :
>
> * « Quels types d’erreurs souhaitez-vous capturer ? »
> * « À qui est destinée l’alerte ? »
> * « Quelles sont les conséquences attendues de cette action ? »
> * « À quel moment dans le processus intervient ce script ? »

<div class="pb-A4"></div>

**📌 Conséquences**

* Clarifie l’intention initiale, même pour le demandeur humain.
* Enrichit le prompt au fil du dialogue.
* Déclenche un **raisonnement partagé** avec le LLM.
* Diminue le risque de mauvaise direction ou de sur-généralisation.
* Rend l’utilisateur plus conscient de ses propres besoins implicites.

**💡 Exemple d’usage**
Un développeur envoie au LLM :

> *« Crée un script d’alerte. »*

Réponse : trop générique, pas exploitable.

Il relance :

> *« Ce script doit détecter des erreurs de facturation dans des fichiers CSV. Quels types d’erreurs puis-je surveiller ? Peux-tu me proposer des catégories ? »*

Le LLM identifie :

* Montants incohérents
* Dates invalides
* Références manquantes
* Doublons

À partir de là, le développeur reformule une demande beaucoup plus précise :

> *« Génère une fonction Python qui scanne un dossier de fichiers CSV, détecte les erreurs listées ci-dessus, et envoie un rapport par mail en fin de traitement. »*

Cette démarche transforme un prompt vague en **spécification dialoguée**.

**🌀 Variantes utiles**

* **Pour cadrer un besoin métier** :

  > « Peux-tu me poser 5 questions pour clarifier ce que je veux faire ? »
* **Pour aider un PO ou un stakeholder** :

  > « Imagine que je ne suis pas sûr de ce que je veux. Aide-moi à explorer les options à partir de mes contraintes. »

<div class="pb-A4"></div>

**🛠️ Outils associés**

* Mode *roleplay* : demander au LLM d’agir comme un UX designer, un coach agile ou un product manager.
* Canevas de clarification des besoins (cf. chapitre 9).

**🧠 Posture recommandée**
Ne cherchez pas une réponse immédiate. Cherchez la **bonne question suivante**. Ce motif vous transforme, vous aussi, en facilitateur de votre propre clarté.

**💬 Prompt-type à mémoriser**

> *« Aide-moi à clarifier ma demande en me posant des questions. Ne propose pas encore de solution. »*
