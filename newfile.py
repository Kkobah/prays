خوش خوشimport telebot

TOKEN = '6573645457:AAHTK0Id4tYBIerhP50zZCt07tf1RzYsYQo'
bot = telebot.TeleBot(TOKEN)

# Command to kick a user
@bot.message_handler(commands=['kick'])
def kick_user(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is the group owner or an administrator
    user_info = bot.get_chat_member(chat_id, user_id)
    if user_info.status in ("creator", "administrator"):
        try:
            target_user_info = message.reply_to_message.from_user
            if target_user_info.is_bot:
                bot.reply_to(message, "Cannot kick bots.")
            elif target_user_info.status not in ("creator", "administrator"):
                bot.kick_chat_member(chat_id, target_user_info.id)
                bot.reply_to(message, "User kicked.")
            else:
                bot.reply_to(message, "Cannot kick administrators.")
        except AttributeError:
            bot.reply_to(message, "Reply to a user's message to kick them.")
    else:
        bot.reply_to(message, "Only administrators can use this command.")

# Command to mute a user
@bot.message_handler(commands=['mute'])
def mute_user(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is the group owner or an administrator
    user_info = bot.get_chat_member(chat_id, user_id)
    if user_info.status in ("creator", "administrator"):
        try:
            target_user_id = message.reply_to_message.from_user.id
            target_user_info = bot.get_chat_member(chat_id, target_user_id)
            if target_user_info.status not in ("creator", "administrator"):
                bot.restrict_chat_member(chat_id, target_user_id, can_send_messages=False)
                bot.reply_to(message, "User muted.")
            else:
                bot.reply_to(message, "Cannot mute administrators.")
        except AttributeError:
            bot.reply_to(message, "Reply to a user's message to mute them.")
    else:
        bot.reply_to(message, "Only administrators can use this command.")

# Command to unmute a user
@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is the group owner or an administrator
    user_info = bot.get_chat_member(chat_id, user_id)
    if user_info.status in ("creator", "administrator"):
        try:
            target_user_id = message.reply_to_message.from_user.id
            bot.restrict_chat_member(chat_id, target_user_id, can_send_messages=True)
            bot.reply_to(message, "User unmuted.")
        except AttributeError:
            bot.reply_to(message, "Reply to a user's message to unmute them.")
    else:
        bot.reply_to(message, "Only administrators can use this command.")

# Command to pin a message
@bot.message_handler(commands=['pin'])
def pin_message(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is the group owner or an administrator
    user_info = bot.get_chat_member(chat_id, user_id)
    if user_info.status in ("creator", "administrator"):
        try:
            target_message_id = message.reply_to_message.message_id
            bot.pin_chat_message(chat_id, target_message_id)
            bot.reply_to(message, "Message pinned.")
        except AttributeError:
            bot.reply_to(message, "Reply to a message to pin it.")
    else:
        bot.reply_to(message, "Only administrators can use this command.")




# Dictionary to store custom replies
custom_replies = {}

# ... (previous command handlers)

# Command to set a custom reply
@bot.message_handler(commands=['setreply'])
def set_custom_reply(message):
    user_id = message.from_user.id

    # Check if the user is the group owner or an administrator
    user_info = bot.get_chat_member(message.chat.id, user_id)
    if user_info.status in ("creator", "administrator"):
        try:
            command_parts = message.text.split(" ", 2)
            if len(command_parts) > 2:
                reply_name = command_parts[1]
                reply_text = command_parts[2]
                custom_replies[reply_name] = reply_text
                bot.reply_to(message, f"Custom reply '{reply_name}' set.")
            else:
                bot.reply_to(message, "Usage: /setreply <name> <text>")
        except AttributeError:
            bot.reply_to(message, "Usage: /setreply <name> <text>")
    else:
        bot.reply_to(message, "Only administrators can use this command.")

# Command to use a custom reply
@bot.message_handler(func=lambda message: any(reply in message.text for reply in custom_replies))
def process_custom_reply(message):
    user_id = message.from_user.id

    for reply_name, reply_text in custom_replies.items():
        if reply_name in message.text:
            bot.reply_to(message, reply_text)
            break


# ... (previous command handlers)

# Command to remove a custom reply
@bot.message_handler(commands=['removereply'])
def remove_custom_reply(message):
    if len(message.text.split(' ', 1000)) > 1000:
        user_id = message.from_user.id

        # Check if the user is an administrator
        user_info = bot.get_chat_member(message.chat.id, user_id)
        if user_info.status in ("creator", "administrator"):
            reply_name = message.text.split(' ', 1)[1].lower()
            if reply_name in custom_replies:
                del custom_replies[reply_name]
                bot.reply_to(message, f"Custom reply '{reply_name}' removed.")
            else:
                bot.reply_to(message, f"Custom reply '{reply_name}' not found.")
        else:
            bot.reply_to(message, "Only administrators can use this command.")
    else:
        bot.reply_to(message, "Usage: /removereply <name>")
        
        
    


# ... (previous command handlers)

# Command to add an admin
@bot.message_handler(commands=['addadmin'])
def add_admin(message):
    user_id = message.from_user.id
    chat_id = message.chat.id

    # Check if the user is the group owner
    user_info = bot.get_chat_member(chat_id, user_id)
    if user_info.status == "creator":
        try:
            target_user_id = message.reply_to_message.from_user.id
            bot.promote_chat_member(chat_id, target_user_id, can_change_info=True, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=False)
            bot.reply_to(message, "User promoted to administrator.")
        except AttributeError:
            bot.reply_to(message, "Reply to a user's message to promote them.")
    else:
        bot.reply_to(message, "Only the group owner can use this command.")

if __name__ == "__main__":
    bot.polling()

