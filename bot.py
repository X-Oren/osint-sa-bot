import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "Welcome\n"
        "Salman osint 🥷🏻\n"
        "كيف اقدر اساعدك"
    )
    await update.message.reply_text(welcome_message)

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN environment variable is not set!")
        
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
