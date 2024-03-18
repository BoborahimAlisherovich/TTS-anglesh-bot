import aiogram
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,InlineQuery,InlineQueryResultArticle,InputTextMessageContent
TOKEN = ""
import asyncio
import logging
import sys
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import time 
from text_to_speech import tts
TOKEN = "6796185877:AAE7DFikiOA-RW2YvKTnExVHuYqcMVPEAwc"

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    await message.answer(text="Assalomu alaykum! Bu bot Inglizcha so'zlarni ovozga aylantirib berishi mumkin!")



from aiogram.types import FSInputFile
@dp.message(F.text)
async def answer_translate(message: Message):
    tts(message.text)
    audio = FSInputFile(f"{message.text}.mp3")
    await message.answer_audio(audio=audio)


async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
