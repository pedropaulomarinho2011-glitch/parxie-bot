from flask import Flask
import threading
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8708124318:AAFOLWvL_gfaWHmwIY4fvZm9o5mzi8cmo5I"

app = Flask('')

@app.route('/')
def home():
    return "Bot rodando"

def run_web():
    app.run(host='0.0.0.0', port=10000)

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    await update.message.reply_text(f"Você disse: {texto}")

bot = ApplicationBuilder().token(TOKEN).build()
bot.add_handler(MessageHandler(filters.TEXT, responder))

def run_bot():
    bot.run_polling()

threading.Thread(target=run_web).start()
run_bot()
