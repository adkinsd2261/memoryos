# Javlin Memory Engine Specification (v0.1)

**Author**: Darryl Adkins  
**Date**: June 2025  
**Version**: 0.1  
**License**: MIT

---

## 📌 Purpose

The Javlin Memory Engine defines a lightweight, modular memory format for GPT-based agents.  
It enables persistent recall, context-aware behavior, and long-term skill growth — without vendor lock-in or backend complexity.

> Memory is structured in `.json`, instructions live in `.md`, and agents plug into both.

---

## 🧠 Core Concepts

- **`memory.json`**: Stores all memory data: prompts, timestamps, accuracy, scores, history.
- **`roles/*.md`**: Modular logic files defining behavior and tools of the GPT worker.
- **Agent shell**: Any GPT can act as a Javlin agent when loaded with a role and linked to memory.

---

## 📂 File System Structure

/memoryos
├── memory.json # Long-term memory file
├── roles/
│ └── example_role.md # GPT logic + instructions
├── memory_engine_spec.md # This spec file
├── roadmap.md # Development path
└── README.md # Project overview

pgsql
Copy
Edit

---

## 📑 memory.json Schema

```json
{
  "userId": "string",
  "memory": [
    {
      "topic": "Prompt Evaluation",
      "type": "SkillDrill",
      "input": "Rewrite this prompt to be more specific.",
      "output": "Rewritten prompt...",
      "score": 21,
      "maxScore": 25,
      "timestamp": "2025-06-20T00:00:00Z",
      "success": true,
      "category": "clarity",
      "reviewed": false
    }
  ],
  "meta": {
    "totalAttempts": 48,
    "avgScore7Days": 18.4,
    "streak": 4,
    "rank": "Student"
  }
}
🧩 Field Reference
Field	Purpose
topic	What domain this memory belongs to (e.g. “Prompt Evaluation”)
type	Activity type (e.g. SkillDrill, TrialSim)
input / output	What the user attempted and what the model responded with
score	Numerical result (1–25 scale or rubric)
timestamp	ISO datetime for session
success	Boolean for pass/fail or soft success
category	Skill area tied to result (e.g. "clarity")
reviewed	Mark if this memory has been reviewed

🔄 Memory Lifecycle
mermaid
Copy
Edit
graph TD;
    A[User starts session] --> B[Agent loads role.md]
    B --> C[Reads memory.json]
    C --> D[Selects relevant prior memories]
    D --> E[Guides session with memory context]
    E --> F[Writes new memory to file]
🌐 Compatibility
This system is:

LLM-agnostic (OpenAI, Claude, etc.)

Tool-free (no API needed to run)

Open-source (MIT License)

Human-editable (debuggable, auditable)

💡 Design Principles
Modularity – Agents are drop-in workers using a single .md file.

Clarity – JSON schema is intentionally minimal.

Durability – Files can be stored, forked, or versioned forever.

Transparency – Users can inspect, export, and adapt memory easily.

🚀 Example Agent Flow (ChatGPT shell)
User adds this to GPT config:

json
Copy
Edit
{
  "fileReferences": [
    "./roles/sensei.md",
    "./memory.json"
  ],
  "instructions": "Load the sensei role, check memory.json, coach the user, and update memory.json after each session."
}
📌 v0.1 Status
This spec is intended to:

Define the first open memory engine for GPT agents

Anchor Javlin’s ecosystem as a modular foundation

Support future hosted versions (v0.2+)

🛡️ License
This spec and the memoryos structure are released under the MIT License.
Use it. Fork it. Build something real.