from telethon import TelegramClient

# подключение к Telegram API
api_id = int
api_hash = ''
client = TelegramClient('session_name', api_id, api_hash)

# отправка сообщения пользователю
async def send_telegram_message(user_id, message):
    await client.send_message(user_id, message)

# запуск клиента и отправка сообщения
with client:
    x = 123123123
    y = 'Hello!'
    client.loop.run_until_complete(send_telegram_message(x, y))