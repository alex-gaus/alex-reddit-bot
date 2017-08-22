import requests
import telegram
from credentials import telegram_bot_token

bot = telegram.Bot(token=telegram_bot_token)


url="https://api.telegram.org/bot%s/getMe"%(telegram_bot_token)
response=requests.get(url)
print(bot.get_me())
updates = bot.get_updates()
print([u.message.text for u in updates])

chat_id = bot.get_updates()[-1].message.chat_id
bot.send_message(chat_id=chat_id, text="Das wäre verrückt wenn das hier funktioniert!")
bot.send_photo(chat_id=chat_id, photo=open('downloads/#1.jpg', 'rb'))


bot.send_photo(chat_id=eli, photo=open('downloads/alex.jpg', 'rb'))