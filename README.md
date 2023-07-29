# Text-to-Speech Telegram Bot

This repository contains a Python-based Telegram bot that converts text messages to speech and sends the audio back to the user. The bot utilizes the `telebot` library to interact with Telegram and the `pyttsx3` library to convert text to speech.

## Requirements

Before running the bot, make sure you have the following installed:

1. Python 3.x
2. `telebot` library: `pip install pyTelegramBotAPI`
3. `pyttsx3` library: `pip install pyttsx3`

## Setup

1. Clone this repository to your local machine.
2. Create a Telegram bot and obtain the API token. You can create a new bot and get the token from the [BotFather](https://core.telegram.org/bots#botfather).
3. Replace the `telebot.TeleBot` line with your Telegram bot API token in the `bot.py` file:

```python
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_API_TOKEN')
```

## How It Works

The bot is designed to convert any text message sent to it into speech. It uses the `pyttsx3` library to generate the speech and `telebot` to interact with Telegram.

### Starting the Bot

The bot is set up to respond to the `/start` command. When a user sends `/start`, the bot replies with a welcome message.

### Converting Text to Speech

For any other text messages sent by the user, the bot converts the text to speech using the `pyttsx3` library. The generated audio is saved as `audio.mp3`.

### Sending the Audio to the User

After converting the text to speech, the bot sends the audio file back to the user. It reads the `audio.mp3` file, converts it into bytes, and sends it as an audio message to the user using the `bot.send_audio()` method.

## Usage

1. Run the `bot.py` script to start the Telegram bot.
2. Open the Telegram app and find your bot.
3. Send any text message to the bot.
4. The bot will convert the text to speech and send the audio back to you.

## Important Note

Please be mindful of the usage of this bot and respect the privacy and preferences of other users. Avoid using the bot for any malicious or harmful purposes.

## Contributions

Contributions to this project are welcome! If you find any issues or have ideas to improve the bot, feel free to open an issue or submit a pull request.

## Disclaimer

This text-to-speech bot is for educational and demonstrative purposes only. It utilizes the `pyttsx3` library for speech synthesis, and the quality of the generated speech depends on the capabilities of the underlying text-to-speech engine used by `pyttsx3`. The bot might not always produce human-like or perfect speech. Use it responsibly and avoid using it for any harmful or offensive content.

Happy chatting and listening! 🗣️🎧
