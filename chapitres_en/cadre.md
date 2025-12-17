
---
<a id="cadre"></a>
## 🔬 Chapter 9 — Implementation Frameworks: Workshops, Methods, and Rituals for an Augmented Practice

> Here’s the testing ground: formats for learning together, exploring, testing, documenting, and transmitting AI usage within your teams.

After exploring motifs, principles, and scenarios of augmented development, this chapter offers **concrete formats** to integrate these practices into the daily reality of teams. Workshops, rituals, canvases, serious games: the aim is to make the contributions of LLMs tangible within safe, learning-oriented collective dynamics.

---

### ✍️ 1. “Team Prompt Design” Workshop

> **Objective:** Learn to formulate, reformulate, and test prompts collectively in order to explore a real topic and improve the quality of interactions with LLMs.

---

**🕒 Duration:** 1h30 to 2h

**👥 Participants:** 3 to 6 people (developers, PO, UX, QA, facilitator…)

**🧰 Materials:** access to an LLM, prompt canvas (paper or Miro), space to visualize responses

---

**🔁 Typical Flow**

#### Introduction & Framing (10 min)

Present the workshop objective:
*“Explore collectively how to better formulate our prompts for a real case.”*

Briefly explain expected postures: openness, iteration, non-judgment

Choose a real topic or case together:

* module breakdown
* test formulation
* technical choice
* reframing a user need

---

#### Initial Prompt (15 min)

Write a **first naive prompt** together: “What would we ask an LLM in this context?”

<div class="pb-A4"></div>  

Read the generated response.

Identify potential problems:

* vagueness, ambiguities, imprecision
* terms too technical or undefined
* unspoken or implicit intention

---

#### Iterations & Reformulations (30–40 min)

Reformulate the prompt from different angles or strategies:

* explicit role (e.g., “You are a software architect…”)
* step by step
* structured version / bullet points
* critical / exploratory / generative version

For each version:

* LLM generates a response
* Quick discussion: how is it different? more useful? biased?

If useful: directly compare several formulations with the same model.

---

#### Extracting a Prompt Pattern (15–20 min)

From the tested versions, collectively formalize a **reusable prompt pattern**:

* base structure
* optional variants or modules
* conditions of use
* pitfalls to avoid

Document everything in a team canvas or library.

---

#### Retrospective & Learnings (10–15 min)

Quick roundtable:

* What I learned
* What I’ll reuse tomorrow
* What I’d still like to test

Possible decision:

* publish a cleaned-up version of the prompt
* test this prompt on other similar cases
* surface an **interaction motif** to add to the pattern language

---

<div class="pb-A4"></div>

> **🧠 Summary:**
>
> * Structuring workshop to build collective capacity for good formulation
> * Allows comparing, critiquing, and improving LLM interactions
> * Generates useful, reusable prompts adapted to the team

> ⚠️ **Pitfalls to Avoid:**
>
> * Focusing on “the” right answer instead of testing variations
> * Failing to name hidden intentions behind a prompt
> * Letting one person write while everyone else just watches

---

### 🗣️ 2. “Dialogue Daily” Ritual

> **Objective:** Establish a short, informal, regular ritual where each team member shares their most notable interactions with an LLM. Encourages collective learning, vigilance, and inspiration.

---

**🕒 Duration:** 5 to 10 minutes

**👥 Participants:** the whole team (dev, PO, UX, QA, facilitator…)

**📆 Frequency:** daily or twice-weekly (adapt to pace and usage)

**🧰 Optional Support:** prompt wall, dedicated Slack channel, shared board

---

**🔁 Typical Flow (per session)**

#### Introduction (1 min)

Short opening remark (facilitator or volunteer):
“What did AI teach us today?”

Remind the **3 guiding questions** (posted or verbal):

* **🧪 What did I try with an LLM?**
* **😲 What surprised, helped, or disappointed me?**
* **📌 What do I take away or want to try next?**

---

#### Spontaneous or Rotating Shares (5–8 min)

One to three people briefly share a notable interaction:

* success or failure
* interesting prompt
* observed bias
* strange or brilliant answer
* off-label LLM usage

Others can react, ask questions, or add anecdotes.

> 📍 *If no one shares spontaneously, draw a motif or “prompt of the day” card for inspiration.*

---

#### Closing & Capture (1–2 min)

Team chooses one or two points to **retain or capture**:

* Add a card to the “prompt grimoire”
* Note a frequent mistake or good practice
* Propose a test for the next sprint

Update the shared support:

* Experimentation dashboard
* Slack thread “#daily-llm”
* Miro/Notion logbook

