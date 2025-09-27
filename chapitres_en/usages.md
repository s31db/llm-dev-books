
---
<a id="usages"></a>
## 🎓 Chapter 11 — Using AI in Learning

### AI as a Tutor and Learning Partner

One of the most immediate uses of LLMs is **guided self-learning**.
A developer can query the model as a mentor available anytime — to ask for an explanation, an analogy, a code example, or a reformulation.

> **Examples:**
> – *“Can you explain JavaScript closures to me as if I were 12?”*
> – *“Show me three versions of this function, from simplest to most optimized.”*

This lets people learn at their own pace, quickly close knowledge gaps, and consolidate their understanding.
The LLM becomes a **permanent learning companion**, customizable and non-judgmental.

Many teams already encourage this as a natural reflex: don’t stay blocked — “ask the AI” before interrupting a colleague — or, conversely, use it to prepare for a more focused discussion.

---

### AI-Assisted Documentation

Documentation is often neglected or postponed. With AI, it’s now possible to generate it **incrementally and in context**, drawing from:

* reading a source file,
* a commit or ticket history,
* a technical chat exchange,
* a recorded demo.

> **Examples:**
> – Automatically generate docstrings from code.
> – Provide a technical summary of a module or a ticket.
> – Synthesize a Markdown document from a Slack or Notion thread.

This on-demand documentation reduces cognitive friction, enables more regular updates, and makes it easier to share with non-technical roles (POs, UX, business stakeholders…).

---

<div class="pb-A4"></div>

### Prompts as Versioned Artifacts

One of the most innovative concepts in this new paradigm is the **prompt as a documentation artifact**.
A well-crafted prompt can become a *resource in its own right*, just like a unit test or a Jira ticket.

> **Example:**
> A prompt used to generate an automated test plan or a component template can be stored, versioned, reviewed, shared, and adapted for other projects.

This means:

* keeping a record of important prompts (in Git, a wiki, or a prompt database),
* attaching their context (need, goal, constraints),
* reviewing them collectively (like code reviews).

Tools are already emerging around this idea — *prompt repositories*, *prompt templates*, *prompt linters*, etc. — fostering a culture of **transparency and shared design thinking**, where many decisions used to remain implicit.

---

### Team Workshops, Learning Loops, and Augmented Coaching

AI can also enrich team dynamics by feeding **collective learning rituals**.
Here are some effective formats:

#### “Prompt Clinic” Workshop

Each member brings a prompt they’ve used, and the team discusses:

* its clarity,
* its robustness,
* the results obtained,
* possible improvements.

This shares prompting practices and cultivates a reflective stance.

#### Augmented Learning Loop

A mini AI-guided learning loop, for example:

1. Formulate a vague need.
2. First AI response.
3. Human reformulation.
4. AI refinement.
5. Document the process.

The team extracts a formal lesson (new pattern, architecture decision, example to keep).

#### Augmented Coaching

Technical or agile coaches can rely on AI to:

* rephrase technical points during reviews,
* suggest resources tailored to junior profiles,
* model different strategies for solving the same problem.

This accelerates skill growth without overloading the human transmission effort.

---

> **Prompt Book: A New Kind of Deliverable**
> 
> More and more teams document their LLM practices in a *prompt book* or *dialog-design notebook*: a structured collection of tested, annotated prompts tailored to their business context.
> This becomes **collective capital**, invaluable for onboarding, project memory, and upskilling.
