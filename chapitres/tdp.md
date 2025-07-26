
---

## 🧪 Annexe 2 — **TDP : Test-Driven Prompting**

> Et si on abordait un **prompt** comme un **test** ?
> Le **Test-Driven Prompting** (TDP) transpose les principes du TDD (Test-Driven Development) au dialogue avec les LLMs : on **définit d’abord l’intention et les critères de qualité**, puis on rédige un prompt, on teste, on ajuste.

---

### 🎯 Objectif

Structurer les interactions avec un LLM **de manière rigoureuse et vérifiable**, en explicitant **ce que l’on attend** d’une réponse — avant même de rédiger le prompt.

---

### 💡 Geste professionnel augmenté

| Avant (prompt classique)            | Avec TDP                                                       |
|-------------------------------------|----------------------------------------------------------------|
| Pose une question “à la volée”      | Définit d’abord l’intention et les critères de succès          |
| Corrige le prompt après un échec    | Anticipe les cas de test dès la formulation                    |
| Réagit aux réponses au fil de l’eau | S’appuie sur une boucle explicite d’évaluation et d’ajustement |
| Difficile à partager ou capitaliser | Produit un artefact testable, transmissible, documentable      |

---

### 🧱 Structure d’un TDP

1. **Intent** → Ce que je veux produire, générer, explorer
2. **Critères de succès** → Ce qui rendra la réponse utilisable ou satisfaisante
3. **Prompt initial** → Première formulation structurée
4. **Cas de test** → Données d’entrée/sortie, formats attendus, contre-exemples
5. **Boucle d’ajustement** → Révision du prompt à partir des écarts observés

---

<div class="pb-A4"></div>

### 🧪 Exemple de TDP

> **Intention** : Générer une API REST Node.js basique avec Express
>
> **Critères de succès** : 
> * Doit contenir au moins deux routes
> * Utiliser `express.json()`
> * Inclure une structure de dossier propre
>
> **Prompt initial** :  
> « Crée une API REST Express avec deux routes (GET/POST), utilisant express.json() et une structure propre. »
>
> **Cas de test** :
> * Présence d’un fichier `index.js` avec routes claires ✅
> * Utilisation de `express.json()` ✅
> * Structure MVC ❌ → à préciser
>
> **Boucle d’ajustement** :  
> → Ajouter au prompt : « Organise le code en respectant un modèle MVC simple. »

---

### 🧰 Trucs et tactiques

* 🔍 **Écrire les cas de test avant le prompt**, comme en TDD
* 📎 **Conserver ses TDP** pour les rejouer, les adapter, les transmettre
* 💬 **Comparer plusieurs prompts pour une même intention**, en conservant les critères constants
* 🧠 **Utiliser les motifs comme générateurs de tests** (Contre-exemple, Miroir, etc.)
* 🧪 **Itérer à froid** : relire un TDP après coup pour identifier ses angles morts

---

### 🧠 Postures associées

| Posture                   | Ce qu’elle active dans le TDP                                 |
| ------------------------- | ------------------------------------------------------------- |
| **Concepteur de prompts** | Formule avec précision l’intention                            |
| **Explorateur critique**  | Questionne la qualité de la sortie avec des cas d’usage réels |
| **Éditeur augmenté**      | Ajuste finement les formulations pour guider le modèle        |
| **Curateur rigoureux**    | Capitalise les prompts testés et efficaces                    |

---

<div class="pb-A4"></div>

### ⚠️ Points de vigilance

* Le TDP **ne garantit pas une réponse parfaite**, mais une démarche itérative, claire et partageable.
* Attention à ne pas **sur-formaliser des demandes simples** : adapter le niveau d’effort au contexte.
* Le **risque inverse existe aussi** : trop vague, un prompt reste interprété au petit bonheur.

---

### 🛠 Pour aller plus loin

* Introduire les TDP dans vos **revues de prompt** ou **sessions d’équipe**
* Versionner vos TDP dans un **dossier projet ou base de connaissances**
* Utiliser les TDP en formation ou pair-prompting comme **support de discussion sur la clarté**

---

> **Test-Driven Prompting**, c’est penser le prompt **comme un test** : explicite, améliorable, et tourné vers l’action.
> Une pratique rigoureuse… pour un dialogue plus fluide.
