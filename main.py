from pyrogram import Client, filters
from pyrogram.enums import ChatAction
import asyncio

# Данные для авторизации (получить на my.telegram.org)
API_ID = 1234567 
API_HASH = 1234567


app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

print("Бот запускается... Ожидание сообщений.")

@app.on_message(filters.private & ~filters.me)
async def smart_reply(client, message):
    text = message.text.lower() if message.text else ""
    
    if "купить" in text or "заказать" in text:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        await asyncio.sleep(2) # Пауза для естественности
        
        await message.reply(
            "Здравствуйте! Рад, что вас заинтересовали услуги. \n"
            "Вот моё портфолио: https://github.com \n"
            "Какая именно услуга вас интересует?"
        )

    elif "цена" in text or "сколько стоит" in text:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        await asyncio.sleep(1.5)
        await message.reply("Стоимость зависит от объема работы. Опишите вашу задачу, и я сориентирую по цене.")

    else:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        await asyncio.sleep(3)
        await message.reply("Принял ваше сообщение! Скоро освобожусь и отвечу вам лично. 🤖")

if __name__ == "__main__":
    app.run()
