import random
import telebot

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا! أنا روبوت أذكار وأوقات الصلاة وأدعية. ارسل /azkar للحصول على أذكار، /dua للحصول على أدعية، و /praytimes للحصول على أوقات الصلاة.')

@bot.message_handler(commands=['praytimes'])
def pray_times(message):
    # Replace these prayer times with actual prayer times for Baghdad
    prayer_times = "أوقات الصلاة في بغداد:\nفجر: 04:30 AM\nشروق الشمس: 05:45 AM\nظهر: 12:15 PM\nعصر: 04:00 PM\nمغرب: 07:30 PM\nعشاء: 09:00 PM"
    bot.reply_to(message, prayer_times)

@bot.message_handler(commands=['azkar'])
def send_azkar(message):
    # Replace these with actual azkar
    azkar = ["سُبْحَانَ اللَّهِ وَبِحَمْدِهِ", "لا إِلَهَ إِلَّا اللهُ وَحْدَهُ لا شَرِيكَ لَهُ"]
    selected_azkar = random.choice(azkar)
    bot.reply_to(message, selected_azkar)

@bot.message_handler(commands=['dua'])
def send_dua(message):
    # Replace these with actual duas
    duas = ["رَبِّ اغْفِرْ وَارْحَمْ وَأَنتَ خَيْرُ الرَّاحِمِينَ", "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ زَوَالِ نِعْمَتِكَ وَتَحَوُّلِ عَافِيَتِكَ وَفُجَاءَةِ نِقْمَتِكَ وَجَمِيعِ سَخَطِكَ"]
    selected_dua = random.choice(duas)
    bot.reply_to(message, selected_dua)

bot.polling()
