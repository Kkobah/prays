import random
import telebot

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا! أنا روبوت أذكار وأوقات الصلاة وأدعية. ارسل /azkar للحصول على أذكار، /dua للحصول على أدعية، و /praytimes للحصول على أوقات الصلاة.')

@bot.message_handler(commands=['pr'])
def pray_times(message):
    # Replace these prayer times with actual prayer times for Baghdad
    prayer_times = "أوقات الصلاة في بغداد:\nفجر: 03:45 AM\nشروق الشمس: 05:18 AM\nظهر: 12:15 PM\nعصر: 03:57 PM\nمغرب: 07:00 PM\nعشاء: 08:28 PM"
    bot.reply_to(message, prayer_times)

@bot.message_handler(commands=['a'])
def send_azkar(message):
    # Replace these with actual azkar
    azkar = ["رَضيـتُ بِاللهِ رَبَّـاً وَبِالإسْلامِ ديـناً وَبِمُحَـمَّدٍ صلى الله عليه وسلم نَبِيّـاً" ,"سُبْحَانَ اللَّهِ وَبِحَمْدِهِ", "لا إِلَهَ إِلَّا اللهُ وَحْدَهُ لا شَرِيكَ لَهُ"]
    selected_azkar = random.choice(azkar)
    bot.reply_to(message, selected_azkar)

@bot.message_handler(commands=['d'])
def send_dua(message):
    # Replace these with actual duas
    duas = ["رَبِّ اغْفِرْ وَارْحَمْ وَأَنتَ خَيْرُ الرَّاحِمِينَ", "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ زَوَالِ نِعْمَتِكَ وَتَحَوُّلِ عَافِيَتِكَ وَفُجَاءَةِ نِقْمَتِكَ وَجَمِيعِ سَخَطِكَ"]
    selected_dua = random.choice(duas)
    bot.reply_to(message, selected_dua)

bot.polling()
