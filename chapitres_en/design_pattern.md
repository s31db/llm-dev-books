
---
<a id="design_pattern"></a>
## 🏠 Chapter 15 — Rethinking Design Patterns in the LLM Era

> *What if patterns became living dialogues rather than frozen recipes?*

---

### 🤝 Why This Chapter?

For decades, *design patterns* have been a reference point for developers. Yet learning them often stays theoretical, static, and hard to contextualize. What if LLMs could turn these abstract bodies of knowledge into practical conversations?

This chapter offers a new way to explore patterns—not as imposed solutions but as springboards for dialoguing with an AI, testing ideas, clarifying an architecture, and documenting collective decisions.

---

### 📈 Classic Patterns: Strengths, Limits, Challenges

*Design patterns* (GoF, GRASP, DDD, EIP…) provide a shared vocabulary. But in practice:

* They’re often learned without context.
* Their implementation can feel verbose or premature.
* They age poorly in evolving codebases.

LLMs can:

* **Generate contextual variants.**
* **Detect** their presence or absence in code.
* **Argue for or against** a pattern choice.
* **Illustrate dynamically** how a pattern behaves.

---

### 🖊️ Classic Patterns Revisited with AI

Below, each pattern is presented with an “augmented prompt” you could give a model, plus what it brings and what to watch for.

---

#### ✨ Strategy Pattern

**Goal:** Encapsulate interchangeable algorithms.

**Augmented Prompt:**

> “Here are three ways to compute a user score. Suggest a structure that lets me select one dynamically based on context and explain your choice.”

**LLM Contributions:**

* Proposes an interface-based implementation.
* Identifies criteria for switching strategies.
* Can simulate an A/B test by context.

**Caution:** May generate excessive genericity if contextual data aren’t explicit.

---

#### ✨ Observer Pattern

**Goal:** Notify dependent components when an event occurs.

**Augmented Prompt:**

> “I want my module to send a notification every time its state changes, but I don’t want tight coupling. Which pattern applies?”

**Typical LLM Response:**

* Describes the Observer pattern.
* Generates TypeScript or Python code.
* Offers an event/pub-sub alternative.

**Benefit:** Shows multiple forms and highlights the indirect coupling created.

---

#### ✨ Factory Pattern

**Goal:** Delegate object creation to a factory function.

**Augmented Prompt:**

> “I have several implementations of a service depending on environment (prod, test, mock). Suggest a design that’s testable and extensible.”

**Possible Dialogue:**

* AI proposes a Factory or Service Locator.
* Suggests dependency injection.
* Warns against overusing Singleton.

**Reflection Triggered:** How configurable does it need to be? Impact on testing?

---

<div class="pb-A4"></div>

#### ✨ Decorator Pattern

**Goal:** Dynamically add behavior to an object.

**Augmented Prompt:**

> “I have a logging service but want to add optional features (caching, metrics) without modifying the existing code.”

**LLM Contributions:**

* Identifies Decorator.
* Proposes a chained-responsibility version.
* Illustrates possible combinations.

**Caution:** Deeply nested decorators can be hard to maintain.

---

#### ✨ Command Pattern

**Goal:** Encapsulate an action as an object.

**Augmented Prompt:**

> “I want to be able to undo or reschedule certain user operations. What structure should I use?”

**Dialogue:**

* LLM identifies Command.
* Proposes `execute()` / `undo()` / `redo()` interfaces.
* May suggest buffers or queues.

**Interesting Effect:** Encourages thinking in reversible state terms.

---

#### ✨ Adapter Pattern

**Goal:** Match an expected interface with an existing implementation.

**Augmented Prompt:**

> “I have an external API with different names from mine. How do I integrate it without touching client code?”

**LLM Proposals:**

* Simple adaptation interface.
* Warns about transformation or latency costs.
* Alternative: mapping via orchestration layer.

**Benefit:** Quick to deploy, easy to test.

---

#### ✨ Proxy Pattern

**Goal:** Control access to an object (lazy loading, security, logging).

**Augmented Prompt:**

> “I want to protect access to a remote resource with logs and caching. What structure would you suggest?”

**LLM Output:**

