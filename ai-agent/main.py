from commands import handle_command

print("🤖 PA Agent Started (type ‘exit’ to stop)\n")

while True:
    text = input("You: ")
    if text.lower() == "exit":
        print("Goodbye bro 👋")
        break

    response = handle_command(text)
    print("AI:", response)