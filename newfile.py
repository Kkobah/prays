import telebot
import requests
import time

# Replace 'YOUR_TOKEN' with your actual Telegram Bot API token
TOKEN = '6656009330:AAEcN7IxrirVgsx6clSJliYe9p42dRc6bEU'

bot = telebot.TeleBot(TOKEN)

def get_prayer_times():
    response = requests.get("http://api.aladhan.com/v1/timingsByCity?city=Baghdad&country=Iraq")
    data = response.json()
    times = data['data']['timings']
    return times

@bot.inline_handler(lambda query: True)
def inline_query(query):
    try:
        prayer_times = get_prayer_times()
        inline_results = []
        
        for prayer, time in prayer_times.items():
            result = telebot.types.InlineQueryResultArticle(
                id=prayer,
                title=prayer,
                description=time,
                input_message_content=telebot.types.InputTextMessageContent(
                    message_text=f"{prayer}: {time}"
                )
            )
            inline_results.append(result)
        
        bot.answer_inline_query(query.id, inline_results)
    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    
