import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Вставь сюда токен своего бота
API_TOKEN = "8260030545:AAG9hcUJyuyec6cORIETBwJIR2Yl3aRrIGo"

# URL вашего backend
BACKEND_URL = "http://127.0.0.1:8000"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Клавиатура
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Каталог")],
    ],
    resize_keyboard=True
)

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Это бот nolikby 🎉", reply_markup=main_kb)

# Каталог акций
@dp.message(lambda m: m.text == "📚 Каталог")
async def catalog(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{BACKEND_URL}/offers") as resp:
            if resp.status != 200:
                await message.answer("Ошибка backend.")
                return
            offers = await resp.json()
    if not offers:
        await message.answer("Нет акций.")
    else:
        for o in offers[:5]:  # первые 5 акций
            await message.answer(f"{o['id']}: {o['title']} — скидка {o['discount']}%")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
