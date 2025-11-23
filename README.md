# ⏰ Telegram Reminder Bot

A simple, clean, and cloud-powered **Telegram Reminder Bot** built with:
- **python-telegram-bot**
- **MongoDB Atlas**
- **APScheduler**
- **Render.com** (for hosting)

This bot lets you set reminders like:

/remind 10m Drink water
/remind 1h Meeting at 3

The bot stores reminders in MongoDB and automatically sends them when the time comes.

---

## 🚀 Features
- `/start` — Shows bot instructions  
- `/remind <time> <task>` — Set reminders  
- Supports `m` (minutes), `h` (hours), `s` (seconds)  
- Background scheduler  
- Cloud database  
- Fully deployable  

---

## 📦 Installation

1. Clone the repo:
git clone https://github.com/Noushik999/reminder-bot
cd reminder-bot

2. Install dependencies:
pip install -r requirements.txt

3. Create a `.env` file:
BOT_TOKEN=1234567890:ABCDefGhIjkLmNoPQrsTuvWxYZ12345678
MONGO_URL=mongodb+srv://<username>:<password>@cluster0.akj23.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

---

## ▶️ Running Locally

Start the bot:
python main.py

---

## ☁️ Deployment (Render)

1. Go to **https://render.com**  
2. Create a **New Web Service**  
3. Connect your GitHub repo  
4. Choose:
   - Runtime: **Python**  
   - Start command:
python main.py
5. Add environment variables:
   - `BOT_TOKEN`
   - `MONGO_URL`

6. Deploy 🎉  

---

## 🤝 Contributing
Pull requests are welcome!  

---

## ⭐ Support
If you like this project, star the repo ✨  

