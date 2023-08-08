import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6409039633:AAEGXtx-M3m6D4148STKnx07TCt3Vt5zUyw'

bot = telebot.TeleBot(TOKEN)

muted_users = set()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! I'm your group protection bot. Use /mute, /unmute, and /kick commands to manage users.")

@bot.message_handler(commands=['mute'])
def mute(message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        muted_users.add(user_id)
        bot.reply_to(message, "تمام.")
    else:
        bot.reply_to(message, "Reply to a user's message to mute them.")

@bot.message_handler(commands=['unmute'])
def unmute(message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        muted_users.discard(user_id)
        bot.reply_to(message, "تمام.")
    else:
        bot.reply_to(message, "Reply to a user's message to unmute them.")

@bot.message_handler(commands=['kick'])
def kick(message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "User kicked from the group.")
    else:
        bot.reply_to(message, "Reply to a user's message to kick them.")

@bot.message_handler(func=lambda message: message.from_user.id in muted_users)
def mute_handler(message):
    bot.delete_message(message.chat.id, message.message_id)

bot.polling()
