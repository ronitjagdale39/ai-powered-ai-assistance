from agent import ask_ai
from datetime import datetime

def handle_command(text):


    text = text.lower()

    if "open chrome" in text:
        os.system("start chrome")
        return "Opening Chrome..."

    elif "open youtube" in text:
        os.system("start https://www.youtube.com")
        return "Opening YouTube..."

    elif "time" in text:
        return str(datetime.now())

    elif "search" in text:
        query = text.replace("search", "")
        os.system(f"start https://www.google.com/search?q={query}")
        return f"Searching for {query}"   

    else:
        return ask_ai(text)
