import telebot

TOKEN = "8756716730:AAGQ9JgJWhMg_nzR5wUVJQ08a-G4YRMLPqqs"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет!")


@bot.message_handler(func=lambda message: True)
def handle(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
