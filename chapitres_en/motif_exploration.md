
---

### 🟣 Pattern 2 — **Guided Exploration**: *Break It Down to Move Forward*

<p style="text-align: center;">
    <img src="../images/motif_exploration.png" width="50%" />
</p>

**🎯 Context**
You’re approaching a subject that’s complex, new, or unclear — an architecture, an algorithm, a cross-cutting feature, an unfamiliar business domain. The task feels vast or shapeless. You sense you need a **plan of attack** to move step by step.

**🚧 Problem**
The initial prompt leads to a response that’s too broad, confused, or superficial. You get a generic explanation without prioritization or useful breakdown. The model tries to answer everything… but ends up solving nothing in a usable way. Result: cognitive overload, dispersion, wasted time.

**✅ Solution**
Use the LLM as a **structuring facilitator**. Ask it explicitly to propose a **progressive breakdown of the subject** into steps, categories, levels of analysis, or functional areas. You’re not asking for a solution yet, but for a **map of the territory**.

> Example prompts:
>
> * “What are the main steps to design this module?”
> * “Can you propose a phased implementation plan?”
> * “Break this problem down into technical subproblems.”
> * “Which business aspects should I explore first?”

**📌 Consequences**

**📌 Conséquences**

* Reduced perceived complexity.
* Better prioritization of tasks.
* A more iterative, incremental approach.
* Discovery of aspects not considered at first.
* Better alignment between technical and business concerns.

**💡 Example Use**
Two developers must create an invoice-processing module in an ERP.
Initial prompt:

> *“How should we design this module?”*

Response: long, dense, hard to use.
They rephrase:

> *“Can you propose a functional and technical breakdown for building this module?”*

The LLM replies:

1. Identify data sources (clients, vendors).
2. Define business validation rules.
3. Structure processing statuses.
4. Integrate notifications.
5. Handle error cases.
6. Plan accounting exports.

The breakdown becomes the basis for a backlog, an MVP plan, and a structured dialogue with the Product Owner. The LLM acts here as a **progress mediator**.

**🌀 Useful Variants**

* **Funnel exploration**: ask for a general plan → zoom in on one step → detail each sub-step.
* **Multi-angle exploration**: ask for a breakdown by role (technical, business, UX), or by different priorities (cost, impact, risk).
* **Critical exploration**: ask for the riskiest steps or those that deserve a proof of concept.

**🛠 Associated Tools**

* Implementation-plan templates (RICE, MoSCoW).
* Mind maps generated from the answer (via a visual tool).
* Using the LLM as a *Project Planner* or *conversational architect*.

**🧠 Recommended Posture**
Accept **not trying to solve everything at once**. Use the LLM to **orchestrate a progression**: map before you code. You become a facilitator of focus rather than a seeker of instant solutions.

**💬 Prompt to Remember**

> *“I’m working on \[topic]. Propose a breakdown into concrete, progressive steps to help me structure my approach.”*
