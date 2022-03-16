from datetime import date
import os
import telebot
from geopy.geocoders import Nominatim
import json
# from translate import Translator

# translator = Translator(to_lang="Russian")

# geolocator = Nominatim(user_agent="geoapiExercises")

# bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))
TOKEN = '5174367037:AAFh8m-c7gIoVO6_H-V9hMBeLqOVjnadXfA'

bot = telebot.TeleBot(TOKEN)

bottons = {
    "Оставить отзыв": None,
    "Меню": None,
    "Мои заказы": None,
    "Настройки": None,
    "Отправить геолокацию": None,
    "Да": None,
    "Мои адреса": None,
    "Изменить язык": None,
    
}

lang = {
    "russian": "Русский",
    "uzbek": None,
}

def add_to_json(id, username, review):
    info = {
        id:{
            username:
                review
        }
    }
    with open(f"{id}.json", "w") as file:
        json.dump(info, file, indent=4)


@bot.message_handler(commands=["start"])
def start_message(message):
    reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.row(
        telebot.types.KeyboardButton(
            text="🍴 Меню"
        )
    )
    reply_markup.row(
        telebot.types.KeyboardButton(
            text="🛍 Мои заказы"
        )
    )
    
    reply_markup.add(
        *[
            telebot.types.KeyboardButton(text="✍️ Оставить отзыв"),
            telebot.types.KeyboardButton(text="⚙️ Настройки")
        ]
    )
    
    username = message.from_user.first_name
    ans_uzb = f"👋Assalomu alaykum {username}\n"
    ans_uzb += f"Quyidagilardan birini tanlang 👇"

    ans_r = f"Здравствуйте {username}\n"
    ans_r += f"Выберите одно из следующих 👇"
    bot.send_message(message.from_user.id, ans_r, reply_markup=reply_markup)
    
