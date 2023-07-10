'''
    _[Telegram Bot]_
     - get data from the excel
     - check the name if it's be there
'''

import os
import pandas as pd
import telebot

sheet_id = os.getenv('SHEET_ID')
sheet_name = os.getenv('SHEET_NAME')
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

# @bot.message_handler(commands=['Greet'])
# def greet(message):
#   bot.reply_to(message, "Hey! Hows it going?")


def stock_request(message):
  request = message.text.split()
  return request

@bot.message_handler(func=stock_request)
def send_price(message):
#   request = message.text.split()[1]

  df = pd.read_csv(url)

#   names = list(df.Name)
#   print(message)
#   if(message.text in  names):

  if len(df[df.Name == message.text].State) == 1:
    bot.send_message(message.chat.id,df[df.Name == message.text].State)
  else:
    bot.send_message(message.chat.id,"الاسم غير موجود")

bot.polling()