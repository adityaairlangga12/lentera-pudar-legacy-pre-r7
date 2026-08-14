import json

with open('hasil diskusi/conversations.json', 'r', encoding='utf-8') as f:
    conversations = json.load(f)

conv = conversations[0]
messages = conv.get('chat_messages', [])

target_messages = [18, 20, 22, 24, 28, 30, 32, 34, 36, 40, 48, 54, 60, 62, 64, 70, 72, 74, 76, 78, 80]

out = []
for idx in target_messages:
    if idx <= len(messages):
        msg = messages[idx-1]
        sender = msg.get('sender', '')
        text = msg.get('text', '')
        out.append(f"## Pesan #{idx} ({sender})\n\n{text}\n\n---\n")

with open('hasil diskusi/extracted-insights.md', 'w', encoding='utf-8') as f:
    f.write("\n".join(out))

print(f"Insights extracted to hasil diskusi/extracted-insights.md")
