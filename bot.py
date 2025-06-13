from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from telegram import Update
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("BOT_TOKEN")

BAD_WORDS = [
    # Нецензурные слова
    "хуй", "пизда", "ебать", "ебаный", "ебан", "ебанутый", "блять", "сука", "мразь", "гандон", 
    "долбоеб", "пидор", "уебок", "уебище", "соси", "ебло", "нахуй", "ебись", "жопа", "тварь", 
    "мудак", "шлюха", "сучка", "даун", "петух", "мудила", "гнида", "дрянь", "хуила", "манда", 
    "залупа", "пидорас", "пидарас", "дебил", "идиот", "кретин", "нехуй", "выеб", "выебать", 
    "въебать", "наебать", "переебать", "объебать", "доебаться", "прихуел", "охуел", "охуеть",
    "нахера", "похуй", "похер", "похерить", "поебать", "хер", "хуярить", "хуесос", "ссать", 
    "ссанина", "выебон", "жопастая", "ебливый", "говно", "говнюк", "говнистый", "моча", "срань",
    "срака", "обдолбанный", "чмо", "мерзота", "тупица", "недоумок", "кал", "сучий", "дристать",
    "нихуя", "поебень", "ебанная", "еблан", "хуйня", "выебу", "пиздюки", "пиздюк", "пиздюка",
    "ебало", "пизды", "пиздец", "спиздили", "спиздил", "нихуево", "уебат", "уебал", "выебнулся",
    "выебывается", "ахуел", "заебись", "ахуенная", "ахуенно", "ахуенный", "уёбище", "хули",
    "пиздишь", "ахуе",

    # Заглавные
    "Хуй", "Пизда", "Ебать", "Ебаный", "Ебан", "Ебанутый", "Блять", "Сука", "Мразь", "Гандон",
    "Долбоеб", "Пидор", "Уебок", "Уебище", "Соси", "Ебло", "Нахуй", "Ебись", "Жопа", "Тварь",
    "Мудак", "Шлюха", "Сучка", "Даун", "Петух", "Мудила", "Гнида", "Дрянь", "Хуила", "Манда",
    "Залупа", "Пидорас", "Пидарас", "Дебил", "Идиот", "Кретин", "Нехуй", "Выеб", "Выебать",
    "Въебать", "Наебать", "Переебать", "Объебать", "Доебаться", "Прихуел", "Охуел", "Охуеть",
    "Нахера", "Похуй", "Похер", "Похерить", "Поебать", "Хер", "Хуярить", "Хуесос", "Ссать",
    "Ссанина", "Выебон", "Жопастая", "Ебливый", "Говно", "Говнюк", "Говнистый", "Моча", "Срань",
    "Срака", "Обдолбанный", "Чмо", "Мерзота", "Тупица", "Недоумок", "Кал", "Сучий", "Дристать",
    "Нихуя", "Поебень", "Ебанная", "Еблан", "Хуйня", "Выебу", "Пиздюки", "Пиздюк", "Пиздюка",
    "Ебало", "Пизды", "Пиздец", "Спиздили", "Спиздил", "Нихуево", "Уебат", "Уебал", "Выебнулся",
    "Выебывается", "Ахуел", "Заебись", "Ахуенная", "Ахуенно", "Ахуенный", "Уёбище", "Хули",
    "Пиздишь", "Ахуе",

    # Транслит
    "huy", "pizda", "ebat", "eban", "ebanutyi", "blyat", "suka", "mraz", "gandon", "dolboeb",
    "pidor", "uyebok", "uebische", "sosi", "eblo", "nahui", "ebis", "zhopa", "tvar", "mudak",
    "shluha", "suchka", "daun", "petuh", "mudila", "gnida", "dryan", "huila", "manda", "zalupa",
    "pidaras", "pidorass", "debil", "idiot", "kretin", "nehuy", "vyeb", "vyebat", "vjebat",
    "naebat", "pereebat", "obebat", "doebatsya", "prihuel", "ohuel", "ohuet", "nahera", "pohuy",
    "poher", "poherit", "poebat", "kher", "huyarit", "huesos", "ssat", "ssanina", "vyebon",
    "zhopastaya", "eblivyi", "govno", "govnyuk", "govnistyi", "mocha", "sran", "sraka",
    "obdolbannyi", "chmo", "merzota", "tupitsa", "nedoumok", "kal", "suchiy", "dristat",
    "nixuya", "poeben", "ebannaya", "eblan", "huynya", "vyebu", "pizdyuki", "pizdyuk", "pizdyuka",
    "ebalo", "pizdy", "pizdets", "spizdili", "spizdil", "nixuevo", "uyebat", "uyebal", "vyebnulsya",
    "vyebyvaetsya", "ahuel", "zaebis", "ahuennaya", "ahueno", "ahuennyi", "uyobische", "huli",
    "pizdish", "ahue"
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
