import telebot
import pyttsx3
import requests

# Create an instance of the bot
bot = telebot.TeleBot('5129018945:AAFElYVuMMAoGfylZYMAMsrFs5kLCFnhYwg')

# Radio stream URL
stream_url = 'http://www.radioindia.in/embed/radio-mirchi-983-fm-395596'

# Initialize pyttsx3
engine = pyttsx3.init()

# Start the radio stream
def start_radio():
    r = requests.get(stream_url, stream=True)
    for block in r.iter_content(1024):
        engine.say(block.decode())
        engine.runAndWait()

# Handler for the '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Radio started!")
    start_radio()

# Handler for the '/stop' command
@bot.message_handler(commands=['stop'])
def stop(message):
    bot.reply_to(message, "Radio stopped!")
    engine.stop()

# Start the bot
bot.polling()
