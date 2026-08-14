import json

with open('hasil diskusi/conversations.json', 'r', encoding='utf-8') as f:
    conversations = json.load(f)

conv = conversations[0]
messages = conv.get('chat_messages', [])

# Search for specific mentions of skills or prompt advice
keywords = ['level-layout-design', 'encounter-pacing', 'player-psychology-engagement', 'orchestration-protocol', 'pola b', 'qc-check']

for idx, msg in enumerate(messages):
    text = msg.get('text', '')
    for kw in keywords:
        if kw.lower() in text.lower():
            sender = msg.get('sender')
            print(f"--- Pesan #{idx+1} ({sender}) matches '{kw}' ---")
            # print snippet
            lines = [l for l in text.split('\n') if kw.lower() in l.lower() or 'skill' in l.lower()][:5]
            for l in lines:
                print("  ", l[:120])
