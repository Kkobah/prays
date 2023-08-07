import random
import telebot

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا! أنا روبوت أذكار وأوقات الصلاة. ارسل /praytimes للحصول على أوقات الصلاة.')

@bot.message_handler(commands=['praytimes'])
def pray_times(message):
    # Replace these prayer times with actual prayer times
    prayer_times = "أوقات الصلاة:\nفجر: 04:30 AM\nشروق الشمس: 05:45 AM\nظهر: 12:15 PM\nعصر: 04:00 PM\nمغرب: 07:30 PM\nعشاء: 09:00 PM"
    bot.reply_to(message, prayer_times)

@bot.message_handler(func=lambda message: True)
def send_dua(message):
    # Replace these with actual duas
    duas = ["اللهم اغفر لي وللمؤمنين والمؤمنات", "اللهم إني أسألك علمًا نافعًا ورزقًا طيبًا وعملاً متقبلاً"]
    selected_dua = random.choice(duas)
    bot.reply_to(message, selected_dua)

bot.polling()
