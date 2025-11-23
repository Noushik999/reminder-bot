import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime, timedelta
from dotenv import load_dotenv
from database import add_reminder
from scheduler import start_scheduler

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

def parse_time(duration):
    num = int(duration[:-1])
    unit = duration[-1]

    if unit == "m":
        return timedelta(minutes=num)
    if unit == "h":
        return timedelta(hours=num)
    if unit == "s":
        return timedelta(seconds=num)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey! Send reminders like:\n\n"
        "`/remind 10m Drink water`\n"
        "`/remind 1h Meeting`\n",
        parse_mode="Markdown"
    )

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("Usage: /remind 10m Drink water")
        return

    duration = context.args[0]
    text = " ".join(context.args[1:])
    delta = parse_time(duration)

    remind_time = datetime.utcnow().replace(second=0, microsecond=0) + delta

    add_reminder(update.effective_chat.id, text, remind_time)

    await update.message.reply_text(
        f"⏳ Reminder set for {duration} from now!"
    )

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", remind))

    start_scheduler(app.bot)

    print("Bot running...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
