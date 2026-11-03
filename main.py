import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest

from config import BOT_TOKEN
from utils.process_text import process_text

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.business_message(F.text)
async def handle_edit_text(message: Message):
    if not message.business_connection_id:
        return

    connection = await bot.get_business_connection(message.business_connection_id)

    if not message.from_user:
        return

    if message.from_user.id != connection.user.id:
        return

    new_text = process_text(message.text)

    try:
        await message.edit_text(new_text)
    except TelegramBadRequest as e:
        print(f"Telegram error: {e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())