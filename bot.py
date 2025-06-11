from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from telegram import Update
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("BOT_TOKEN")

BAD_WORDS = [
    "хуй", "пизда", "ебать", "ебаный", "блять", "сука", "мразь", "гандон", "долбоеб", "пидор",
    "уебок", "соси", "ебло", "нахуй", "ебись", "жопа", "тварь", "мудак", "шлюха", "сучка",
    "Хуй", "Пизда", "Ебать", "Ебаный", "Блять", "Сука", "Мразь", "Гандон", "Долбоеб", "Пидор",
    "Уебок", "Соси", "Ебло", "Нахуй", "Ебись", "Жопа", "Тварь", "Мудак", "Шлюха", "Сучка"
]

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        chat = update.message.chat
        text = update.message.text.lower()

        if any(bad_word in text for bad_word in BAD_WORDS):
            try:
                await update.message.delete()
                await update.message.reply_text("Пожалуйста, не используйте плохие слова!")
            except Exception as e:
                print(f"Ошибка при удалении сообщения: {e}")

def main():
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), check_message))
    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
