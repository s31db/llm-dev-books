
---
<a id="responsabilite"></a>
## ⚖️ Chapter 7 — Responsibility, Transparency, and Limits: An Ethics of Augmented Development

> Using an LLM in development isn’t just an opportunity. It’s also a responsibility.
> It’s not enough for the result to work. You must **be able to explain how it was produced and under what conditions.**

---

### 🧭 Why This Chapter?

In a context where:

* tools propose code with no clear author,
* teams integrate generated blocks they don’t fully understand,
* architecture decisions are made using AI suggestions,

**documenting interactions with LLMs** becomes a major issue. Not to record everything… but to **make visible what was generated, validated, interpreted.**

---

### 📘 Documenting LLM Use

#### Why Document?

* To keep a record of choices made with the help of AI.
* To avoid **generative debt**: code produced too fast without explanation.
* To be able to review a reasoning or prompt six months later.
* To equip reviewers and QA teams.

> Prompt documentation isn’t a luxury. It’s **a condition of maintainability.**

---

#### What to Document?

| Element                       | Purpose                                          |
|-------------------------------|--------------------------------------------------|
| **Source Prompt**             | Understand the initial intent                    |
| **LLM Version Used**          | Assess potential limits, bias, or hallucinations |
| **Generated Response**        | Archive the iteration used                       |
| **Human Validation Provided** | Identify the human role in accepting the result  |
| **Contextual Assumptions**    | Preserve the logic behind generation             |

---

#### Possible Formats

* Annotations in code comments
* History in the LLM tool (chat, snapshot, `.prompt.md` file)
* Separate documentation (Wiki, PR, `prompts/` folder)
* Structured model (e.g., Prompt Sheet + associated intent tests)

---

#### Concrete Example

> **Function generated from a GPT-4 prompt on 04/12/2025**
>
> Prompt: “Write a JavaScript function that validates an email address with a simple RegExp”
>
> Response modified to:
> – Add handling of special characters
> – Replace alert with explicit exception

---

### ⚖️ Ethical Issues and Responsibility

#### LLM = Shared Responsibility

> Just because an LLM proposed code doesn’t make you less responsible.
> You’re responsible **for what you understand, validate, and integrate.**

Models are powerful but:

* give no reliability guarantee,
* can reproduce bias,
* can generate non-compliant or legally risky content,
* aren’t capable of refusing an inappropriate task by themselves.

> **A Bug From a Convincing Example**
>
> A developer recently integrated an LLM-generated snippet for OAuth authentication. The code was syntactically perfect, commented, and seemed secure… except it used an obsolete, vulnerable library. Security audit revealed a critical flaw. The LLM had simply “copied” an old example without warning. Result: several days lost and a useful wake-up call.

---

<div class="pb-A4"></div>

#### Common Risks

| Risk                       | Example                                                          |
| -------------------------- | ---------------------------------------------------------------- |
| **Function Hallucination** | Plausible but non-existent function in a given language          |
| **Involuntary Copying**    | Reproducing protected code from the training corpus              |
| **Implicit Bias**          | Stereotypes in generated examples or answers                     |
| **Overconfidence**         | Decision-making without review or test, based on a single prompt |
| **Lack of Traceability**   | Generated code with no indication of origin or validation        |

---

#### Questions to Ask Yourself (Ethics Checklist)

1. Do I understand what the model produced?
2. Can I explain to someone why this solution is valid?
3. Have I tested or verified this code?
4. Have I indicated that it was generated?
5. Did the model produce a biased or questionable response?
6. Could this interaction be misinterpreted or misused by someone else?
7. Would I stand by this decision in production?

> If the answer is “no” to two or more questions, it’s **too soon to validate this AI contribution.**

---

### 🔍 Toward a Culture of Transparency

* Making LLM use visible isn’t a constraint. It’s **a lever for collective trust.**
* It allows re-reading, correction, and transmission.
* It provides **proof of technical diligence** in case of dispute or incident.
* It nurtures a team culture where AI **stimulates reasoning rather than replacing it.**

---

> **The “Dialogue Journal”**
>
> In a health-sector startup, every interaction with an LLM on critical topics (protocols, anonymization, security) is archived as a journal. This journal includes: initial prompt, iterations, chosen outcome, human evaluation, and decision justification. This setup improves internal transparency, eases audits, and fosters a reflective posture.

---

<div class="pb-A4"></div>

### 🔐 Protecting Data, Even in Dialogue

> *Everything you send to an LLM isn’t neutral — or invisible.*

Interactions with an LLM can unintentionally expose sensitive, confidential, or personal data: client names, proprietary code excerpts, production examples, or strategic decisions.

Even when the tool appears local or “secure,” it’s essential to adopt an active prudence:

* **Filter data upstream**, as you would before a public post.
* **Avoid blind copy-paste** from confidential documents or internal databases.
* **Use controlled environments** that guarantee data won’t be exploited (self-hosted LLMs, enterprise mode, explicit contractual clauses).
* **Anonymize data** used in prompts whenever possible.
* **Train teams** on the risks of unintentional information leakage through poorly crafted prompts.

Finally, ask yourself one simple question before sending:

> *“Would I be allowed to email this to an external third party?”*
> If the answer is no, the prompt needs to be reworked.

This focus on **data protection** fits into a broader ethics: that of **responsible, traceable development aware of its technical, social, and legal impacts.**

---

### ✏️ In Summary

* Documenting prompts and interactions is a **good technical practice** and an **ethical gesture.**
* LLMs shift responsibility but don’t dissolve it.
* Only a **transparent and shared practice** can ensure the quality, robustness, and ethics of AI-assisted designs.

> LLMs don’t think. They complete.
> But you do **think with them** — and that commits you.
