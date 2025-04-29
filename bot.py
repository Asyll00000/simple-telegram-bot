import telebot

# Вставь сюда свой токен от BotFather
TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Привет! Я простой Telegram-бот.")

bot.polling()
