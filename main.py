import telebot
import telebotapi
from config import token
from telebot import types
bot = telebot.TeleBot(token)

url = 'https://detskiy-style.by/'
one1 = 'https://detskiy-style.by/tproduct/1-884060409491-detskii-elektromobil-novakids-bentley-ex'
one2 = 'https://detskiy-style.by/tproduct/1-295449452061-detskii-elektromobil-toyland-mercedes-be'
one3 = 'https://detskiy-style.by/tproduct/1-962924015001-detskii-elektromobil-novakids-mercedes-b'
two1 = 'https://detskiy-style.by/tproduct/1-690780829091-detskii-elektromobil-toyland-mercedes-be'
two2 = 'https://detskiy-style.by/tproduct/1-789306296951-detskii-elektromobil-toyland-baggi-monst'
two3 = 'https://detskiy-style.by/tproduct/1-647715165581-roskosh-na-grani-razoreniya-detskii-elek'
three1 = 'https://detskiy-style.by/tproduct/1-220720657621-dvuhmestnii-detskii-elektromobil-toyland'
three2 = 'https://detskiy-style.by/tproduct/1-440469791781-detskii-elektromobil-toyland-mercedes-be'
three3 = 'https://detskiy-style.by/tproduct/1-761018435511-dvuhmestnii-detskii-elektromobil-novakid'
te1 = '@Detskiy_style'
te2 = '@Detskiy_style'
te3 = '@kalamix128'
@bot.message_handler(commands= ['start'])
def user_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    us1 = types.KeyboardButton('Перейти на сайт.')
    us2 = types.KeyboardButton('Помощь специалиста.')
    us3 = types.KeyboardButton('Помощь бота.')
    markup.add(us1, us2, us3)
    bot.send_message(message.chat.id, 'Привет! Я бот который пможет выбрать детский атомобиль из магазина номер один в Беларуси! Нажмите на одну из кнопок или напишите нам!', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def callback(message):
    if message.chat.type == 'private':
        if message.text == 'Перейти на сайт.':
            bot.send_message(message.chat.id, url)
        elif message.text == 'Помощь специалиста.':
            markup = types.InlineKeyboardMarkup(row_width=3)
            tel1 = types.InlineKeyboardButton('Алёна', callback_data='al')
            tel2 = types.InlineKeyboardButton('Светлана', callback_data='sv')
            tel3 = types.InlineKeyboardButton('Николай', callback_data='nk')
            markup.add(tel1, tel2, tel3)
            bot.send_message(message.chat.id, 'Мы поможем осуществить мечту Вашего ребёнка!', reply_markup=markup)
        elif message.text == 'Помощь бота.':
            markup = types.InlineKeyboardMarkup(row_width=2)
            year1 = types.InlineKeyboardButton('От 1 до 3', callback_data='one')
            year2 = types.InlineKeyboardButton('От 4 до 7', callback_data='two')
            year3 = types.InlineKeyboardButton('От 8 до 12', callback_data='three')
            markup.add(year1, year2, year3)
            bot.send_message(message.chat.id, 'Сколько лет малышу?. Я могу предложить несколько популярных моделей.', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Приветствуем Вас в нашем магазине! Здесь осуществляются детские мечты!')
            bot.send_message(message.chat.id, url)
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.message:
        if call.data == 'one':
            bot.send_message(call.message.chat.id, one1)
            bot.send_message(call.message.chat.id, one2)
            bot.send_message(call.message.chat.id, one3)
        if call.data == 'two':
            bot.send_message(call.message.chat.id, two1)
            bot.send_message(call.message.chat.id, two2)
            bot.send_message(call.message.chat.id, two3)
        if call.data == 'three':
            bot.send_message(call.message.chat.id, three1)
            bot.send_message(call.message.chat.id, three2)
            bot.send_message(call.message.chat.id, three3)
        if call.data == 'al':
            bot.send_message(call.message.chat.id, te1)
        if call.data == 'sv':
            bot.send_message(call.message.chat.id, te2)
        if call.data == 'nk':
            bot.send_message(call.message.chat.id, te3)
bot.polling(none_stop=True)