* Identifies Proxy (virtual, remote, protective).
* Describes typical use cases.
* Shows an implementation injecting the real subject.

**Key Effect:** Makes control and metrics intentions visible.

---

#### ✨ Composite Pattern

**Goal:** Treat a hierarchy of objects as a single entity.

**Augmented Prompt:**

> “I want to apply the same operation to a group of elements, some of which are groups themselves.”

**AI Dialogue:**

* Proposes Composite.
* Structures a tree example.
* Explains benefits in recursion and polymorphism.

**Benefit:** Simulates complex behaviors with one interface.

---

#### ✨ Builder Pattern

**Goal:** Gradually build complex objects.

**Augmented Prompt:**

> “I have an object with many optional parameters. How can I build it without an unreadable constructor?”

**LLM Contributions:**

* Proposes a fluent Builder.
* Shows how to avoid misconfiguration.
* Suggests an immutable version.

**Warning:** Beware of class explosion.

---

#### ✨ Le pattern “Event Sourcing”

**Goal:** Keep a full history of state changes as events.

**Augmented Prompt:**

> “I want to replay business decisions over time and audit an object’s evolution.”

**AI Dialogue:**

* Proposes Event Sourcing.
* Explains `Command`, `Event`, `Projection`.
* Warns about event versioning.

**Key Effect:** Reliability, auditability—but requires team culture.

---

#### ✨ CQRS (Command Query Responsibility Segregation)

**Goal:** Separate read and write models to optimize each.

**Augmented Prompt:**

> “I need a system with very fast reads but robust business logic on writes.”

**LLM Proposals:**

* Structures `CommandHandler`, `QueryModel`, `ReadStore`.
* Identifies good-fit cases (high-read, scalable systems).
* Warns about added complexity.

**Utility:** LLMs can simulate command/state exchanges clearly.

---

<div class="pb-A4"></div>

#### ✨ Circuit Breaker Pattern

**Goal:** Prevent a failing system from overloading the rest.

**Augmented Prompt:**

> “How can I isolate an unstable service without impacting the whole system?”

**LLM Response:**

* Proposes Circuit Breaker with states (`Closed`, `Open`, `Half-Open`).
* Shows integration with HTTP calls.
* Can even generate configurable threshold metrics.

**Benefit:** LLMs can help test thresholds, fallback scenarios, or even run assisted chaos engineering.

---

### 🎮 New Architectural Dialogue Motifs

| Motif           | Intention                                 | Sample Prompt                                                | Risk                    |
|-----------------|-------------------------------------------|--------------------------------------------------------------| ----------------------- |
| Comparison      | Choose among patterns                     | “Compare Factory, Builder and AbstractFactory for this need” | Bias toward a default   |
| Guided Refactor | Rethink code with a pattern               | “Refactor this module with the Strategy pattern”             | Context error           |
| Diagnostic      | Detect an anti-pattern or structure issue | “Do you see a God Object here?”                              | False positives         |
| Argumentation   | Explain an architectural choice           | “Why use CQRS here rather than CRUD?”                        | Hallucinated advantages |
| Synthesis       | Compare two structures side by side       | “Compare these two models for this functional need”          | Superficial comparison  |

---

### 🎓 Workshop: The Augmented Architectural Dilemma

**Objective:**
Practice orchestrating human+AI architecture thinking in a collective setting.

**Outline:**

1. Present a complex situation (e.g., designing a payment module).
2. Each human+LLM pair proposes a structure + justification.
3. Cross-comparison, then argued voting.
4. Build a hybrid version combining the best ideas.

**Benefits:**

* Exposes diversity of paths.
* Surfaces implicit assumptions.
* Anchors patterns in real reasoning.

---

### 🕵️ Watch-Outs

* **Don’t idolize the pattern:** LLMs can overrate their usefulness.
* **Document your choice:** Why this pattern here, not another?
* **Validate with humans:** Every pattern is a collective decision, not an automatic answer.

---

### 🌐 In Summary

Design patterns are powerful architectural tools. But they come alive when used as a **dialogue scaffold**—between humans, and with AI.

> “A well-used pattern is a conversation between context, intention, and consequence.”

With LLMs, we can learn to document, enrich, test, and sometimes challenge these conversations.
