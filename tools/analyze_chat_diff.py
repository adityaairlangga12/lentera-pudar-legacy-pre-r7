import json

with open('hasil diskusi/conversations.json', 'r', encoding='utf-8') as f:
    conversations = json.load(f)

conv = conversations[0]
messages = conv.get('chat_messages', [])

print(f"Total messages: {len(messages)}")

topics = []
for i in range(0, len(messages), 2):
    user_msg = messages[i].get('text', '') if i < len(messages) else ''
    asst_msg = messages[i+1].get('text', '') if i+1 < len(messages) else ''
    
    # summarize first line or intent
    user_first_line = user_msg.strip().split('\n')[0][:100]
    print(f"Turn {i//2 + 1}: User: {user_first_line}")
