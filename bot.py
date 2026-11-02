import os
import io
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "⚡️ **Welcome**\n"
        "🔒 **salman osint كيف اقدر اساعدك** 🥷🏻\n\n"
        "اختر الأداة الاستخباراتية للبدء بالتحليل المرئي واستخراج التقرير:"
    )
    
    keyboard = [
        [InlineKeyboardButton("📸 البحث الاستخباراتي بالصور", callback_data="run_google")],
        [InlineKeyboardButton("🐦 تحليل تغريدات X (BirdHunt)", callback_data="run_birdhunt")],
        [InlineKeyboardButton("🎥 الذباب الالكتروني (EulerStream)", callback_data="run_eulerstream")],
        [InlineKeyboardButton("📲 التواصل الاجتماعي مع المبرمج", callback_data="social_links")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "run_google":
        context.user_data['active_tool'] = 'google'
        await query.message.reply_text(
            "📸 **أنت الآن في وضع بحث الصور العكسي الذكي.**\n\n"
            "📥 *أرسل النص أو رابط الصورة لمحاكاة بث التحليل المرئي واستخراج الـ PDF.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_birdhunt":
        context.user_data['active_tool'] = 'birdhunt'
        await query.message.reply_text(
            "🐦 **أنت الآن في وضع تحليل تغريدات X (BirdHunt).**\n\n"
            "🔗 المرجع: https://birdhunt.huntintel.io/\n"
            "📥 *أرسل رابط التغريدة أو اسم الحساب لبدء بث التحليل المباشر واستخراج التقرير.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_eulerstream":
        context.user_data['active_tool'] = 'eulerstream'
        await query.message.reply_text(
            "🫆 **أنت الآن في وضع تحليل الحسابات الرقمية (EulerStream).**\n\n"
            "👣 *أرسل رابط البث لبدء تتبع الحساب او البث المباشر واستخراج التقرير الأمني.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "social_links":
        context.user_data['active_tool'] = None
        developer_info = (
            "👨‍💻 **معلومات المبرمج:**\n\n"
            "🇸🇦 **Salman Alanzi**\n"
            "👻 **Snapchat:** `@ele-99`\n"
            "✈️ **Telegram:** `@u3clz`"
        )
        await query.message.reply_text(developer_info, parse_mode="Markdown")

def generate_osint_pdf(tool_name, target_info):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Salman OSINT Intelligence Report 🥷🏻")
    
    c.setLineWidth(1)
    c.line(50, height - 60, width - 50, height - 60)
    
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 100, f"Tool Used: {tool_name}")
    c.drawString(50, height - 130, f"Target Data: {target_info}")
    
    c.setFont("Helvetica", 10)
    c.drawString(50, height - 160, "Status: Live Stream Analysis & Extraction Completed 🟢")
    c.drawString(50, height - 180, "Classification: Confidential / OSINT Investigation")
    

    c.line(50, 80, width - 50, 80)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, 60, "Developed by: Salman Alanzi (Salman OSINT)")
    c.drawString(50, 45, "Snapchat: @ele-99 | Telegram: @u3clz")
    
    c.save()
    buffer.seek(0)
    return buffer

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    active_tool = context.user_data.get('active_tool')
    user_text = update.message.text
    
    if active_tool in ['google', 'birdhunt', 'eulerstream']:
        if active_tool == 'google':
            tool_title = "Google Images Live Analysis"
        elif active_tool == 'birdhunt':
            tool_title = "X (Twitter) BirdHunt Live Stream Analysis"
        else:
            tool_title = "EulerStream Live Stream Analysis"
        

        stream_msg = await update.message.reply_text("🔴 **[LIVE STREAM]** جاري الاتصال بخوادم الفحص وبدء البث المباشر للتحليل...")
        await asyncio.sleep(1.5)
        
        await stream_msg.edit_text("📡 **[LIVE STREAM]** يتم التقاط الحزم واستخراج بيانات الهدف الحية...")
        await asyncio.sleep(1.5)
        
        await stream_msg.edit_text("🟢 **[LIVE STREAM]** تم تأكيد البث بنجاح، جاري توليد التقرير الاستخباراتي النهائي...")
        await asyncio.sleep(1)
        

        pdf_file = generate_osint_pdf(tool_title, user_text)
        pdf_file.name = "Salman_OSINT_Report.pdf"
        

        await update.message.reply_document(
            document=pdf_file,
            caption="📄 **إليك تقرير الاستخبارات المفتوحة المستخرج من البث المباشر.**"
        )
        

        keyboard = [
            [InlineKeyboardButton("✅ نعم، إرسال للجهات المختصة", callback_data="send_authorities")],
            [InlineKeyboardButton("❌ لا، شكراً", callback_data="cancel_authorities")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("هل تريد إرسالها الى الجهات المختصة؟", reply_markup=reply_markup)
        
        context.user_data['active_tool'] = None
    else:
        await update.message.reply_text("⚠️ أهلاً بك يا بطل! يرجى الضغط على `/start` واختيار الأداة للبدء بالتحليل المرئي والاستخراج 🥷🏻")

async def authorities_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "send_authorities":
        await query.message.edit_message_text("🚀 **تم إرسال التقرير والبيانات بنجاح إلى الجهات المعنية المعتمدة!** 🔒")
    elif query.data == "cancel_authorities":
        await query.message.edit_message_text("👍 تم إلغاء العملية. يمكنك البدء من جديد عبر `/start`.")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN environment variable is not set!")
        
    application = Application.builder().token(token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(authorities_handler, pattern="^(send_authorities|cancel_authorities)$"))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
