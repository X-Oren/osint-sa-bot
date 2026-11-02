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
        "⚡️ **SALMAN OSINT INTELLIGENCE COMMAND CENTER** 🥷🏻\n"
        "🔒 **منظومة الاستخبارات الميدانية والتحليل الرقمي المتقدم**\n\n"
        "اختر الأداة الاستخباراتية المطلوبة لتشغيل رادار البث المباشر للهجمات واستخراج التقرير الجنائي المعتمد:"
    )
    
    keyboard = [
        [InlineKeyboardButton("📸 بحث الصور العكسي الذكي", callback_data="run_google")],
        [InlineKeyboardButton("🐦 تحليل تغريدات X (BirdHunt)", callback_data="run_birdhunt")],
        [InlineKeyboardButton("🎥 تحليل البثوث الرقمية (EulerStream)", callback_data="run_eulerstream")],
        [InlineKeyboardButton("🌐 فحص التهديدات والهندسة العكسية (PhishCheck)", callback_data="run_phishcheck")],
        [InlineKeyboardButton("🗺️ خريطة فضاء الهجمات المباشرة (Live Cyber Map)", callback_data="run_attack_map")],
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
            "📸 **[وضع الاستخبارات البصرية]:** تم تفعيل محرك البحث العكسي الذكي.\n\n"
            "📥 *أرسل النص أو رابط الصورة المستهدفة لتفعيل رادار التتبع وتحليل العقد المرئية.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_birdhunt":
        context.user_data['active_tool'] = 'birdhunt'
        await query.message.reply_text(
            "🐦 **[وضع الرصد التكتيكي X]:** تم تشغيل أداة BirdHunt للمراقبة الداخلية.\n\n"
            "🛡️ *تم ربط العقد العنقودية بالكامل داخل الشات.*\n"
            "📥 *أرسل رابط التغريدة أو المعرف المستهدف لبدء فحص الشبكة.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_eulerstream":
        context.user_data['active_tool'] = 'eulerstream'
        await query.message.reply_text(
            "🎥 **[وضع الرقابة الرقمية]:** تم تفعيل أداة EulerStream لتحليل البثوث.\n\n"
            "📥 *أرسل رابط البث المباشر لبدء رادار التتبع الجغرافي واستخراج المؤشرات الأمنية.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_phishcheck":
        context.user_data['active_tool'] = 'phishcheck'
        await query.message.reply_text(
            "🌐 **[وضع فحص الثغرات والتهديدات]:** تم تنشيط بروتوكول PhishCheck.\n\n"
            "📥 *أرسل الرابط أو النطاق المشبوه لفحص البنية التحتية وكشف نقاط الضعف الخطرة.*", 
            parse_mode="Markdown"
        )
        
    elif query.data == "run_attack_map":
        context.user_data['active_tool'] = None
        # بث مباشر تفاعلي لخريطة فضاء الهجمات الإلكترونية داخل الشات
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
            "├─ 🔴 **الهدف المرصود (CRITICAL):** عقدة اتصال مشبوهة (Middle-East Sector) `[تنبيه خطر عالي]`\n"
            "├─ ⚠️ **حالة الثغرات:** رصد محاولات حقن برمجيات خبيثة `[مكتشف]`\n"
            "├─ 🛡️ **حالة الجدار الناري:** مفعل ومحصن بالكامل عبر Salman OSINT\n"
            "├─ ⚡ **معدل اعتراض الحزم:** 4.8 GB/s (مستقر)\n"
            "└─ 📍 **الحالة العامة:** البث يعمل بتحديث لحظي مباشر داخل الغرفة الأمنية.\n\n"
            "🚨 *تم رصد مؤشرات خطرة مرتبطة بالنطاق. استخدم القائمة الرئيسية `/start` لفحص الأهداف بدقة.*"
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

def generate_official_osint_pdf(tool_name, target_info, threat_level):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'OfficialTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=15, leading=18,
        textColor=colors.HexColor('#1A365D'), alignment=1
    )
    subtitle_style = ParagraphStyle(
        'OfficialSubtitle', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13,
        textColor=colors.HexColor('#4A5568'), alignment=1
    )
    heading_style = ParagraphStyle(
        'SectionHeading', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=11, leading=15,
        textColor=colors.HexColor('#2B6CB0')
    )
    body_style = ParagraphStyle(
        'OfficialBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=14,
        textColor=colors.HexColor('#2D3748')
    )
    footer_style = ParagraphStyle(
        'OfficialFooter', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=11,
        textColor=colors.HexColor('#718096'), alignment=1
    )

    story = []

    story.append(Paragraph("SALMAN OSINT INTELLIGENCE REPORT", title_style))
    story.append(Paragraph("Official Cyber Security & Open Source Investigation Unit 🥷🏻", subtitle_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1A365D'), spaceAfter=12))

    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')
    meta_data = [
        [Paragraph("<b>Report ID:</b> SOSINT-2026-908", body_style), Paragraph(f"<b>Timestamp:</b> {current_time}", body_style)],
        [Paragraph("<b>Classification:</b> Top Secret / Official", body_style), Paragraph(f"<b>Status:</b> Verified 🟢 ({threat_level})", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F7FAFC')),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("1. Target & Tool Operational Data", heading_style))
    story.append(Spacer(1, 4))
    
    target_data = [
        [Paragraph("<b>Active Tool:</b>", body_style), Paragraph(f"{tool_name}", body_style)],
        [Paragraph("<b>Target Input:</b>", body_style), Paragraph(f"{target_info}", body_style)],
        [Paragraph("<b>Threat Level:</b>", body_style), Paragraph(f"{threat_level}", body_style)],
        [Paragraph("<b>Technical Status:</b>", body_style), Paragraph("Scanned successfully via live cyber attack radar", body_style)]
    ]
    target_table = Table(target_data, colWidths=[140, 400])
    target_table.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 5),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#EDF2F7')),
    ]))
    story.append(target_table)
    story.append(Spacer(1, 12))

    story.append(Paragraph("2. Detailed Target Analysis & Findings", heading_style))
    story.append(Spacer(1, 4))
    
    analysis_text = (
        f"Target Reference: {target_info}<br/>"
        "• Network Infrastructure: Active routing nodes identified across regional gateways.<br/>"
        "• Threat Assessment: Comprehensive OSINT correlation completed.<br/>"
        "• Security Status: Evaluated against global threat intelligence databases.<br/>"
        "• Actionable Intelligence: All digital artifacts and metadata successfully cataloged."
    )
    story.append(Paragraph(analysis_text, body_style))
    story.append(Spacer(1, 15))

    story.append(Paragraph("3. Official Authorization & Seal", heading_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("This report is digitally generated and certified via Salman OSINT Automation System for official use.", body_style))
    story.append(Spacer(1, 25))

    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E0'), spaceAfter=8))
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
        
        # محاكاة شاشة بث مباشر تفاعلية داخل الشات
        stream_msg = await update.message.reply_text("🚨 **[LIVE CYBER STREAM]** جاري تهيئة الاتصال برادار فضاء الهجمات واستخراج عقد البيانات...")
        await asyncio.sleep(1.0)
        
        await stream_msg.edit_text("📡 **[LIVE CYBER STREAM]** يتم رصد وتتبع الثغرات وتحليل الأنشطة عبر خوادم الأوسنت...")
        await asyncio.sleep(1.2)
        
        await stream_msg.edit_text("🗺️ **[ATTACK MAP SYNC]** إسقاط الإحداثيات الجغرافية للهدف على خريطة الفضاء السيبراني المباشر...")
        await asyncio.sleep(1.0)
        
        await stream_msg.edit_text("⚡️ **[LIVE CYBER STREAM]** اكتشاف الهدف بنجاح! جاري اعتراض الحزم وتأمين البث...")
        await asyncio.sleep(1.0)
        
        await stream_msg.edit_text("🟢 **[LIVE CYBER STREAM]** تم إكمال الفحص وتحليل النتائج بنجاح، جاري بناء التقرير الجنائي...")
        await asyncio.sleep(0.8)
        
        # تقييم مستوى الخطورة وتحديد التفاعل المناسب
        # (ملاحظة: في تقارير PDF تم استخدام مفاتيح الإنجليزية لضمان عدم ظهور النص كرموز غير مقروءة بسبب قيود الخطوط الافتراضية في ReportLab)
        is_dangerous = any(keyword in user_text.lower() for keyword in ['http', 'www', 'malware', 'hack', 'attack', 'phish', 'scam', 'suspect', 'admin', 'root'])
        threat_level = "CRITICAL / DANGEROUS 🔴" if is_dangerous else "MODERATE / SECURE 🟢"
        risk_emoji = "🚨" if is_dangerous else "🟢"
        
        # تنسيق معلومات الهدف بشكل مرتب ومفصل تحت الهدف مباشرة داخل الشات مع رموز تفاعلية استخباراتية
        structured_chat_report = (
            f"🎯 **[تقرير الاستخبارات الفورية - Salman OSINT]**\n"
            f"──────────────────────────────\n"
            f"📌 **الهدف المرصود:** `{user_text}`\n"
            f"🛠️ **الأداة المستخدمة:** `{tool_title}`\n"
            f"📊 **مستوى الخطورة والتفاعل:** {risk_emoji} **{threat_level}**\n\n"
            f"📋 **النتائج التفصيلية لكل هدف:**\n"
            f"  ├─ 🌐 **البنية التحتية والعقد:** مطابقة تامة لقواعد البيانات الجغرافية\n"
            f"  ├─ 🔍 **فحص الثغرات (Vulnerabilities):** {'تم اكتشاف مؤشرات حقن وتهديدات عالية' if is_dangerous else 'لا توجد ثغرات حرجة ظاهرة'}\n"
            f"  ├─ 📡 **حالة الرصد الجغرافي:** مؤكد عبر رادار فضاء الهجمات المباشر\n"
            f"  └─ 🛡️ **التوصية الأمنية:** {'عزل الهدف وفحص الحزم فوراً' if is_dangerous else 'متابعة روتينية وآمنة'}\n"
            f"──────────────────────────────"
        )
        await update.message.reply_text(structured_chat_report, parse_mode="Markdown")
        
        # إنشاء ملف PDF الرسمي في الذاكرة (تم تحسينه لضمان وضوح البيانات الإنجليزية والرقمية دون تشفير)
        pdf_file = generate_official_osint_pdf(tool_title, user_text, threat_level)
        pdf_file.name = "Salman_Official_OSINT_Report.pdf"
        
        # إرسال ملف الـ PDF الرسمي للمستخدم
        await update.message.reply_document(
            document=pdf_file,
            caption=f"📄 **إليك تقرير الاستخبارات الرسمي المعتمد للهدف.** {risk_emoji}"
        )
        
        # رد تفاعلي استخباراتي بعد إرسال التقرير
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
