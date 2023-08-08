import random
import telebot
from telebot import types

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

bot = telebot.TeleBot(TOKEN)

# Dictionary to store prayer times
prayer_times_dict = {
    "فجر": "04:30 AM",
    "شروق الشمس": "05:45 AM",
    "ظهر": "12:15 PM",
    "عصر": "04:00 PM",
    "مغرب": "07:30 PM",
    "عشاء": "09:00 PM"
}

# List to store azkar
azkar_list = ["سُبْحَانَ اللَّهِ وَبِحَمْدِهِ", "لا إِلَهَ إِلَّا اللهُ وَحْدَهُ لا شَرِيكَ لَهُ"]

# List to store duas
dua_list = ["رَبِّ اغْفِرْ وَارْحَمْ وَأَنتَ خَيْرُ الرَّاحِمِينَ", "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِنْ زَوَالِ نِعْمَتِكَ وَتَحَوُّلِ عَافِيَتِكَ وَفُجَاءَةِ نِقْمَتِكَ وَجَمِيعِ سَخَطِكَ"]

# Function to display the prayer times keyboard
def show_prayer_times_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for prayer in prayer_times_dict:
        button = types.KeyboardButton(prayer)
        keyboard.add(button)
    bot.send_message(message.chat.id, "اختر وقت الصلاة:", reply_markup=keyboard)

# Command to display prayer times keyboard
@bot.message_handler(commands=['praytimes'])
def pray_times(message):
    show_prayer_times_keyboard(message)

# Command to add azkar
@bot.message_handler(commands=['addazkar'])
def add_azkar(message):
    azkar_text = message.text.split(' ', 1)[1]
    azkar_list.append(azkar_text)
    bot.reply_to(message, "تمت إضافة الذكر بنجاح!")

# Command to add dua
@bot.message_handler(commands=['adddua'])
def add_dua(message):
    dua_text = message.text.split(' ', 1)[1]
    dua_list.append(dua_text)
    bot.reply_to(message, "تمت إضافة الدعاء بنجاح!")

# Handler for prayer time buttons
@bot.message_handler(func=lambda message: message.text in prayer_times_dict)
def handle_prayer_time(message):
    prayer_name = message.text
    prayer_time = prayer_times_dict[prayer_name]
    bot.reply_to(message, f"{prayer_name}: {prayer_time}")

# Handler for '/azkar' command
@bot.message_handler(commands=['azkar'])
def send_azkar(message):
    selected_azkar = random.choice(azkar_list)
    bot.reply_to(message, selected_azkar)

# Handler for '/dua' command
@bot.message_handler(commands=['dua'])
def send_dua(message):
    selected_dua = random.choice(dua_list)
    bot.reply_to(message, selected_dua)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا! أنا روبوت أذكار وأوقات الصلاة وأدعية. ارسل /azkar للحصول على أذكار، /dua للحصول على أدعية، و /praytimes للحصول على أوقات الصلاة.')

# Polling loop
bot.polling()
