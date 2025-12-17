
---

### 🟣 Motif 2 — **Exploration guidée** : *Découper pour mieux avancer*

<p style="text-align: center;">
    <img src="../images/motif_exploration.png" width="50%" />
</p>

**🎯 Contexte**
Vous abordez un sujet complexe, nouveau ou flou — une architecture, un algorithme, une fonctionnalité transversale, un domaine métier inconnu. La tâche paraît vaste ou informe. Vous sentez que vous avez besoin d’un **plan d’attaque** pour avancer étape par étape.

**🚧 Problème**
Le prompt initial mène à une réponse trop large, confuse ou superficielle. Vous recevez une explication générique, sans hiérarchisation des priorités ni découpage utile. Le modèle cherche à répondre à tout… sans résoudre rien de manière exploitable. Résultat : surcharge cognitive, dispersion, perte de temps.

**✅ Solution**
Utiliser le LLM comme **facilitateur de structuration**. Lui demander explicitement de proposer un **découpage progressif du sujet** en étapes, catégories, niveaux d’analyse ou zones fonctionnelles. Vous ne demandez pas encore de solution, mais une **carte du territoire**.

<div class="pb-paper"></div>

> Exemples de prompts :
>
> * « Quelles grandes étapes pour concevoir ce module ? »
> * « Peux-tu proposer un plan d’implémentation en plusieurs phases ? »
> * « Découpe cette problématique en sous-problèmes techniques. »
> * « Quels aspects métier devrais-je explorer en priorité ? »

**📌 Conséquences**

* Réduction de la complexité perçue.
* Meilleure priorisation des tâches.
* Approche plus itérative et incrémentale.
* Découverte d’aspects non envisagés au départ.
* Meilleur alignement entre technique et fonctionnel.

**💡 Exemple d’usage**
Deux développeurs doivent créer un module de traitement de factures dans un ERP.
Prompt initial :

> *« Comment concevoir ce module ? »*

Réponse : longue, dense, difficile à exploiter.
Ils reformulent :

> *« Peux-tu proposer un découpage fonctionnel et technique pour construire ce module ? »*

Le LLM répond :

1. Identifier les sources de données (clients, fournisseurs).
2. Définir les règles de validation métier.
3. Structurer les statuts de traitement.
4. Intégrer les notifications.
5. Gérer les cas d’erreur.
6. Prévoir les exports comptables.

Le découpage devient la base d’un backlog, d’un plan de MVP, et d’un dialogue structuré avec le Product Owner. Le LLM agit ici comme **médiateur d’avancement**.

**🌀 Variantes utiles**

* **Exploration en entonnoir** : demander un plan général → zoomer sur une étape → détailler chaque sous-étape.
* **Exploration multi-angles** : demander un découpage par rôle (technique, fonctionnel, UX), ou selon différentes priorités (coût, impact, risque).
* **Exploration critique** : demander les étapes les plus risquées, ou celles qui méritent un POC.

**🛠️ Outils associés**

* Templates de plan d’implémentation (type RICE, MoSCoW).
* Mindmaps générées à partir de la réponse (via outil visuel).
* Utilisation du LLM comme *Project Planner* ou *architecte conversationnel*.

**🧠 Posture recommandée**
Acceptez de **ne pas chercher à tout résoudre d’un coup**. Appuyez-vous sur le LLM pour **orchestrer une progression** : cartographier avant de coder. Vous devenez facilitateur de focus, plutôt que chercheur de solutions immédiates.

**💬 Prompt-type à mémoriser**

> *« Je travaille sur \[sujet]. Propose une décomposition en étapes concrètes et progressives, pour m’aider à structurer ma démarche. »*
