import random
import telebot
import requests
import time

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6357249652:AAGrVUHOKYWcLrBJr8KsZ4-cbX4BwKQYmmc'

bot = telebot.TeleBot(TOKEN)

def get_prayer_times(city):
    url = f'http://api.aladhan.com/v1/timingsByCity?city={city}&country=Iraq&method=8'
    response = requests.get(url)
    data = response.json()
    prayer_times = data['data']['timings']
    return prayer_times

def send_daily_prayer_times(chat_id, prayer_times):
    message = "أوقات الصلاة:\n"
    for prayer, time in prayer_times.items():
        message += f"{prayer}: {time}\n"
    bot.send_message(chat_id, message)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'مرحبًا! أنا روبوت أذكار وأوقات الصلاة. ارسل /dua للحصول على أذكار و /praytimes لأوقات الصلاة.')

@bot.message_handler(commands=['dua'])
def send_dua(message):
    # Replace these with actual duas
    duas = ["اللهم اغفر لي وللمؤمنين والمؤمنات", "اللهم إني أسألك علمًا نافعًا ورزقًا طيبًا وعملاً متقبلاً"]
    selected_dua = random.choice(duas)
    bot.reply_to(message, selected_dua)

@bot.message_handler(commands=['praytimes'])
def pray_times_command(message):
    city = 'Baghdad'  # You can change this to your preferred city
    prayer_times = get_prayer_times(city)
    send_daily_prayer_times(message.chat.id, prayer_times)

def send_prayer_times_reminder():
    city = 'Baghdad'
    prayer_times = get_prayer_times(city)
    for chat_id in chat_ids:
        send_daily_prayer_times(chat_id, prayer_times)
        time.sleep(1)  # To prevent rate limiting

# Set the chat IDs where you want to send automatic prayer time reminders
chat_ids = [1896079987]

# Schedule automatic prayer time reminders
while True:
    current_time = time.strftime('%H:%M')
    if current_time == '00:00':  # You can adjust the time as needed
        send_prayer_times_reminder()
    time.sleep(60)  # Check every minute

bot.polling()
