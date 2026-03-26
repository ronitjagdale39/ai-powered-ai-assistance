from commands import handle_command
from voice import listen
from speaker import speak
import sys

def run_assistant():
    print("\n" + "="*40)
    print("🤖 AI ASSISTANT IS ONLINE")
    print("Commands: 'open [app]', 'exit' to quit")
    print("="*40 + "\n")

    while True:
        try:
            # Get input (currently voice.py's listen() just uses input())
            text = listen()

            if not text:
                continue

            if any(word in text for word in ["exit", "quit", "goodbye"]):
                farewell = "Goodbye! Have a great day."
                print(f"Assistant: {farewell}")
                speak(farewell)
                break

            # Process command
            response = handle_command(text)
            
            # Output response
            print(f"Assistant: {response}")
            speak(response)

        except KeyboardInterrupt:
            print("\nShutting down...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_assistant()