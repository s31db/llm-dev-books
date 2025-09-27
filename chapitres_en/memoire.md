
---
<a id="memoire"></a>
## 🗂️ Chapter 12 — Documenting, Archiving, Capitalizing: Toward an Augmented Memory

> Every interaction with an LLM leaves a trace. But if that trace isn’t kept, structured, or shared, it disappears.
> Designing with an LLM also means **caring for a new kind of memory** — conversational, living, and shared.

---

### 🧭 Why This Chapter?

The patterns we’ve explored are born from concrete situations. But to keep them alive over time, they must be **documented, archived, and capitalized**.

In the age of generative AI, our interactions with LLMs produce a new form of “gray matter”: explorations, hypotheses, leads, and productive mistakes. Too often, these dialogues vanish as soon as they’re used.

This chapter proposes turning these exchanges into **lasting informational assets** by integrating prompts, responses, adjustments, and learnings into the living memory of projects.

It’s not about “doing documentation” in the traditional sense, but about **building an augmented memory** that supports:

* the quality of deliverables,
* individual and collective learning,
* handovers between people and between generations of teams.

It’s an invitation to think of documentation as a **reflective extension of our practice**, supported by AI but shaped by real-world needs.

---

### 🗂️ Three Levels of Augmented Memory

#### 🧠 Interaction Memory

Keeps the record of a specific exchange with an LLM.
Purpose: replay, review, and learn from experience.

| Element | Typical Content |
|-----------------|-------------------------|
| Original prompt | With context and intent |
| LLM response    | Retained version or intermediate iteration |
| Human modifications | What was kept, rejected, or altered |
| Associated tag/pattern | e.g. “guided exploration,” “technical mirror” |

<div class="pb-A4"></div>

👉 **Suggested format:** `.prompt.md` file or Obsidian/Notion entry
👉 Example naming: `2025-05-05_mirror-pattern_auth-service.md`

---

#### 📁 Project Memory

Integrates AI-generated content into project artifacts.
Purpose: future understanding, reviews, audits.

| Object Type | Example of Associated Documentation |
|-------|-------------------------------------|
| Generated code | Comment with source prompt + LLM version |
| Specification | Archive of the conversation that led to a user story |
| Architecture | AI-generated comparison of two implementation options |
| Tests | Origin of the test set (generated, adapted, validated by the team) |

👉 **Suggested format:** `/doc/ai_interactions/` folder with `prompt + response + lessons learned`
👉 Bonus: create an **augmented PR** explaining how AI contributed.

---

#### 🏛️ Collective Memory

Formalizes patterns, best practices, prompt canvases, and intent tests useful to the team or community.

| Element                   | Use                           |
| -------------------------- | ------------------------------- |
| Library of lived patterns | Training, reviews, onboarding |
| Annotated prompt library  | Reuse and adaptation        |
| Generative team journal   | Usage history, discussion, evolution |
| In-house grammar guide    | Internal prompting guide      |

👉 **Tools:** Miro / Notion / GitBook / Docusaurus…
👉 Tip: start small. One page called “Patterns of the Week” is enough to begin.

---

### 🧪 Example of a Living Memory: a “/prompts/” Folder

```
/prompts/
  2025-06-01_refactor_service.md
  2025-06-03_auth_vs_oauth_comparison.md
  2025-06-05_ui_a11y_review.md
```

Each file contains:

* Context (who, when, why)
* Original prompt
* Selected response
* Human modifications
* Associated patterns
* Lessons learned

This folder can be synced with Git, integrated into reviews, or presented during retrospectives.

---

### 🧭 Toward an Architecture of Conversational Memory

An “augmented memory” is not a static repository. It’s:

* **A space for dialogue with future contributors**
* **A support for learning and continuous improvement**
* **A lever for trust and transparency**

It can be **personal, team-based, or collective**, but it should always be:

* accessible,
* understandable,
* contextual,
* kept up to date.

---

### ✏️ In Summary

* Documenting exchanges with LLMs isn’t bureaucracy. It’s **cognitive architecture**.
* Think at three levels: **interaction, project, collective**.
* A well-organized memory lets you **capitalize without ossifying**.
* It’s a cornerstone for transferring knowledge, maintaining quality, securing outputs, and learning.

> An augmented memory isn’t an archive.
> It’s a **living trace of a design dialogue.**
