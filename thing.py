from ollama import Client

client = Client(host='http://127.0.0.82:3000/')
response = client.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
])
print(response)
