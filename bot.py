import telebot

TOKEN = "8756716730:AAGLtb2TJTW-SQwcbw04ENFpG0S7KbHgNY4"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(func=lambda message: True)
def handle(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
