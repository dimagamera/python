from lib.db_manager import db_manager
from lib.settings import *
import telebot

__URL = "https://api.covid19api.com/summary"
db_object = db_manager(host, user, passwd, database, __URL)
covid_19_data = db_object.get_all_data()
bot = telebot.TeleBot(token)
# db_object.save_all_data(covid_19_data)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    countr = message.text
    coron = db_object.show_country(countr)
    if message.text == countr:
        for item in coron:
            bot.send_message(message.from_user.id, "Оперативна інформація про поширення коронавірусної інфекції 🌏 [𝐂𝐎𝐕𝐈𝐃-19] 🌏\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"+"\n✈️ Країна ✈️ → " + str(item[1]) +
                             "\n🤧 Кількість захворювань 🤧 → " + str(item[4]) + "\n🤧 Кількість захворювань за добу 🤧 → " + str(item[5]) + "\n☠️ Кількість смертей ☠️ → " + str(item[6]) + "\n☠️ Кількість смертей за добу ☠️ → " + str(item[5]) + "\n💊 Кількість вилікуваних 💊 → " + str(item[8]) + "\n💊 Кількість вилікуваних за добу 💊 → " + str(item[7]))


bot.polling(none_stop=True)