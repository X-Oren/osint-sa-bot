import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك! بوت الأوسنت شغال وجاهز لأوامرك 🚀")

def main():
    token = os.getenv("BOT_TOKEN")
    application = Application.builder().token(token).build()
    
    # تسجيل أمر /start
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()

if __name__ == "__main__":
    main()
