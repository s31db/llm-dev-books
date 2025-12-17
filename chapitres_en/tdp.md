
---
<a id="tdp"></a>
## 🧪 Annex 2 — **TDP: Test-Driven Prompting**

> What if we treated a **prompt** like a **test**?
> **Test-Driven Prompting** (TDP) applies the principles of TDD (Test-Driven Development) to working with LLMs: you **define the intent and success criteria first**, then draft the prompt, test it, and iterate.

---

### 🎯 Purpose

Structure your interactions with an LLM **in a rigorous and verifiable way**, by making explicit **what you expect** from an answer—before even writing the prompt.

---

### 💡 Augmented Professional Gesture

| Before (classic prompt) | With TDP |
|-------------------------|----------|
| Ask a question “on the fly” | Define intent and success criteria first |
| Fix the prompt after a failure | Anticipate test cases up front |
| React to answers as they come | Use an explicit evaluation and adjustment loop |
| Hard to share or build on later | Produce a testable, transferable, documentable artifact |

---

### 🧱 Anatomy of a TDP

1. **Intent** → What I want to produce, generate, or explore
2. **Success criteria** → What will make the answer usable or satisfactory
3. **Initial prompt** → First structured formulation
4. **Test cases** → Input/output data, expected formats, counter-examples
5. **Adjustment loop** → Revise the prompt based on observed gaps

---

<div class="pb-A4"></div>

### 🧪 Example TDP

> **Intent:** Generate a basic Node.js REST API with Express
>
> **Success criteria:**
> • Must include at least two routes
> • Use `express.json()`
> • Include a clean folder structure
>
> **Initial prompt:**
> “Create an Express REST API with two routes (GET/POST), using express.json() and a clean structure.”
>
> **Test cases:**
> • Presence of an `index.js` file with clear routes ✅
> • Usage of `express.json()` ✅
> • MVC structure ❌ → needs to be specified
>
> **Adjustment loop:**
> → Add to the prompt: “Organize the code following a simple MVC model.”

---

### 🧰 Tips and Tactics

* 🔍 **Write your test cases before the prompt**, as in TDD.
* 📎 **Save your TDPs** to replay, adapt, and share them.
* 💬 **Compare multiple prompts for the same intent**, keeping success criteria constant.
* 🧠 **Use motifs as test generators** (Counter-example, Mirror, etc.).
* 🧪 **Review cold**: revisit a TDP later to spot blind spots.

---

### 🧠 Associated Postures

| Posture               | What it activates in TDP                              |
|-----------------------|-------------------------------------------------------|
| **Prompt designer**   | Precisely formulates intent                           |
| **Critical explorer** | Probes the quality of the output with real-life cases |
| **Augmented editor**  | Fine-tunes wording to guide the model                 |
| **Rigorous curator**  | Captures and shares tested, effective prompts         |

---

<div class="pb-A4"></div>

### ⚠️ Watch-outs

* TDP **does not guarantee a perfect answer**, but it provides an iterative, clear, and shareable approach.
* Beware of **over-formalizing simple requests**: match the effort to the context.
* The opposite risk also exists: if a prompt is too vague, it will still be interpreted randomly.

---

### 🛠 Going Further

* Introduce TDPs into your **prompt reviews** or **team sessions**.
* Version your TDPs in a **project folder or knowledge base**.
* Use TDPs in training or pair-prompting as a **discussion tool for clarity**.

---

> **Test-Driven Prompting** means treating a prompt **like a test**: explicit, improvable, and action-oriented.
> A rigorous practice… for a smoother, more reliable dialogue with your LLM.
