import json
from datetime import datetime

# Load existing memory
with open('memory.json', 'r', encoding='utf-8') as f:
    memory = json.load(f)

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

# Append and save
memory.append(new_entry)

with open('memory.json', 'w', encoding='utf-8') as f:
    json.dump(memory, f, indent=2)

print("✅ Memory entry added.")
