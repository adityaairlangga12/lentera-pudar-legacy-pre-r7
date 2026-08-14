import json
import sys

with open('hasil diskusi/conversations.json', 'r', encoding='utf-8') as f:
    conversations = json.load(f)

print(f"Total conversations found: {len(conversations)}")
for i, conv in enumerate(conversations):
    name = conv.get('name', 'Unnamed')
    created_at = conv.get('created_at', '')
    updated_at = conv.get('updated_at', '')
    msg_count = len(conv.get('chat_messages', []))
    print(f"[{i}] Title: {name} | Messages: {msg_count} | Created: {created_at} | Updated: {updated_at}")
