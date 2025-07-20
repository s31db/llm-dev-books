
---

### 🟣 Motif 5 — **Clarification par contre-exemple** : *Explorer les limites d’une proposition*

**🎯 Contexte**
Le LLM a produit une réponse satisfaisante — un code, une solution technique, une recommandation. Tout semble correct… mais une forme de doute persiste. Est-ce vraiment robuste ? La réponse couvre-t-elle tous les cas ? Le raisonnement tient-il dans les cas extrêmes ?

**🚧 Problème**
Le modèle donne souvent une solution « idéale » ou typique, qui **masque les cas limites ou les situations d’échec**. Le développeur peut être tenté de faire confiance par défaut. Pourtant, sans mise à l’épreuve, on risque de déployer une solution fragile, biaisée ou naïve.

**✅ Solution**
Interroger la réponse **par la négation** : demander un **contre-exemple**, une situation où la solution échoue, devient inefficace ou produit un effet inattendu. Cela révèle les **limites implicites** du raisonnement et affine la compréhension de ce que la solution couvre — ou pas.

> Exemples de prompts :
>
> * « Dans quel cas cette solution pourrait échouer ? »
> * « Peux-tu proposer un exemple de données qui poserait problème ? »
> * « Et si le fichier est vide ? Si la connexion échoue ? Si l’utilisateur n’est pas authentifié ? »
> * « Quelle hypothèse implicite, si elle est fausse, rend cette solution invalide ? »

**📌 Conséquences**

* Détection précoce des cas limites.
* Meilleure robustesse de la solution proposée.
* Formation d’une posture critique chez le développeur.
* Réduction des effets de bord ou des surprises en production.
* Enrichissement du prompt initial si besoin (cf. motif 6).

**💡 Exemple d’usage**
Un étudiant demande au LLM d’implémenter l’algorithme de Dijkstra en JavaScript.
La solution paraît correcte. Il relance avec :

> *« Et si le graphe contient des cycles négatifs ? »*

Le LLM répond :

> *« Dijkstra n’est pas adapté à ce cas. Il faudrait utiliser Bellman-Ford, qui gère les poids négatifs. »*

Cette simple relance transforme une session de génération en **moment d’apprentissage algorithmique**, en rendant visible une hypothèse invisible.

**🌀 Variantes utiles**

* **Test de bord** : « Et si le tableau est vide ? Si une donnée est nulle ? »
* **Stress test** : « Et si 10 000 utilisateurs accèdent à ce module en même temps ? »
* **Contre-règle métier** : « Quelle situation métier invaliderait cette règle ? »
* **Débat simulé** : « Peux-tu simuler l’avis d’un développeur qui critique cette solution ? »

**🛠️ Outils associés**

* Table de tests d’acceptation enrichie par le modèle.
* Utilisation combinée avec la génération de jeux de tests (cf. motif 3).
* Pairing augmenté : un développeur joue l’avocat du diable avec le LLM.

**🧠 Posture recommandée**
Ne te satisfais pas de la « bonne réponse » en apparence. Adopte une **posture scientifique** : falsifier, tester, pousser la logique jusqu’à ses bords. C’est ainsi que le LLM devient un **partenaire critique**, et non un automate flatteur.

**💬 Prompt-type à mémoriser**

> *« Donne un cas qui fait échouer cette solution. Qu’est-ce que cela révèle sur ses limites ? »*
