
---

### 🟣 Motif 4 — **Modèle miroir** : *Comparer pour éclairer un choix*

<p style="text-align: center;">
    <img src="../images/motif_miroir.png" width="50%" />
</p>

**🎯 Contexte**
Vous hésitez entre plusieurs solutions possibles : deux architectures, deux approches algorithmiques, deux styles de code, deux outils. L’équipe discute, mais le débat reste flou ou biaisé. Vous avez besoin de prendre du recul pour décider *en conscience*, et pas par réflexe ou préférence personnelle.

**🚧 Problème**
Le LLM répond souvent avec *une seule solution* par défaut. Or, dans les situations complexes, il est plus utile de **comparer plusieurs options** que d’en générer une « réponse-type ». Sans confrontation d’alternatives, on risque de s’en tenir à une première bonne impression… sans voir les conséquences.

**✅ Solution**
Utiliser le LLM comme **miroir comparatif** : lui demander explicitement de produire plusieurs variantes d’une solution, puis de les comparer selon des critères définis (lisibilité, performance, maintenabilité, UX…). Cela transforme la réponse en **analyse dialectique**, qui éclaire la décision.

> Exemples de prompts :
>
> * « Propose deux implémentations de cette fonction : l’une impérative, l’autre fonctionnelle. Compare-les. »
> * « Donne trois options d’architecture et leurs avantages/inconvénients selon nos contraintes. »
> * « Compare React et Svelte pour ce type de projet. »

<div class="pb-A4"></div>

**📌 Conséquences**

* Favorise l’analyse critique au lieu du mimétisme.
* Explicite les critères de choix.
* Aide à la décision collective, surtout dans un contexte d’équipe.
* Réduit le biais de confirmation ou d’autorité.
* Sert de support à la documentation des décisions.

**💡 Exemple d’usage**
Dans un projet de refonte de système de paiement, l’équipe hésite entre :

1. Une architecture orientée événements avec Kafka
2. Une architecture REST synchrone plus classique

Le prompt devient :

> *« Compare ces deux options pour un système haute disponibilité avec 100 transactions/s. Quels sont les compromis ? »*

Le LLM souligne que :

* Kafka est plus résilient mais plus complexe à monitorer,
* REST est plus simple à tester mais moins robuste aux pics de charge.

La discussion s’appuie sur ces éléments pour prendre une **décision argumentée**, et pas simplement « parce qu’on a toujours fait comme ça ».

**🌀 Variantes utiles**

* **Miroir de styles** : comparer style impératif vs fonctionnel, orienté objet vs déclaratif.
* **Miroir de paradigmes** : polling vs event-driven, synchronisme vs asynchronisme.
* **Miroir d’outils** : frameworks front, moteurs de base de données, bibliothèques de tests, etc.
* **Miroir UX** : comparer deux messages d’erreur, deux parcours utilisateur.

**🛠️ Outils associés**

* Grille de comparaison à co-construire avec le LLM.
* Tableau à double entrée : options × critères.
* Intégration possible dans une documentation de choix d’architecture (ADR).

**🧠 Posture recommandée**
Demandez *plusieurs options* avant de creuser une seule. Faites du LLM un **stimulateur de divergence raisonnée**. Il ne décide pas à votre place — il éclaire le chemin.

**💬 Prompt-type à mémoriser**

> *« Propose plusieurs alternatives pour ce besoin, puis compare-les selon ces critères : \[X, Y, Z]. »*
