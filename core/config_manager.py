import os
import json
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        load_dotenv()
        self.data = {
            "elo": "Unranked",
            "squad_code": None,
            "consent": True,
            "level": 2 # Default N2
        }
        self.load_user_data()

    def is_first_run(self):
        return not os.path.exists("user_data.json")

    def load_user_data(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json", "r") as f:
                self.data.update(json.load(f))

    def save_user_data(self):
        with open("user_data.json", "w") as f:
            json.dump(self.data, f)
            
    def get_api_key(self, service):
        return os.getenv(f"{service}_API_KEY")