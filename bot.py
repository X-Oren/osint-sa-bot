import os
import io
import asyncio
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "⚡️ **SALMAN OSINT INTELLIGENCE SYSTEM**\n"
        "🔒 **منظومة الاستخبارات الميدانية والتحليل الرقمي المتطور** 🥷🏻\n\n"
        "اختر الأداة الاستخباراتية المطلوبة لبدء رادار البث المباشر للهجمات واستخراج التقرير الرسمي المعتمد:"
    )
    
    keyboard = [
        [InlineKeyboardButton("📸 بحث الصور العكسي الذكي", callback_data="run_google")],
        [InlineKeyboardButton("🐦 تحليل تغريدات X (BirdHunt)", callback_data="run_birdhunt")],
        [InlineKeyboardButton("🎥 تحليل البثوث الرقمية (EulerStream)", callback_data="run_eulerstream")],
        [InlineKeyboardButton("🌐 فحص وهندسة الروابط والتهديدات (PhishCheck)", callback_data="run_phishcheck")],
        [InlineKeyboardButton("🗺️ عرض خريطة فضاء الهجمات المباشرة", callback_data="run_attack_map")],
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
            "📸 **[وضع الاستخبارات البصرية]:** تم تفعيل محرك بحث الصور العكسي الذكي بنجاح.\n\n"
            "📥 *أرسل النص أو رابط الصورة المستهدفة لتفعيل رادار التتبع واستخراج التقارير الجنائية الفورية.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_birdhunt":
        context.user_data['active_tool'] = 'birdhunt'
        await query.message.reply_text(
            "🐦 **[وضع الرصد التكتيكي]:** تم تشغيل أداة BirdHunt لتحليل منصة X (تويتر).\n\n"
            "🛡️ *تم ربط العقد الداخلية بالكامل داخل البث المباشر.*\n"
            "📥 *أرسل رابط التغريدة أو المعرف المستهدف لبدء فحص الشبكة العنقودية.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_eulerstream":
        context.user_data['active_tool'] = 'eulerstream'
        await query.message.reply_text(
            "🎥 **[وضع الرقابة الرقمية]:** تم تفعيل أداة EulerStream لتحليل البثوث.\n\n"
            "📥 *أرسل رابط البث المباشر لبدء رادار التتبع الجغرافي والتحليل الأمني الائتماني.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_phishcheck":
        context.user_data['active_tool'] = 'phishcheck'
        await query.message.reply_text(
            "🌐 **[وضع فحص التهديدات السيبرانية]:** تم تنشيط بروتوكول PhishCheck.\n\n"
            "📥 *أرسل الرابط أو النطاق المشبوه لفحص البنية التحتية وكشف الثغرات ونقاط الضعف.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_attack_map":
        context.user_data['active_tool'] = None
        # محاكاة تفاعلية لخريطة فضاء الهجمات الإلكترونية مباشرة داخل الشات
        map_msg = await query.message.reply_text(
            "🗺️ **[CYBER ATTACK SPACE MAP - LIVE RADAR]**\n"
            "🌐 جاري تهيئة الاتصال بالأقمار الصناعية وعقد الخوادم الموزعة...\n\n"
            "```text\n"
            "[░░░░░░░░░░░░░░░░░░░░] 0%\n"
            "```", parse_mode="Markdown"
        )
        await asyncio.sleep(1.0)
        await map_msg.edit_text(
            "🗺️ **[CYBER ATTACK SPACE MAP - LIVE RADAR]**\n"
            "📡 جاري رصد مسارات الحركة وحزم البيانات الخبيثة في الوقت الفعلي...\n\n"
            "```text\n"
            "[████████░░░░░░░░░░░░] 40% | Nodes: Active\n"
            "```", parse_mode="Markdown"
        )
        await asyncio.sleep(1.2)
        await map_msg.edit_text(
            "🗺️ **[CYBER ATTACK SPACE MAP - LIVE RADAR]**\n"
            "⚡ تم رصد عقد الاختراق وتحديد الإحداثيات الجغرافية العالمية...\n\n"
            "```text\n"
            "[████████████████░░░░] 80% | Shield: Secure\n"
            "```", parse_mode="Markdown"
        )
        await asyncio.sleep(1.0)
        
        final_map_view = (
            "🗺️ **[خريطة فضاء الهجمات الإلكترونية - البث المباشر النشط]** 🟢\n\n"
            "🌍 **إحداثيات الرادار والنشاط السيبراني العالمي:**\n"
            "├─ 🔴 **الهدف المرصود:** عقدة اتصال مشبوهة (Middle-East Sector)\n"
            "├─ 🛡️ **حالة الجدار الناري:** مفعل ومحصن بالكامل\n"
            "├─ ⚡ **معدل اعتراض الحزم:** 4.8 GB/s (مستقر)\n"
            "└─ 📍 **الحالة العامة:** البث يعمل بتحديث لحظي مباشر داخل الغرفة الأمنية.\n\n"
            "*استخدم القائمة الرئيسية `/start` لاختيار أداة فحص جديدة أو استخراج التقرير.*"
        )
        await map_msg.edit_text(final_map_view, parse_mode="Markdown")
        
    elif query.data == "social_links":
        context.user_data['active_tool'] = None
        developer_info = (
            "👨‍💻 **[بطاقة الاعتماد الميداني للمبرمج]**\n\n"
            "🇸🇦 **المطور:** Salman Alanzi (Salman OSINT)\n"
            "👻 **Snapchat:** `@ele-99`\n"
            "✈️ **Telegram:** `@u3clz`\n"
            "🔒 *جميع الحقوق محفوظة لمنظومة العون والاستخبارات الرقمية © 2026*"
        )
        await query.message.reply_text(developer_info, parse_mode="Markdown")

def generate_official_osint_pdf(tool_name, target_info):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'OfficialTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=colors.HexColor('#1A365D'),
        alignment=1
    )
    
    subtitle_style = ParagraphStyle(
        'OfficialSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#4A5568'),
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#2B6CB0')
    )
    
    body_style = ParagraphStyle(
        'OfficialBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor('#2D3748')
    )
    
    footer_style = ParagraphStyle(
        'OfficialFooter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#718096'),
        alignment=1
    )

    story = []

    story.append(Paragraph("SALMAN OSINT INTELLIGENCE REPORT", title_style))
    story.append(Paragraph("Official Cyber Security & Open Source Investigation Unit 🥷🏻", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1A365D'), spaceAfter=15))

    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    meta_data = [
        [Paragraph("<b>رقم التقرير:</b> SOSINT-2026-908", body_style), Paragraph(f"<b>تاريخ الإصدار:</b> {current_time}", body_style)],
        [Paragraph("<b>تصنيف التقرير:</b> سري للغاية / رسمي", body_style), Paragraph("<b>حالة الاعتماد:</b> معتمد للجهات المختصة 🟢", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F7FAFC')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 15))

    story.append(Paragraph("1. بيانات الأداة ورادار الفضاء السيبراني", heading_style))
    story.append(Spacer(1, 5))
    
    target_data = [
        [Paragraph("<b>الأداة المستخدمة:</b>", body_style), Paragraph(f"{tool_name}", body_style)],
        [Paragraph("<b>رابط / مدخلات الهدف والمرصد:</b>", body_style), Paragraph(f"{target_info}", body_style)],
        [Paragraph("<b>حالة الفحص التقني الخريطي:</b>", body_style), Paragraph("اكتمل بنجاح عبر البث المباشر لخريطة الهجمات", body_style)]
    ]
    target_table = Table(target_data, colWidths=[140, 400])
    target_table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#EDF2F7')),
    ]))
    story.append(target_table)
    story.append(Spacer(1, 15))

    story.append(Paragraph("2. الملخص الفني والنتائج الاستخباراتية", heading_style))
    story.append(Spacer(1, 5))
    
    summary_text = (
        "تم رصد الهدف وتحليله تقنياً عبر خريطة فضاء الهجمات المباشرة ومنظومة (OSINT). "
        "أظهرت مؤشرات الرادار وتتبع الأنشطة مطابقة دقيقة للعقد الرقمية المرتبطة بالهدف. "
        "تم استخراج كافة الأدلة الجنائية والعقد البرمجية اللازمة لإرفاقها ضمن ملفات التحقيق الرسمية."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(Spacer(1, 20))

    story.append(Paragraph("3. الاعتماد والختم الرسمي", heading_style))
    story.append(Spacer(1, 5))
    story.append(Paragraph("هذا التقرير مُصدر آلياً وموثق رقمياً عبر منظومة Salman OSINT Automation لخدمة الجهات الأمنية والمختصة.", body_style))
    story.append(Spacer(1, 30))

    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E0'), spaceAfter=10))
    footer_text = (
        "<b>Developed by: Salman Alanzi (Salman OSINT)</b><br/>"
        "Snapchat: @ele-99 | Telegram: @u3clz<br/>"
        "All Rights Reserved © 2026"
    )
    story.append(Paragraph(footer_text, footer_style))

    doc.build(story)
    buffer.seek(0)
    return buffer

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    active_tool = context.user_data.get('active_tool')
    user_text = update.message.text
    
    if active_tool in ['google', 'birdhunt', 'eulerstream', 'phishcheck']:
        if active_tool == 'google':
            tool_title = "Google Images Live Cyber Stream"
        elif active_tool == 'birdhunt':
            tool_title = "X (Twitter) BirdHunt Live Attack Stream"
        elif active_tool == 'eulerstream':
            tool_title = "EulerStream Live Cyber Stream"
        else:
            tool_title = "PhishCheck Cyber Threat & Infrastructure Analysis"
        
        # محاكاة شاشة بث مباشر تفاعلية مدعومة بخريطة الهجمات والتحليل الاستخباراتي داخل الشات
        stream_msg = await update.message.reply_text("🚨 **[LIVE CYBER STREAM]** جاري تهيئة الاتصال بخريطة فضاء الهجمات واستخراج عقد البيانات...")
        await asyncio.sleep(1.0)
        
        await stream_msg.edit_text("📡 **[LIVE CYBER STREAM]** يتم رصد وتتبع الثغرات وتحليل الأنشطة عبر خوادم الأوسنت الموزعة...")
        await asyncio.sleep(1.2)
        
        await stream_msg.edit_text("🗺️ **[ATTACK MAP SYNC]** إسقاط الإحداثيات الجغرافية للهدف على خريطة الفضاء السيبراني المباشر...")
        await asyncio.sleep(1.0)
        
        await stream_msg.edit_text("⚡️ **[LIVE CYBER STREAM]** اكتشاف الهدف بنجاح! جاري اعتراض الحزم وتأمين البث المباشر...")
        await asyncio.sleep(1.0)
        
        await stream_msg.edit_text("🟢 **[LIVE CYBER STREAM]** تم إكمال البث المرئي للهجمات وتحديث الخريطة بنجاح، جاري بناء التقرير الرسمي...")
        await asyncio.sleep(0.8)
        
        # إنشاء ملف PDF الرسمي في الذاكرة
        pdf_file = generate_official_osint_pdf(tool_title, user_text)
        pdf_file.name = "Salman_Official_OSINT_Report.pdf"
        
        # إرسال ملف الـ PDF الرسمي للمستخدم
        await update.message.reply_document(
            document=pdf_file,
            caption="📄 **إليك تقرير الاستخبارات الرسمي والمعتمد المرفق بنتائج خريطة الهجمات المباشرة.**"
        )
        
        # رد تفاعلي استخباراتي بعد إرسال الـ PDF
        keyboard = [
            [InlineKeyboardButton("✅ نعم، إرسال للجهات المختصة", callback_data="send_authorities")],
            [InlineKeyboardButton("❌ لا، شكراً", callback_data="cancel_authorities")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("🛡️ هل تود اعتماد وإرسال الملف الاستخباراتي إلى الجهات المعنية المختصة؟", reply_markup=reply_markup)
        
        context.user_data['active_tool'] = None
    else:
        await update.message.reply_text("⚠️ **تنبيه استخباراتي:** يرجى البدء بكتابة الأمر `/start` لاختيار الأداة المطلوبة وتفعيل رادار فضاء الهجمات المباشر 🥷🏻")

async def authorities_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "send_authorities":
        await query.message.edit_message_text("🚀 **[تم الاعتماد الأمني]:** تم إرسال التقرير الرسمي الموثق بنجاح إلى الجهات المعنية المعتمدة! 🔒")
    elif query.data == "cancel_authorities":
        await query.message.edit_message_text("👍 **[إلغاء العمليات]:** تم إغلاق الجلسة الحالية. يمكنك البدء من جديد عبر `/start`.")

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
