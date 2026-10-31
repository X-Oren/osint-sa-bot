import os
from telegram.ext import Application

TOKEN = os.getenv("BOT_TOKEN")

def main():
    application = Application.builder().token(TOKEN).build()
    application.run_polling()

if __name__ == "__main__":
    main()
