"""Module to load the data."""
# backend/config/data_loader.py

# ✅ Standard Library Imports
import json
import os
from pathlib import Path


def load_chatbot_data():
    try:
        data_file = Path(__file__).parent.parent / "data" / "kindly-bot.json"
        with open(data_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"Error loading chatbot data: {str(e)}")


chatbot_data = load_chatbot_data()
