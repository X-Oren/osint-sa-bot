import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "⚡️ **Welcome**\n"
        "🔒 **salman osint كيف اقدر اساعدك** 🥷🏻"
    )
    
    # الأزرار التفاعلية برموز فخمة ومميزة
    keyboard = [
        [InlineKeyboardButton("📸 Google Images (بحث الصور الذكي)", callback_data="tool_google")],
        [InlineKeyboardButton("🌐 OSINT Framework (دليل المصادر)", callback_data="tool_framework")],
        [InlineKeyboardButton("🚗 CarID (استعلام المركبات)", callback_data="tool_carid")],
        [InlineKeyboardButton("📲 التواصل الاجتماعي مع المبرمج", callback_data="social_links")],
        [InlineKeyboardButton("⏳ باقي تطويرات على البوت قريباً", callback_data="coming_soon")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "tool_google":
        text = (
            "🎯 **Google Images (Reverse Image Search)**\n\n"
            "🔍 **الفايدة في الأوسنت:** تُعتبر من أهم أدوات التحقيق للبحث العكسي عن الصور.\n"
            "💡 **دورها الأمني:** تساعد في تتبع مصدر الصور، معرفة متى وأين نشرت لأول مرة، كشف الحسابات الوهمية، وتحليل المواقع الجغرافية من خلال معالم الصور."
        )
        # زر يفتح الرابط مباشرة مع زر الرجوع أو رسالة توضيحية
        keyboard = [[InlineKeyboardButton("🔗 فتح الموقع", url="https://images.google.com/")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif query.data == "tool_framework":
        text = (
            "🌐 **OSINT Framework**\n\n"
            "🎯 **الفايدة في الأوسنت:** المرجع الأساسي والأشهر لكل محقق أمني ومختص استخبارات مصادر مفتوحة.\n"
            "💡 **دورها الأمني:** عبارة عن شجرة تفاعلية ضخمة تضم مئات الأدوات والمواقع المجانية لجمع المعلومات عن الأشخاص، الشركات، النطاقات، وشبكات التواصل."
        )
        keyboard = [[InlineKeyboardButton("🔗 فتح الموقع", url="https://osintframework.com/")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif query.data == "tool_carid":
        text = (
            "🚗 **CarID Database**\n\n"
            "🎯 **الفايدة في الأوسنت:** قاعدة بيانات متكاملة لقطع غيار وتفاصيل المركبات.\n"
            "💡 **دورها الأمني:** تفيد محققي الـ OSINT في تحليل بيانات السيارات، معرفة مواصفاتها الدقيقة، أرقام القطع، وتتبع طرازات المركبات أثناء التحقيقات الاستخباراتية المرשدة."
        )
        keyboard = [[InlineKeyboardButton("🔗 فتح الموقع", url="https://www.carid.com/")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif query.data == "social_links":
        developer_info = (
            "👨‍💻 **معلومات المبرمج:**\n\n"
            "🇸🇦 **Salman Alanzi**\n"
            "👻 **Snapchat:** `@ele-99`\n"
            "✈️ **Telegram:** `@u3clz`"
        )
        await query.message.reply_text(developer_info, parse_mode="Markdown")
        
    elif query.data == "coming_soon":
        await query.message.reply_text("⏳ **جاري العمل على إضافة أدوات استخباراتية وسيبرانية متقدمة قريباً، خليك قريب!** 🚀", parse_mode="Markdown")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN environment variable is not set!")
        
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
  
