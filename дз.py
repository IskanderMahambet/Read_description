import telebot
import datetime

token = '485606860:AAFC1eSP_LksyJSRHsDK0Z9b49Rt4u_YzEI'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def check_message(message):
    time=str(datetime.datetime.now())
    file = open('text.csv','w',encoding = 'utf-8')
    file.write(message.text)
    file.write('             ')
    file.write(time)

bot.polling(none_stop=True)
file.close()