---

> **🧠 Summary:**
>
> * Simple, lightweight ritual with no prep
> * Surfaces real usage, pitfalls, new ideas
> * Feeds ongoing team knowledge capture
> * Fosters a culture of experimentation and horizontal learning

> ⚠️ **Pitfalls to Avoid:**
>
> * Turning it into a static stand-up or forced roundtable
> * Slipping into judgment or competition over “best prompts”
> * Not connecting learnings to action (tests, documentation…)
> * Not planning a place to capture useful stories

---

### 🗺️ 3. “Dialogue Motif Mapping” Workshop

> **Objective:** Identify the most useful, frequent, or desirable LLM interaction motifs for the team and turn them into a shared base to guide future usage.

---

**🕒 Duration:** 1h30 to 2h

**👥 Participants:** 4 to 8 people (developers, PO, UX, testing, facilitators…)

**🧰 Materials:**

* Motif cards or sheets (from the book or local practices)
* Double-entry board (frequency / usefulness)
* Collection space (Miro, whiteboard, wiki…)

---

<div class="pb-A4"></div>

**🔁 Workshop Flow**

#### Introduction & Framing (10 min)

Remind what an **LLM interaction motif** is: a recurring form of use with intent, structure, and effect.
Why map them? *To orient, inspire, transmit, progress.*
Present the mapping support: a double-entry matrix *(X-axis: frequency of use; Y-axis: perceived usefulness)*

---

#### Re-activating Known Motifs (15 min)

Quick reading or visual presentation of 6–10 existing motifs.
For each motif:

* Team says if they know it
* If they’ve used it, and in what context

**Examples of motifs:**

Rephrasing a fuzzy idea
Generating test cases
Exploring architecture alternatives
Translating a business need into a user story
Step-by-step explanation of a behavior

---

#### Collective Mapping (30 min)

> Place motifs on the matrix in two steps.

**Individual or Pair Work (10 min)**
Each participant places motifs on the matrix according to:

* Frequency in their daily work
* Perceived usefulness

**Group Discussion (20 min)**

* Compare positions
* Consensus or dispersion: where is there agreement or divergence?
* Note open questions or underused motifs

---

<div class="pb-A4"></div>

#### Generating New Motifs (20 min)

From recent usage or “gaps” in the matrix:

* Which interaction types are missing from the map?
* What have we seen work but not yet formalized?

Each participant or sub-group sketches a **new motif** on a blank card:

* Intent
* Prompt structure
* Examples
* Limits or pitfalls

---

#### Consolidation & Capture (15 min)

* Gather all cards/motifs on a common support (wall, digital board)
* Suggest sorting or grouping by family: *exploration*, *reduction*, *control*, *creation*, etc.
* Agree on what to publish / share / test further

---

#### Bonus (optional)

* Give each motif an original name (“The Socratic Coach,” “The Clever Counter-Example,” etc.)
* Vote on motifs to formalize in the team library or repository

---

> **🧠 Summary:**
>
> * Creates a shared view of useful forms of dialogue with an LLM
> * Surfaces dominant usages… and blind spots
> * Gives a starting point for motifs to formalize or spread

> ⚠️ **Pitfalls to Avoid:**
>
> * Talking only about technical (or only functional) motifs
> * Underestimating postures (curiosity, prudence, critique…)
> * Reducing the map to a “best prompts” ranking
> * Underestimating the need for collective reformulation

---

<div class="pb-A4"></div>

### 🎲 4. The “Absurd Prompts” Game

> **Objective:** Experiment with the limits, paradoxes, hallucinations, and biases of language models — with humor and critical thinking.

---

**🕒 Duration:** 1h to 1h30

**👥 Participants:** 4 to 10 people

**🧰 Materials:** access to an LLM, sticky notes or shared board, capture tool (Miro, Notion, whiteboard…)

---

**🔁 Typical Flow**

#### Introduction (10 min)

* Present the goal of the workshop: *“Play with the limits to better understand them.”*
* Explain the rules: create absurd prompts, LLM answers seriously, then analyze.
* Remind expected postures: kindness, curiosity, constructive critique, no mocking people.

---

#### Group Warm-Up (10 min)

* Each participant invents an **absurd, contradictory, or vague prompt** (e.g., “Write a poem about a programming language that doesn’t exist but has bugs.”)
* Read a few examples aloud.
* Group picks 2–3 to submit to the LLM to start.

---

#### Prompt Creation & Selection (15–20 min)

Each person writes 2 prompts:

* one deliberately paradoxical or fallacious
* one inspired by an error or bad formulation already encountered