@bot.message_handler(func=lambda message:True)
def echo_all(message):
    fikr = False
    if lang["russian"]:
        if message.text == "🍴 Меню":
            reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2 ,resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(text="📍 Отправить геолокацию", request_location=True)
            )
            reply_markup.add(
                telebot.types.KeyboardButton(text="🗺 Мои адреса"),
                telebot.types.KeyboardButton(text="⬅️ Назад")
            )
            
            bot.send_message(message.from_user.id, "Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=reply_markup)
            
        elif message.text == "🗺 Мои адреса":
            reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2 ,resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(text="📍 Отправить геолокацию", request_location=True)
            )
            reply_markup.add(
                telebot.types.KeyboardButton(text="🗺 Мои адреса"),
                telebot.types.KeyboardButton(text="⬅️ Назад")
            )
            bot.send_message(message.from_user.id, "У вас нет адреса.", reply_markup=reply_markup)
            
        elif message.text == "🛍 Мои заказы":
            bot.send_message(message.from_user.id, "Вы совсем ничего не заказали.")
        

        elif message.text == "⚙️ Настройки":
            
            reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(text="Изменить язык")
            )
            reply_markup.row(
                telebot.types.KeyboardButton(text="⬅️ Назад")
            )
            
            bot.send_message(message.from_user.id,"*Выберите действие:*", parse_mode="markdown", reply_markup=reply_markup)
            
        elif message.text == "Изменить язык":
            reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            reply_markup.add(*[
                telebot.types.KeyboardButton(text="🇷🇺 Русский"),
                telebot.types.KeyboardButton(text="🇺🇿 O'zbekcha")
            ])
            reply_markup.row(
                telebot.types.KeyboardButton(text="⬅️ Назад")
            )
            bottons["Изменить язык"] = "Изменить язык"
            bot.send_message(message.from_user.id, "*Выберите язык*", parse_mode="markdown", reply_markup=reply_markup)
            
        elif message.text == "🇷🇺 Русский":
            lang["russian"] = "🇷🇺 Русский"
            lang["uzbek"] = None
                        
            reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(text="Изменить язык")
            )
            reply_markup.row(
                telebot.types.KeyboardButton(text="⬅️ Назад")
            )
            
            bot.send_message(message.from_user.id, "*✅ Готово*", parse_mode="markdown",reply_markup=reply_markup)
            
        elif message.text == "🇺🇿 O'zbekcha":
            lang["uzbek"] = "🇺🇿 O'zbekcha"
            lang["russian"] = None
            reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(text="Tilni o'zgartirish")
            )
            reply_markup.row(
                telebot.types.KeyboardButton(text="⬅️ Ortga")
            )
            
            bot.send_message(message.from_user.id, "*✅ Tayyor*", parse_mode="markdown", reply_markup=reply_markup )
        elif message.text == "❌ Нет":
            reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(text="📍 Отправить геолокацию", request_location=True)
                )
            reply_markup.add(
                telebot.types.KeyboardButton(text="🗺 Мои адреса"),
                telebot.types.KeyboardButton(text="⬅️ Назад")
            )
            bot.send_message(message.from_user.id, "Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=reply_markup)
            
        elif message.text == "✅ Да":
            reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            reply_markup.add(
                *[
                    telebot.types.KeyboardButton(text="Сет"),
                    telebot.types.KeyboardButton(text="Лаваш"),
                    telebot.types.KeyboardButton(text="Шаурма"),
                    telebot.types.KeyboardButton(text="Донар"),
                    telebot.types.KeyboardButton(text="Бургер"),
                    telebot.types.KeyboardButton(text="Хот-дог"),
                    telebot.types.KeyboardButton(text="Десерты"),
                    telebot.types.KeyboardButton(text="Напитки"),
                    telebot.types.KeyboardButton(text="Гарнир")
                    
                ]
            )
            reply_markup.add(
                *[
                    telebot.types.KeyboardButton(text="📥 Корзинка"),
                    telebot.types.KeyboardButton(text="⬅️ Назад")
                ]
            )
            
            bottons["Да"] = "Да"
            bot.send_message(message.from_user.id, "Выберите категорию.", reply_markup=reply_markup)        
        elif message.text == "⬅️ Назад":
            if bottons["Да"]:
                reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                reply_markup.row(
                    telebot.types.KeyboardButton(text="📍 Отправить геолокацию", request_location=True)
                    )
                reply_markup.add(
                    telebot.types.KeyboardButton(text="🗺 Мои адреса"),
                    telebot.types.KeyboardButton(text="⬅️ Назад")
                )
                bottons["Да"] = None   
                bot.send_message(message.from_user.id, "Отправьте 📍 геолокацию или выберите адрес доставки", reply_markup=reply_markup)

            elif bottons["Изменить язык"]:
                reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
                reply_markup.row(
                    telebot.types.KeyboardButton(text="Изменить язык")
                )
                reply_markup.row(
                    telebot.types.KeyboardButton(text="⬅️ Назад")
                )
                bottons["Изменить язык"] = None
                bot.send_message(message.from_user.id, "*Выберите действия:*", parse_mode="markdown",reply_markup=reply_markup)
                
            else:
                reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                reply_markup.row(
                    telebot.types.KeyboardButton(
                        text="🍴 Меню"
                    )
                )
                reply_markup.row(
                    telebot.types.KeyboardButton(
                        text="🛍 Мои заказы"
                    )
                )
                
                reply_markup.add(
                    *[
                        telebot.types.KeyboardButton(text="✍️ Оставить отзыв"),
                        telebot.types.KeyboardButton(text="⚙️ Настройки")
                    ]
                )
                bot.send_message(message.from_user.id, "Выберите одно из следующих 👇", reply_markup=reply_markup) 
            
        elif message.text == "✍️ Оставить отзыв":
            reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            reply_markup.add(
                telebot.types.KeyboardButton(text="⬅️ Назад")
            )
            bottons["Оставить отзыв"] = "✍️ Оставить отзыв"
            bot.send_message(message.from_user.id, "Отправьте ваши отзывы", reply_markup=reply_markup)
            
        elif message.text and bottons["Оставить отзыв"]:
            reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(
                    text="🍴 Меню"
                )
            )
            reply_markup.row(
                telebot.types.KeyboardButton(
                    text="🛍 Мои заказы"
                )
            )
            
            reply_markup.add(
                *[
                    telebot.types.KeyboardButton(text="✍️ Оставить отзыв"),
                    telebot.types.KeyboardButton(text="⚙️ Настройки")
                ]
            )
            id = message.from_user.id
            username = message.from_user.first_name
            text = message.text
            bottons["Оставить отзыв"] = None
            add_to_json(id, username, text)
            bot.send_message(message.from_user.id, "Спасибо за ваш отзыв", reply_markup=reply_markup)
        
        
        else:
            reply_markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            reply_markup.row(
                telebot.types.KeyboardButton(
                    text="🍴 Меню"
                )
            )
            reply_markup.row(
                telebot.types.KeyboardButton(
                    text="🛍 Мои заказы"
                )
            )
            
            reply_markup.add(
                *[
                    telebot.types.KeyboardButton(text="✍️ Оставить отзыв"),
                    telebot.types.KeyboardButton(text="⚙️ Настройки")
                ]
            )
                        
            bot.send_message(message.from_user.id, "Выберите одно из следующих 👇", reply_markup=reply_markup) 
            
        
# @bot.message_handler(content_type=['location'])

@bot.message_handler(content_types=['location'])
def handle_location(message):
    Longitude = str(message.location.longitude)
    Latitude = str(message.location.latitude)
    
    # location = geolocator.reverse(Latitude+","+Longitude)
    geoLoc = Nominatim(user_agent="GetLoc")
    
    locname = geoLoc.reverse(Latitude+","+Longitude)
    
    address = locname.address
    reply_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    reply_markup.add(
        telebot.types.KeyboardButton(text="❌ Нет"),
        telebot.types.KeyboardButton(text="✅ Да")
    )
    reply_markup.row(
        telebot.types.KeyboardButton(text="⬅️ Назад")
    )
    text = f"Адрес, по которому вы хотите заказать:{address}.\nВы подтверждаете этот адрес?"
    bot.send_message(message.from_user.id, text=text, reply_markup=reply_markup)

bot.polling(non_stop=True)