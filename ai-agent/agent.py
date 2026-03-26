import requests
import os
chat_history = []

def ask_ai(prompt):
    global chat_history
    
    chat_history.append({"role": "user", "content": prompt})
    
    full_prompt = ""
    for msg in chat_history:
        full_prompt += f"{msg['role']}: {msg['content']}\n"
    
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    result = response.json()

    reply = result.get("response", "No response")
    
    chat_history.append({"role": "assistant", "content": reply})

    return reply


if __name__ == "__main__":
    while True:
        user_input = input(">> ")
        print(handle_command(user_input))