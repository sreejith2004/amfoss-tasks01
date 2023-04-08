import os
import telebot
import requests
import json
import csv
key = 'f2fe03'
# TODO: 1.1 Get your environment variables 
API_TOKEN = "6095592234:AAEfwSF0w62L1DhxB22aw8DTiEk16T9DxFs"
yourkey = os.getenv(key)
bot_id = os.getenv(key)
id_token = os.getenv('f2fe03')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message, '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie The Shawshank Redemption\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    text = message.text[7:]
    endpoint= f"http://www.omdbapi.com/?apikey={key}&t={text}"
    print(endpoint)
    r = requests.get(endpoint)
    data = r.json()
 
    print(data)
    img = data['Poster']
    data = "Title ="+ data['Title'] + " " +"Year="+ data['Year'] + " " +"IMDBRating=" + data['imdbRating']
    bot.send_message(message.chat.id, data)
    bot.send_photo(message.chat.id, img)
    
    with open('info.csv', 'w', encoding='UTF8',newline='')as f:
        writer = csv.writer(f)

    # write the data
        writer.writerow(data)

    
    # TODO: 1.2 Get movie information from the API
    # TODO: 1.3 Show the movie information in the chat window
    # TODO: 2.1 Create a CSV file and dump the movie information in it

  
@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    
    bot.send_document(message.chat.id, document=open('info.csv','rb'))

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')
    
bot.infinity_polling()
Footer

