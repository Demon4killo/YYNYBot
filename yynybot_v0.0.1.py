import config
import telebot
import random



bot = telebot.TeleBot(config.token)
rand = int
rcount = int
msgcount = 0
totalMsg = "" 
Author = ""
CHANNEL_NAME = "@yynyChannel"


WELCOME = "Добро пожаловать в чатик с YYNY ботом \nДля помощи наберите ""/help"""
HELP = "\tВведите четыре вопроса любого содержания, после каждого нажимая \"Ввод\" \n\tБот отвечает на вопросы только Да или Нет, поэтому будьте бдительны \n\tПосле ввода последнего вопроса, Вам будет показан итог переписки\n\tНачать сначала \t- \t""/start"""

def get_author(message):
 if message.chat.username :
   Author =  message.chat.username
 elif message.chat.first_name and message.chat.last_name : 
   Author = message.chat.first_name + " " + message.chat.last_name
 elif message.chat.first_name and not message.chat.last_name : 
   Author = message.chat.first_name
 elif not message.chat.first_name and message.chat.last_name :
   Author = message.chat.last_name 
 else : 
   Author = "Unknown User" 
 return Author


@bot.message_handler(commands=["start"])
def send_welcome(message):
        global msgcount
        global totalMsg
        bot.send_message(message.chat.id, WELCOME)
        bot.send_message(message.chat.id, "Начинаем, \n Вопрос 1 из 4:")
        msgcount = 0
        totalMsg = ""
    

@bot.message_handler(commands=["help"])
def send_help(message):
         bot.send_message(message.chat.id, HELP)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    rand = random.randint(0,1)
    rcount = random.randint(0,44)
    global msgcount
    global totalMsg
    if rcount == 4 :
        totalMsg = totalMsg + ": " + message.text + "\nYYNY: Да от куда мне это знать \n \n"
        print ("Вы: \t" + message.text + "\n Bot: \t ХЗ \n ")
        msgcount += 1
        bot.send_message(message.chat.id, "\nВопрос " + str(msgcount+1) + " из 4:") if msgcount < 4 else bot.send_message(message.chat.id, "начнём с начала? ""/start") 
    else :
        if rand :
            #message.chat.username
            totalMsg = totalMsg + "Вы: " + message.text + "\nYYNYBot: Да\n \n"
            print ("Вы : \t" + message.text + "\n Bot: \t Да \n ")
            msgcount += 1
            bot.send_message(message.chat.id, "\nВопрос " + str(msgcount+1) + " из 4:") if msgcount < 4 else bot.send_message(message.chat.id, "начнём с начала? ""/start") 
        else :
            totalMsg = totalMsg + "Вы: " + message.text + "\nYYNYBot: Нет \n \n"
            print ("Вы: \t" + message.text + "\n Bot: \t Нет \n")
            msgcount += 1
            bot.send_message(message.chat.id, "\nВопрос " + str(msgcount+1) + " из 4:") if msgcount < 4 else bot.send_message(message.chat.id, "начнём с начала? ""/start") 
        if msgcount > 3 :
            if 0 <= rcount <= 16 :
                bot.send_message(CHANNEL_NAME, totalMsg + "\nAuthor: " +  get_author(message))
            bot.send_message(message.chat.id, "\n \n \t Вашы запросы обработаны ботом с глубоким усердием и в итоге чат принял следующую форму и содержание: \n \n" + totalMsg)    
            msgcount = 0
            totalMsg = ""
            print ("rcount = " + str(rcount) + " and Author: " + get_author(message))
            print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
                           
if __name__ == '__main__':
    bot.polling(none_stop=False)
