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
        "⚡️ **Welcome**\n"
        "🔒 **salman osint كيف اقدر اساعدك** 🥷🏻\n\n"
        "اختر الأداة الاستخباراتية للبدء بمحاكاة البث المباشر للهجمات واستخراج التقرير الرسمي:"
    )
    
    keyboard = [
        [InlineKeyboardButton("📸 بحث الصور العكسي الذكي", callback_data="run_google")],
        [InlineKeyboardButton("🌐 دليل المصادر المفتوحة", callback_data="run_framework")],
        [InlineKeyboardButton("🚗 استعلام المركبات (CarID)", callback_data="run_carid")],
        [InlineKeyboardButton("🐦 تحليل تغريدات X (BirdHunt)", callback_data="run_birdhunt")],
        [InlineKeyboardButton("🫆 الذباب الالكتروني (EulerStream)", callback_data="run_eulerstream")],
        [InlineKeyboardButton("🛰️ رادار خريطة هجوم الفضاء الإلكتروني", callback_data="run_space_cyber")],
        [InlineKeyboardButton("📲 التواصل الاجتماعي مع المبرمج", callback_data="social_links")],
        [InlineKeyboardButton("⏳ باقي تطويرات على البوت قريباً", callback_data="coming_soon")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "run_google":
        context.user_data['active_tool'] = 'google'
        await query.message.reply_text(
            "📸 **أ
