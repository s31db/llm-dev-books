
---

### 🟣 Pattern 1 — **Socratic Questioning**: *Reframe to Understand*

<p style="text-align: center;">
    <img src="../images/motif_socratique_en.png" width="50%" />
</p>

**🎯 Context**
A need is expressed vaguely, incompletely, or imprecisely — by you, a colleague, a client, or a user. You’re in a zone of uncertainty: the initial prompt isn’t sufficient to guide a useful answer. This can happen at the start of a project, during exploration, or in an interdisciplinary exchange.

**🚧 Problem**
A vague prompt generates a generic, stereotyped, or off-target answer. The LLM fills in the blanks with implicit assumptions — often different from your real intentions. That leads to lost time, poor direction, or the illusion of progress.

**✅ Solution**
Adopt a posture of **Socratic questioning**: ask **targeted, progressive, open questions** to clarify the real intention. You invite the model to help you **better formulate your own need**. By doing so, you explore the contours of the request before expecting a structured answer.

> Useful follow-up questions:
>
> * “What kinds of errors do you want to capture?”
> * “Who is the alert for?”
> * “What are the expected consequences of this action?”
> * “At what point in the process does this script run?”

<div class="pb-A4"></div>

**📌 Consequences**

* Clarifies the original intention, even for the human requester.
* Enriches the prompt as the dialogue unfolds.
* Triggers **shared reasoning** with the LLM.
* Reduces the risk of misdirection or over-generalization.
* Makes you more aware of your own implicit needs.

**💡 Example Use**
A developer sends the LLM:

> *“Create an alert script.”*

Response: too generic, not usable.

They follow up:

> *“This script should detect billing errors in CSV files. What kinds of errors can I monitor? Can you propose categories?”*

The LLM suggests:

* Inconsistent amounts
* Invalid dates
* Missing references
* Duplicates

From there, the developer reformulates a much more precise request:

> *“Generate a Python function that scans a folder of CSV files, detects the errors listed above, and sends a report by email at the end of processing.”*

This approach transforms a vague prompt into a **dialogued specification**.

**🌀 Useful Variants**

* **For framing a business need**:

  > “Can you ask me 5 questions to clarify what I want to do?”
* **For helping a PO or stakeholder**:

  > “Imagine I’m not sure what I want. Help me explore options based on my constraints.”

<div class="pb-A4"></div>

**🛠 Associated Tools**

* Roleplay mode: ask the LLM to act as a UX designer, an agile coach, or a product manager.
* Needs-clarification canvas (see Chapter 9).

**🧠 Recommended Posture**
Don’t look for an immediate answer. Look for the **next good question**. This pattern also turns you into a facilitator of your own clarity.

**💬 Prompt to Remember**

> *“Help me clarify my request by asking me questions. Don’t propose a solution yet.”*
