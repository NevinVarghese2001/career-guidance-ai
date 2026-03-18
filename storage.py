import json
from datetime import datetime
import os

DATA_FILE = "data/responses.json"


def save_response(user_responses):
    """
    Save user responses with timestamp to a JSON file
    """
    entry = {
        "timestamp": datetime.now().isoformat(),
        "responses": user_responses
    }

    # Ensure data directory exists
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    # Append as a new line (JSON Lines format)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")