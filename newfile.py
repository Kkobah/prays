import random
import telebot
from telebot import types

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

bot = telebot.TeleBot(TOKEN)

# Dictionary to store prayer times
prayer_times_dict = {
    "Fajr": "04:30 AM",
    "Sunrise": "05:45 AM",
    "Dhuhr": "12:15 PM",
    "Asr": "04:00 PM",
    "Maghrib": "07:30 PM",
    "Isha": "09:00 PM"
}

# List to store azkar
azkar_list = ["Subhanallah wa bihamdihi", "La ilaha illallah wahdahu la sharika lahu"]

# List to store duas
dua_list = ["Rabbi-ghfir warham wa anta khayrur-rahimeen", "Allahumma inni a'oodhu bika min zawali ni'matika wa tahawwuli 'afiyatika wa fuja'ati niqmatika wa jami'i sakhatika"]

# Function to display the prayer times keyboard
def show_prayer_times_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for prayer in prayer_times_dict:
        button = types.KeyboardButton(prayer)
        keyboard.add(button)
    bot.send_message(message.chat.id, "Select a prayer time:", reply_markup=keyboard)

# Command to display prayer times keyboard
@bot.message_handler(commands=['praytimes'])
def pray_times(message):
    show_prayer_times_keyboard(message)

# Command to add azkar
@bot.message_handler(commands=['addazkar'])
def add_azkar(message):
    azkar_text = message.text.split(' ', 1)[1]
    azkar_list.append(azkar_text)
    bot.reply_to(message, "Zikr added successfully!")

# Command to add dua
@bot.message_handler(commands=['adddua'])
def add_dua(message):
    dua_text = message.text.split(' ', 1)[1]
    dua_list.append(dua_text)
    bot.reply_to(message, "Dua added successfully!")

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
    bot.reply_to(message, "Welcome! I'm a bot for Azkar, Prayer Times, and Duas. Use /azkar for Azkar, /dua for Duas, and /praytimes for Prayer Times.")

# Polling loop
bot.polling()
