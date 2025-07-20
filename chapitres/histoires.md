
---

### 🎭 Deux histoires ordinaires

Nous avons vu que la honte n’est pas un symptôme individuel, mais souvent le reflet d’un collectif qui ne sait pas encore comment accueillir l’usage de l’IA.

Mais au-delà des principes, il y a les gestes du quotidien.
Ce qu’on ose dire — ou pas.
Ce qu’on cache dans un coin d’onglet.
Ce qu’on partage, ou ce qu’on tait.

Pour prolonger cette réflexion, voici deux récits inspirés de situations réelles.
Deux façons d’interagir avec l’IA.
Deux postures. Deux climats d’équipe.

L’une se vit en silence.
L’autre se transforme en apprentissage collectif.

---

### 🪞 **Ce qu’on ne dit pas**

Maxime est développeur depuis sept ans. Il aime le code propre, les tests qui passent du premier coup, les specs bien ficelées. C’est un dev rigoureux. Un “vrai”, comme il dit.

Ce matin, il est bloqué sur une fonctionnalité de parsing JSON. Un truc bancal, mal défini, avec des cas tordus. Il tourne en rond depuis une heure. Rien ne marche. La pression monte — c’est la fin du sprint.

Il regarde autour de lui. Personne ne semble faire attention.
Il ouvre un onglet privé. Tape vite fait dans ChatGPT :

> *"Comment parser un JSON avec des relations imbriquées en Java ?”*

Quelques secondes. La réponse s’affiche. Simple. Efficace. Étonnamment claire.

Il sent une gêne. Trop facile.
Mais il copie, adapte deux ou trois lignes.
Les tests passent. Il commit :

```bash
git commit -m "implémentation parsing JSON"
```

Pas de mention de l’IA. Même pas un commentaire dans le code.

Le lendemain, au daily, Adrien jette un œil à la PR :

> — Joli ! C’est toi qui as trouvé ce pattern ?
> Maxime hoche la tête :
> — J’ai… fait des recherches.

Personne ne dit rien. Il passe la parole au suivant.

Mais Maxime, lui, sent un creux. Il a l’impression d’avoir triché.
Il se dit qu’il reviendra dessus plus tard, pour comprendre vraiment.
Il ne reviendra pas.

Le soir, en scrollant sur LinkedIn, il tombe sur un post viral :

> *“Les développeurs qui délèguent à l’IA ne sont plus que des assembleurs. Triste époque.”*

Il ne like pas. Il ne commente pas.
Il ferme l’appli. Reste une petite boule au ventre.
Il a livré à l’heure. Le code fonctionne. Personne ne lui a rien reproché.

Mais au fond, il doute.

---

### 🌱 **Ce qu’on cultive**

Sarah n’est pas du genre à garder les choses pour elle. Développeuse fullstack depuis cinq ans, elle aime autant coder que réfléchir à la manière dont on collabore. Elle a proposé récemment d’ajouter un temps de veille IA dans la rétrospective. “Pour qu’on arrête de faire nos tests dans notre coin.”

Ce matin, elle démarre une nouvelle tâche avec Léo, un·e junior fraîchement arrivé·e dans l’équipe.
Fonctionnalité à fort enjeu : synchroniser deux systèmes d’authentification.

Sarah ouvre son éditeur, puis un fichier `.md` à part.

> — On peut démarrer par un peu de prompting ensemble. Juste pour explorer.

Léo hésite.

> — On ne va pas coder directement ?
> 
> — Si, mais regarde. Ça nous évite de rester enfermés dans une seule approche.

Elle tape :

> Contexte : On doit faire cohabiter deux systèmes de login (LDAP et OAuth) dans une même appli backend.
>
> Prompt : Donne 3 stratégies possibles avec avantages/inconvénients pour ce scénario.

ChatGPT propose trois options, bien structurées.

Ils lisent ensemble. Sarah ne choisit pas pour Léo. Elle demande :

> — Laquelle tu trouves la plus simple à tester ?
> 
> — La deuxième. Mais faudrait éviter que ça devienne spaghetti.

Ils modifient le prompt. Demandent un exemple. Puis un autre avec un twist de sécurité. Ils discutent, rigolent parfois — quand l’IA propose des choses absurdes.
Au final, ils codent une version adaptée, issue du deuxième scénario.

Dans la PR, Sarah ajoute un encart en bas du `README.md` de la fonctionnalité :


> 🧠 **Exploration IA**
> 
> Prompt utilisé : comparaison stratégies login<br/>
> Réponse retenue : option 2 (adaptée)<br/>
> Discussion en binôme : Léo + Sarah<br/>
> Leçon : le prompt nous a aidés à expliciter les besoins de sécurité avant de coder.


En rétro, elle partage l’expérience :

> — Ce que j’ai aimé, c’est que ça nous a obligés à clarifier nos attentes. Et que Léo a pu voir plusieurs solutions dès le départ.

Tom, l’architecte, rebondit :

> — Tu peux l’ajouter dans le répertoire des prompts utiles ? Ce cas va revenir.

Sarah sourit.
Elle ne sent ni honte, ni gêne.
Juste la satisfaction d’avoir transmis quelque chose.
Et d’avoir fait de l’IA un outil au service de l’équipe — pas un secret de productivité.

---

### 🧩 Ce que ces histoires révèlent

Ces deux récits racontent beaucoup plus que des prompts ou des commits.
Ils mettent en lumière ce qui se joue **quand la technique rencontre l’humain** :

* La première histoire parle de **silence**, de stratégie d’évitement, de peur du regard.
  Elle montre comment l’usage de l’IA peut générer du **repli**, même chez des développeurs compétents.

* La seconde parle de **dialogue**, de réflexivité, de mise en commun.
  Elle illustre comment un usage assumé de l’IA devient un **levier de progression collective**.

La différence ne tient pas à l’outil, ni au niveau technique.
Elle tient à l’environnement. À la culture d’équipe. À ce qui est possible, autorisé, valorisé.

**Créer une culture “non honteuse” de l’IA, c’est une responsabilité partagée.**
Cela demande des rituels, des espaces pour en parler, des cadres où l’erreur devient apprentissage.

Parce qu’au fond, l’enjeu n’est pas d’utiliser ou non une IA.
L’enjeu est de **rester humain dans la manière de s’en servir** — et dans la manière d’en parler ensemble.
