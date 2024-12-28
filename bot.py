from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# التوكن وID الإدمن
TOKEN = "8154296863:AAEdjzVYyvndPdAkKlPZNw04Ep6bzRcsDxY"
ADMIN_ID = 270734616

# قائمة لتخزين الرسائل
messages = []

# أمر /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا بك في صارحني! أرسل رسالتك الآن.")

# معالجة الرسائل النصية
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # تخزين بيانات الرسالة
    message_data = {
        "text": update.message.text,
        "sender_name": update.message.from_user.full_name,
        "sender_username": update.message.from_user.username,
        "sender_id": update.message.from_user.id,
    }

    # إرسال تأكيد للمرسل
    await update.message.reply_text("تم إرسال رسالتك بنجاح!")

    # تنسيق الرسالة للإدمن
    admin_message = (
        f"📩 **رسالة جديدة:**\n"
        f"📜 النص: {message_data['text']}\n"
        f"🙍‍♂️ الاسم: {message_data['sender_name']}\n"
        f"🔗 المعرف: @{message_data['sender_username'] if message_data['sender_username'] else 'غير موجود'}\n"
        f"🆔 ID: {message_data['sender_id']}"
    )

    # إرسال الرسالة للإدمن
    await context.bot.send_message(chat_id=ADMIN_ID, text=admin_message, parse_mode="Markdown")

# إعداد البوت
def main():
    # بناء التطبيق باستخدام ApplicationBuilder
    app = ApplicationBuilder().token(TOKEN).build()

    # إضافة الأوامر والمستمعين
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ البوت يعمل الآن... افتح Telegram وابدأ بالتفاعل!")

    # تشغيل البوت
    app.run_polling()

if __name__ == "__main__":
    main()
