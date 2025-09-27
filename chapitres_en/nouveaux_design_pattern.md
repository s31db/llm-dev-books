
---
<a id="nouveaux_design_pattern"></a>
## 🤖 Chapter 16 — Emerging Design Patterns in the Era of LLMs and AI Agents

> *When artificial intelligence becomes an actor in the system, new patterns appear.*

---

### 🎯 Purpose of This Chapter

This chapter explores **new, still-forming design patterns** that are emerging with the growing use of LLMs and AI agents in software architectures. These patterns are not yet standardized, but they help imagine:

* dialogic systems,
* autonomous or orchestrated agents,
* distributed chains of reasoning,
* intent-driven infrastructures,
* conversational artifacts as design objects.

They reflect an evolution of software architectures toward greater reflexivity, modularity, and human–machine collaboration.

---

### 🧪 What Is an Emerging Pattern?

An *emerging pattern* is:

* **Not canonized** (not formally documented yet),
* **Recurrent** in experiments or tools,
* **Born from real use** but still evolving,
* **Potentially disruptive** (intent > instruction, dialogue > command).

This chapter draws on observations of prototypes, open-source tools and practices from pioneering teams.

---

<div class="pb-A4"></div>

### 🔭 New Patterns with LLMs

#### 🧠 “Collaborative Agent” Pattern

> A specialized AI agent assisting a human role in a reflexive loop.

* Role: support for decision-making, analysis, verification.
* Examples: *Windsurf*, *Amazon Q for DevOps*, *Mintlify*.
* Characteristics: context tracking, open dialogue, explainability.

**Sample Prompt:**

> “Act as a friendly reviewer: read this code and ask me the right questions.”

**Benefits:** Keeps the human responsible while enriching their perspective.

---

#### 🧩 “Chain of Reason” (Chain-of-Thought Engine)

> Structure a complex task into logical steps assigned to one or more LLMs.

* Explicit stages: plan, clarify, execute, verify.
* Used in agentification, multi-turn generation, self-evaluation.
* Team remains in supervision.
* Can be combined with *prompt chaining* or *Tree of Thought*.

**Sample Prompt:**

> “Break the following problem into steps, then solve each step one by one.”

**Risk:** Accumulation of imprecision or bias if left unchecked.

---

#### 🔗 “Prompt Chaining” Pattern

> Link several prompts to break down complex reasoning or generation.

* Each step produces an output reused in the next.
* Lets you control progression and validate intermediate hypotheses.
* Makes reasoning reproducible and auditable.

**Example Pipeline:**

1. Generate a summary of a business need.
2. Derive three meaningful test cases.
3. Generate the test code for each.

**Effect:** Clear, structured, iterative thinking pipeline.

---

#### 🌳 “Tree of Thought” Pattern

> Explore multiple reasoning paths in parallel, selecting or combining the best ideas.

* Tree-like rather than linear approach.
* Each “thought” is developed, evaluated, compared.
* Suited to architecture choices, ambiguous decisions, complex resolutions.

**Example:**

> “Should we break this module into microservices?” → The LLM explores performance, maintainability, costs, etc.

**Benefit:** Greater reflexivity, avoids single-path or local-optimum bias.

---

#### 🛠️ “Prompt as Interface” Pattern

> Treat the prompt as a persistent, versioned, testable artifact.

* Role: intermediary between human intent and AI implementation.
* Can be designed like a specification: “the prompt is authoritative.”
* Versioned, commented, auto-tested.

**Example:** A file `ask_for_architecture_analysis.prompt.md` reused across projects.

**Effect:** Industrializes formulation while keeping the flexibility of natural language.

---

#### 🕸️ “Agent Mesh” Pattern

> A set of specialized AI agents cooperating without a fixed hierarchy.

* Each agent has an expertise or function.
* Communicate via messages, shared memory, local arbitration.
* Inspired by *microservices*—but cognitive.

**Example:** A user-support system with diagnostic agent, rephraser and synthesizer.

**Effect:** Greater cognitive scalability, but higher coordination complexity.

---

<div class="pb-A4"></div>

#### 🧭 “Intention Router” Pattern

> Dynamically select the right tool, agent or LLM based on expressed intent.

* Requires intent classification (analyze, generate, critique…).
* May use a first LLM to route the request.
* Compatible with a *Plug & Prompt* approach.

**Sample Prompt:**

> “From the following question, choose the right tool among A, B, C or me.”

**Benefit:** Smooths the user experience, avoids prompt overload.

---

### 🧰 Representing These New Patterns

These motifs call for new visualization tools:

* **Hybrid diagrams**: humans + agents + LLMs.
* **Conversational timelines**: before / during / after interaction.
* **Explicit roles**: designer, validator, arbitrator.
* **Visualizing intentions** rather than only flows.

Tools like Mermaid, D2 or tldraw can be repurposed to represent these complex interactions.

---

### 🎮 Workshops to Explore Emerging Patterns

#### 🧪 “Pattern Invention” Workshop

> Imagine a pattern starting from a prospective need.

* Material: blank canvas, scenario board, LLM as creative partner.
* Steps: situation → problem → interaction → benefit → pattern name.
* Output: a living pattern card tested in a simulated situation.

#### 🎲 “Pattern Observatory” Workshop

> Identify existing motifs in team practices.

* Goal: observe real uses and give them names.
* Format: collective table (name, situation, example, trap, success).
* Can be kept in Notion, Miro, Gitbook…

---

<div class="pb-A4"></div>

### ⚠️ Limits and Cautions

* ⚖️ A pattern is only useful if it answers a real situation.
* 🔍 You must **experimentally validate** what AI proposes as a motif.
* 🧠 Co-construction with humans remains essential.
* 📚 Easy to drift into buzzwords: a name alone doesn’t create value.

> What matters is not inventing patterns… but recognizing the ones truly emerging.

---

### 📌 In Summary

* AI-augmented systems generate **new forms of organizing reasoning**.
* These forms can be described as *emerging design patterns*.
* They don’t replace classical patterns but extend them into reflective, intentional, collaborative contexts.
* Documenting, naming and testing them is a collective act of **engineering-in-the-making**.

> Today’s patterns are tomorrow’s engineering languages.
