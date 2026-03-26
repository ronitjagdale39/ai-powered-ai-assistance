import os
import re
from agent import ask_ai

# Mapping of common names to official macOS application names
APP_MAPPING = {
    "chrome": "Google Chrome",
    "browser": "Safari",
    "safari": "Safari",
    "notes": "Notes",
    "music": "Music",
    "calculator": "Calculator",
    "terminal": "Terminal",
    "code": "Visual Studio Code",
    "vs code": "Visual Studio Code",
    "slack": "Slack",
    "discord": "Discord",
    "spotify": "Spotify",
    "finder": "Finder",
    "mail": "Mail",
    "calendar": "Calendar",
}

def handle_command(text):
    text = text.lower().strip()

    # Regex to catch "open [app]" or "please open [app]" or "can you open [app]"
    open_match = re.search(r'(?:open|launch|start)\s+(.+)', text)
    
    if open_match:
        app_query = open_match.group(1).strip()
        
        # Check mapping first
        app_name = APP_MAPPING.get(app_query, app_query)
        
        try:
            # -a flag ensures it opens the specific application
            exit_code = os.system(f'open -a "{app_name}"')
            if exit_code == 0:
                return f"🚀 Opening {app_name}..."
            else:
                return f"❌ Failed to open {app_name}. Make sure it's installed."
        except Exception as e:
            return f"⚠️ Error trying to open {app_name}: {str(e)}"

    # 🤖 AI fallback
    return ask_ai(text)
