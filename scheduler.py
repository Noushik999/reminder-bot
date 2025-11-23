from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from database import get_due_reminders, delete_reminder

def start_scheduler(bot):
    scheduler = BackgroundScheduler()

    @scheduler.scheduled_job("interval", seconds=30)
    def check_reminders():
        now = datetime.utcnow().replace(second=0, microsecond=0)
        due = get_due_reminders(now)

        for r in due:
            bot.send_message(
                chat_id=r["user_id"],
                text=f"⏰ Reminder: {r['text']}"
            )
            delete_reminder(r["_id"])

    scheduler.start()
