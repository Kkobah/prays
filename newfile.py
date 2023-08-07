import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا روبوت أذكار وأوقات الصلاة. ارسل /praytimes للحصول على أوقات الصلاة.')

def pray_times(update: Update, context: CallbackContext) -> None:
    # Replace these prayer times with actual prayer times
    prayer_times = "أوقات الصلاة:\nفجر: 04:30 AM\nشروق الشمس: 05:45 AM\nظهر: 12:15 PM\nعصر: 04:00 PM\nمغرب: 07:30 PM\nعشاء: 09:00 PM"
    update.message.reply_text(prayer_times)

def send_dua(update: Update, context: CallbackContext) -> None:
    # Replace these with actual duas
    duas = ["اللهم اغفر لي وللمؤمنين والمؤمنات", "اللهم إني أسألك علمًا نافعًا ورزقًا طيبًا وعملاً متقبلاً"]
    selected_dua = random.choice(duas)
    update.message.reply_text(selected_dua)

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("praytimes", pray_times))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_dua))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
