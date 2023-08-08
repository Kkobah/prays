import random
import telebot
import sqlite3
from telebot import types

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table for azkar if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS azkar (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')

# Create a table for duas if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS duas (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)''')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا! أنا روبوت أذكار وأدعية. ارسل /azkar للحصول على أذكار، /dua للحصول على أدعية، و /praytimes للحصول على أوقات الصلاة.')

@bot.message_handler(commands=['praytimes'])
def pray_times(message):
    # Replace these prayer times with actual prayer times for Baghdad
    prayer_times = "أوقات الصلاة في بغداد:\nفجر: 04:30 AM\nشروق الشمس: 05:45 AM\nظهر: 12:15 PM\nعصر: 04:00 PM\nمغرب: 07:30 PM\nعشاء: 09:00 PM"
    bot.reply_to(message, prayer_times)

@bot.message_handler(commands=['azkar'])
def send_azkar(message):
    cursor.execute("SELECT text FROM azkar")
    azkar_list = cursor.fetchall()
    
    if not azkar_list:
        bot.reply_to(message, "لا يوجد أذكار مضافة حاليًا.")
    else:
        selected_azkar = random.choice(azkar_list)[0]
        bot.reply_to(message, selected_azkar)

@bot.message_handler(commands=['dua'])
def send_dua(message):
    cursor.execute("SELECT text FROM duas")
    duas_list = cursor.fetchall()
    
    if not duas_list:
        bot.reply_to(message, "لا يوجد أدعية مضافة حاليًا.")
    else:
        selected_dua = random.choice(duas_list)[0]
        bot.reply_to(message, selected_dua)

@bot.message_handler(commands=['addazkar'])
def add_azkar(message):
    bot.reply_to(message, "أرسل الذكر الجديد:")
    bot.register_next_step_handler(message, save_new_azkar)

def save_new_azkar(message):
    new_azkar = message.text
    cursor.execute("INSERT INTO azkar (text) VALUES (?)", (new_azkar,))
    conn.commit()
    bot.reply_to(message, "تم إضافة الذكر بنجاح.")

@bot.message_handler(commands=['adddua'])
def add_dua(message):
    bot.reply_to(message, "أرسل الدعاء الجديد:")
    bot.register_next_step_handler(message, save_new_dua)

def save_new_dua(message):
    new_dua = message.text
    cursor.execute("INSERT INTO duas (text) VALUES (?)", (new_dua,))
    conn.commit()
    bot.reply_to(message, "تم إضافة الدعاء بنجاح.")

bot.polling()
