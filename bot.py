import re
import telebot
from config import TOKEN
import wikipedia
from urllib.parse import unquote
regexp = r'^\[\[(.+?)\]\]|\{\{(.+?)\}\}$'

bot = telebot.TeleBot(TOKEN)
wikipedia.set_lang("zh")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if (message.chat.type == 'private'):
        bot.send_message(message.chat.id, '直接输入文字，如：华为')

@bot.message_handler(commands=['version'])
def help(message):
    if (message.chat.type == 'private'):
        bot.reply_to(message, "https://github.com/Jv0id/groupwiki")

#@bot.message_handler(regexp=regexp)
@bot.message_handler()
def search_keyword(message):
    #m = re.search(regexp, message.text)
    #keyword = m[1] or m[2]
    #if not keyword: return
    keyword = message.text
    try:
        result = wikipedia.page(keyword)
        bot.reply_to(message, unquote(result.url), parse_mode="markdown")
    except wikipedia.exceptions.PageError:
        bot.reply_to(message, '没找到结果')

if __name__ == '__main__':
    print('Service is running...')
    bot.polling()