Pool them: participants read their proposals aloud.

Group selects 3–5 prompts to test based on:

* potential for derailment or surprise
* link to realistic professional situations

---

<div class="pb-A4"></div>

#### Dialogue With the LLM (20–30 min)

Submit prompts one by one to the LLM.
For each response:

* Collective reading
* Guided debrief:

  * What did the model attempt?
  * What does this reveal about its functioning?
  * Bug or over-obedience?
  * What risks if this response were taken seriously?

---

#### Collective Synthesis (15 min)

In group or pairs: what types of errors did we observe?

* Hallucinations?
* Absurd but credible answers?
* Blind obedience to incoherent orders?
* Lack of ethical or logical filter?

Capture on a shared board:

* “What this teaches me about LLMs”
* “What this teaches me about my formulation”

---

#### (Optional) Educational Variant

Create a “Fictional but Plausible Error” sheet:

* Initial prompt
* Absurd response
* Risk if taken seriously
* Good reflex for review or reformulation

---

> **🧠 Summary:**
>
> * Playful workshop to sharpen critical thinking
> * Lets you discuss LLM flaws without pressure
> * Builds a culture of doubt and reformulation in the team

> ⚠️ **Pitfalls to Avoid:**
>
> * Laughing at colleagues’ errors instead of analyzing formulations
> * Believing this game replaces serious testing practice
> * Forgetting to draw applicable lessons for real contexts

---

<div class="pb-A4"></div>

### 📘 5. “LLM Ready” Team Reference

> **Objective:** Co-create an LLM usage guide adapted to the team, grounded in real experience, needs, and collective learning.

---

**🕒 Duration:** 2h (can be split into 2 × 1h sessions)

**👥 Participants:** whole team or volunteer sub-group (4 to 8 people)

**🧰 Materials:**

* Miro / whiteboard or physical wall
* Access to an LLM interaction history (if available)
* Reference template (Notion, markdown, wiki…)

---

**🔁 Workshop Flow**

#### Introduction & Goals (10 min)

Why create a reference? *To capitalize, transmit, secure, save time*
Reminder: this is **not a fixed standard**, but an **evolving support**
Quick presentation of possible sections: prompt types, rules, pitfalls, validation levels…

---

#### Sharing Concrete Usages (20 min)

> Which LLM interactions were really helpful — or problematic?

Each person shares **1–2 notable examples** (successes or failures)
Quick writing in pairs or on sticky notes:

* Context
* Prompt
* Result
* Learning

Collectively classify into three columns:

* 🔁 To reproduce
* ⚠️ To adapt
* 🛑 To avoid

---

<div class="pb-A4"></div>

#### Building the Reference (45 min)

> Build sections from real stories.

##### **Prompt Types**

Extract reusable effective formulations
Organize by use: writing, code analysis, transformation, exploration…

##### **Response Quality Criteria**

Propose a **common grid**:

* Relevance
* Robustness
* Transparency
* Security
* Alignment with team standards

##### **Usage Rules**

Define clear, simple rules together:

* When to use an LLM
* When to validate with a human
* When to document the response

##### **Blacklist / Frequent Pitfalls**

Capture encountered errors: vague prompts, credible hallucinations, overconfidence, etc.

---

#### Formatting & Publishing (15 min)

Choose the publication format: Notion, README, Miro, Confluence page…
Assign roles:

* 1 reference steward
* 1–2 evolution keepers (e.g., sprint review, retro)

---

#### Retrospective & Commitment (10 min)

Roundtable:

* “What I learned”
* “What I want to test now”
* “What I’d like in the next version”

Reminder: a reference is **never finished**, it **co-evolves** with the team.

---

> **🧠 Summary:**
>
> * Structuring workshop to stabilize good AI practices in the team
> * Creates a useful, evolving, appropriated reference
> * Strengthens collective reflexivity and quality of usage

> ⚠️ **Pitfalls to Avoid:**
>
> * Writing a “theoretical” reference disconnected from real usage
> * Freezing it as a rigid standard
> * Letting it age without regular review (plan an update rhythm)

---

### Augmented Engineering Is Also Social Engineering

These formats show that augmented development isn’t just about tooling. It relies on:

* a culture of dialogue (with AI and between humans),
* the ability to make our reasoning explicit,
* a reflective practice that transforms the team as much as the deliverables.

> 🧵 **Key Takeaway:**
> This chapter is an open toolbox. Each proposed format can be adapted, combined, repurposed. What matters is not applying them “to the letter,” but making them your own to create your own paths toward an augmented, collective, and responsible coding practice.
