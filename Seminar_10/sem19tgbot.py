import random
import telebot

bot = telebot.TeleBot("6137832927:AAHXJQkNaZ02sody4t0I1MSJrIMw4N5JmUc") # токен от botFather

sweets = 80
max_sweet = 28
user_turn = 0
bot_turn = 0
flag = ""

@bot.message_handler(commands = ["start"]) # если сообщение от пользователя = start, тогда запускается выполнение внутренней функции start()
def start(message):  # message = start - передаёт команду start в аргументы функции start
    global flag
    bot.send_message(message.chat.id, f"Приветствую вас в игре!")  # сообщение бота в чат
    bot.send_message(message.chat.id, f"Всего в игре {sweets} конфет") # сообщение пользователю сколько конфет в игре
    flag = random.choice(["user", "bot"])    # 1. кто ходит первым
    if flag == "user":  
        bot.send_message(message.chat.id, f"Первым ходите вы")  # 2. сообщение тому, кто первый ходит
        controller(message)
    else:
        bot.send_message(message.chat.id, f"Первым ходит бот")  # 2. сообщение тому, кто первый ходит
        controller(message)  # 3.

def controller(message):
    global flag
    if sweets > 0:
        if flag == "user":  # 4. 
            bot.send_message(message.chat.id, f"Ваш ход, введите количество кофет от 0 до {max_sweet}")  # 5.
            bot.register_next_step_handler(message, user_input) # 6. message передаётся в user_input, ждём сообщения от пользователя
        else:             
            bot_input(message) # ход бота
    else:
        flag = "user" if flag == "bot" else "bot"
        bot.send_message(message.chat.id, f"Победил {flag}!")


def bot_input(message):
    global sweets, bot_turn, flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
        if bot_turn == 0:
            bot_turn = 1 
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"осталось {sweets} конфет")
    flag = "user" if flag == "bot" else "bot"   # смена хода
    controller(message)


def user_input(message):
    global flag, user_turn, sweets
    user_turn = int(message.text) # 7. сообщение от пользователя
    sweets -= user_turn # 8. сколько осталось конфет
    bot.send_message(message.chat.id, f"осталось {sweets} конфет")
    flag = "user" if flag == "bot" else "bot"   # 9. смена хода
    controller(message)

bot.infinity_polling()
