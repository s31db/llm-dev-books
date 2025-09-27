
---
<a id="anatomie_prompt"></a>
## 🎯 Chapter 1 — Anatomy of a Good Prompt: Precision, Context, and Intention

> *A prompt isn’t a command. It’s a thinking interface. It frames the dialogue, steers the response, and conditions the quality of collaboration.*

### Why this chapter?

In any exchange with an LLM, **the prompt is the entry point**. It defines the task, the scope, and the level of detail you expect. But a good prompt is more than a well-worded question: it’s an act of design.
It combines three essential dimensions: **precision**, **context**, and **intention**.
It’s the interface between two intelligences — human and artificial.

This chapter offers a simple but robust framework for crafting prompts that are useful, actionable, and suited to real-world software development situations.

---

### Three Core Dimensions of an Effective Prompt

#### 1. **Precision: Clarify What You Expect**

A vague prompt produces a vague response.

> ❌ *“Give me some sorting code.”*
> ✅ *“Write a Python function that sorts a list of dictionaries by the key ‘date’ in descending order.”*

Be explicit. State the task, the level of detail, and the language.
Define the boundaries of the expected output.

#### 2. **Context: Provide What the Model Needs to Reason Well**

An LLM doesn’t know your project or constraints unless you tell it.

> *“I’m developing a REST API in Node.js in a microservices environment deployed via Docker.”*

Providing the right context enables a more targeted, relevant, realistic response.

<div class="pb-A4"></div>

#### 3. **Intention: Say Why You’re Asking**

The quality of the exchange depends on the clarity of your goal.

> *“I want even an intern to be able to run this script without risk of error.”*

Naming the intention guides the form, tone, and complexity level of the answer.

---

### 🗨️ A Prompt Is the Opening of a Conversation

It helps to see the prompt not as a one-off request but as the **first line of an exchange**. A good prompt **opens the space for dialogue** — it invites iteration, reformulation, and follow-up. It sets a frame but leaves room for co-construction.

---

### 🧭 Common Prompt Formats

Here are some frequent formats you’ll find in the pattern library (Chapter 4):

| Prompt Type              | Example                                                                          | Typical Use Case                        |
|--------------------------|----------------------------------------------------------------------------------|-----------------------------------------|
| **Context + Task**       | “In the context of an OAuth2 authentication service in Go, write a middleware…”  | Targeted implementation                 |
| **Example + Variation**  | “Here’s a JS function. Can you propose a faster version using `reduce`?”         | Refactor, optimization                  |
| **Roleplay**             | “Act as a senior Django expert. What steps would you take to refactor this app?” | Simulated expertise, specialized advice |
| **Step-by-Step**         | “Explain step by step how to secure an API against CSRF attacks.”                | Teaching, onboarding, training          |
| **Cascade**              | “Add an action tracing system to specific logs.”                                 | Implementation, refactor, optimization  |

---

<div class="pb-A4"></div>

### ✅ Best Practices

* Format prompts with **bullets, code blocks, or headings** to structure your thinking.
* Add **examples**: they guide the model and clarify expectations.
* Be explicit about:

  * the language and version used;
  * the style or level expected;
  * any specific constraints (technical, functional, organizational).

---

### ❌ Common mistakes to avoid

* Stacking several unrelated requests into one prompt.
* Using vague terms like “improve” or “make it cleaner” without criteria.
* Forgetting to state the real objective behind the task.

---

### 🧪 Comparative Example

#### Weak Prompt:

> *“Make me a Node API.”*

🔁 Result: generic, hardly usable response.

#### Improved Prompt:

> *“I want to create a REST API in Node.js with Express. It should manage users stored in MongoDB. I’d like a modular architecture, no ORM, with a clear separation of responsibilities. Can you propose a file structure and base code?”*

✅ Result: structured, contextualized, directly usable response.

---

### 🛠 Tool Sheet — Structure of a Good Prompt

| Element             | Example                                                          |
| ------------------- | ---------------------------------------------------------------- |
| **Context**         | “I’m working on a FastAPI app in Python deployed on AWS Lambda…” |
| **Clear Task**      | “I want a function that validates a JWT token in HTTP headers.”  |
| **Constraints**     | “No ORM, clear logs on failure, Python 3.10.”                    |
| **Intention**       | “The goal is for a junior developer to understand it.”           |
| **Expected Format** | “Commented example + unit tests.”                                |

---

<div class="pb-A4"></div>

### ✏️ In Short

A good prompt is:

* 🎯 a clear request,
* 🧱 explicit context,
* 🧠 a stated intention,
* 📦 a specified output format.

It’s the foundation of any fruitful collaboration with an LLM.

> *“It’s not the AI that’s fuzzy. It’s often how we talk to it.”* — ChatGPT
