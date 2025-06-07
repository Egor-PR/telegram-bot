# from telegram import Update
# from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
# import asyncio

# # Твой Telegram токен
# TOKEN = '8186346125:AAFAT_vAxbI8Snw7srus3iuJ9GTF1_NfAiU'

# # Функция обработки входящих сообщений
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Бот получил сообщение!")

# # Главная функция
# async def main():
#     app = ApplicationBuilder().token(TOKEN).build()
#     app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#     await app.run_polling()

# # Обход ошибки "loop already running"
# if __name__ == '__main__':
#     import nest_asyncio
#     nest_asyncio.apply()

#     asyncio.get_event_loop().run_until_complete(main())


# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
# from textblob import TextBlob

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

# TOKEN = '8186346125:AAFAT_vAxbI8Snw7srus3iuJ9GTF1_NfAiU'

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if update.message and update.message.text:
#         text = update.message.text
#         blob = TextBlob(text)
#         polarity = blob.sentiment.polarity
#         logging.info(f"Message: {text} | Polarity: {polarity}")

#         if polarity < -0.3:
#             try:
#                 await update.message.delete()
#                 logging.info("Deleted a negative message")
#             except Exception as e:
#                 logging.error(f"Error deleting message: {e}")

# def main():
#     app = ApplicationBuilder().token(TOKEN).build()
#     app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

#     print("Bot started...")
#     app.run_polling()

# if __name__ == '__main__':
#     main()

# from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
# from telegram import Update

# BAD_WORDS = ['плохое', 'слово', 'пример']

# async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f"Получено обновление: {update}")
#     if update.message and update.message.text:
#         text = update.message.text.lower()
#         print(f"Текст сообщения: {text}")
#         if any(bad_word in text for bad_word in BAD_WORDS):
#             print("Плохое слово найдено")
#             try:
#                 await update.message.delete()
#                 await update.message.reply_text("Пожалуйста, не используйте плохие слова!")
#             except Exception as e:
#                 print(f"Ошибка при удалении сообщения: {e}")

# def main():
#     token = '8186346125:AAFAT_vAxbI8Snw7srus3iuJ9GTF1_NfAiU'
#     app = ApplicationBuilder().token(token).build()
#     app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), check_message))

#     print("Бот запущен...")
#     app.run_polling()

# if __name__ == '__main__':
#     main()
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from telegram import Update

BAD_WORDS = ['плохое', 'слово', 'пример']

async def check_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"DEBUG: Получено обновление: {update}")  # Выводим всё обновление

    if update.message and update.message.text:
        chat = update.message.chat
        text = update.message.text.lower()

        print(f"DEBUG: Тип чата: {chat.type} | Название: {chat.title if chat.title else chat.id}")
        print(f"DEBUG: Сообщение: {text}")

        if any(bad_word in text for bad_word in BAD_WORDS):
            print("DEBUG: Найдено плохое слово")
            try:
                await update.message.delete()
                await update.message.reply_text("Пожалуйста, не используйте плохие слова!")
            except Exception as e:
                print(f"Ошибка при удалении сообщения: {e}")
        else:
            print("DEBUG: Сообщение не содержит запрещённых слов")
    else:
        print("DEBUG: Сообщение отсутствует или не является текстом")

def main():
    token = '8186346125:AAFAT_vAxbI8Snw7srus3iuJ9GTF1_NfAiU'
    app = ApplicationBuilder().token(token).build()

    # Обрабатываем все текстовые сообщения (без фильтра по типу чата)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), check_message))

    print("Бот запущен...")
    app.run_polling()

if __name__ == '__main__':
    main()
    
