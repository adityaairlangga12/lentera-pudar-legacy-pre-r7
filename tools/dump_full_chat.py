import json

with open('hasil diskusi/conversations.json', 'r', encoding='utf-8') as f:
    conversations = json.load(f)

conv = conversations[0]
messages = conv.get('chat_messages', [])

out_lines = [
    f"# Transkrip Lengkap: {conv.get('name')}",
    f"- **Created**: {conv.get('created_at')}",
    f"- **Updated**: {conv.get('updated_at')}",
    f"- **Total Messages**: {len(messages)}",
    "\n---\n"
]

for idx, msg in enumerate(messages):
    sender = msg.get('sender', 'unknown')
    text = msg.get('text', '')
    created = msg.get('created_at', '')
    
    sender_label = "👤 **USER**" if sender == 'human' else "🤖 **CLAUDE**"
    out_lines.append(f"### Pesan #{idx+1} — {sender_label} ({created})\n")
    out_lines.append(text)
    out_lines.append("\n---\n")

with open('hasil diskusi/full-transcript.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(out_lines))

print(f"Transcript exported successfully to hasil diskusi/full-transcript.md ({len(out_lines)} blocks)")
