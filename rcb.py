from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import google.generativeai as genai

genai.configure('')
model = genai.GenerativeModel('gemini-pro')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = model.generate_content(user_text)
    await update.message.reply_text(response.text)

if __name__ == '__main__':
    app = ApplicationBuilder().token('9052474329:AAHcrnnO8tLP4wU0Ij1n41GXCYizL1d77DM').build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
