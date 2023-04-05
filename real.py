import telebot
import pyttsx3
from io import BytesIO

bot = telebot.TeleBot('6157727329:AAFS-3uUSqmeuU_1Y8s-RaEsyqMl5ori-X8')
engine = pyttsx3.init()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi, welcome to the text-to-speech bot!')

@bot.message_handler(func=lambda message: True)
def text_to_speech(message):
    # Convert text to speech
    engine.save_to_file(message.text, 'audio.mp3')
    engine.runAndWait()
    # Send audio file back to the user
    with open('audio.mp3', 'rb') as audio_file:
        audio_bytes = audio_file.read()
    audio_io = BytesIO(audio_bytes)
    audio_io.seek(0)
    bot.send_audio(chat_id=message.chat.id, audio=audio_io)

bot.polling()