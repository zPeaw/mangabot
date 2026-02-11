import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
USER_ID = int(os.getenv("USER_ID", "0"))

CHECK_INTERVAL = 86400  
CLEAN_INTERVAL = 1000

URL = "https://lgbtics.com/"

DATA_FOLDER = "data"
SENT_FILE = os.path.join(DATA_FOLDER, "sent_messages.json")
KNOWN_FILE = os.path.join(DATA_FOLDER, "known.json")
