import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from database import Database

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

db = Database()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "👋 Welcome to the Temasek Hall Dryer Bot!\n\n"
        "Commands:\n"
        "/join - Join a dryer queue\n"
        "/status - View current queue status"
    )
    await update.message.reply_text(message)

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Join Dryer 1", callback_data='join_1')],
        [InlineKeyboardButton("Join Dryer 2", callback_data='join_2')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select a dryer to join:", reply_markup=reply_markup)

async def handle_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    dryer_number = int(query.data.split('_')[1])
    user = query.from_user
    db.add_to_queue(user.id, user.username or user.first_name, dryer_number)
    await query.edit_message_text(f"✅ You have joined Dryer {dryer_number}'s queue.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = "📋 Dryer Queue Status:\n\n"
    for dryer_number in [1, 2]:
        queue = db.get_queue_info(dryer_number)
        message += f"Dryer {dryer_number}:\n"
        if not queue:
            message += "  ✅ Available\n"
        else:
            for i, user in enumerate(queue, 1):
                message += f"  {i}. {user.username}\n"
        message += "\n"
    await update.message.reply_text(message)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CallbackQueryHandler(handle_join, pattern='^join_'))
    app.run_polling()

if __name__ == "__main__":
    main()

