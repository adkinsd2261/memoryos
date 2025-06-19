import json
from datetime import datetime

# Define required fields
REQUIRED_FIELDS = [
    "topic", "type", "input", "output", "score", "maxScore",
    "timestamp", "success", "category", "reviewed"
]

# Load existing memory
with open('memory.json', 'r', encoding='utf-8') as f:
    try:
        memory = json.load(f)
        if not isinstance(memory, list):
            raise ValueError("memory.json must be a list.")
    except json.JSONDecodeError:
        print("❌ memory.json is invalid JSON.")
        exit(1)

# Example new entry
new_entry = {
    "topic": "Quick Test",
    "type": "SkillDrill",
    "input": "What is Javlin?",
    "output": "A lightweight memory engine using JSON + Markdown.",
    "score": 23,
    "maxScore": 25,
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "success": True,
    "category": "system-knowledge",
    "reviewed": False
}

# Validate new entry
missing = [f for f in REQUIRED_FIELDS if f not in new_entry]
if missing:
    print(f"❌ Missing fields: {missing}")
    exit(1)

# Append and save
memory.append(new_entry)

with open('memory.json', 'w', encoding='utf-8') as f:
    json.dump(memory, f, indent=2)

print("✅ Valid memory entry added.")

