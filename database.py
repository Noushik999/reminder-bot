import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client["reminder_bot"]
reminders = db["reminders"]

def add_reminder(user_id, text, remind_time):
    reminders.insert_one({
        "user_id": user_id,
        "text": text,
        "remind_time": remind_time
    })

def get_due_reminders(current_time):
    return list(reminders.find({"remind_time": current_time}))

def delete_reminder(reminder_id):
    reminders.delete_one({"_id": reminder_id})
