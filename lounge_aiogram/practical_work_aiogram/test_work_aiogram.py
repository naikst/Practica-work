import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Задаем логирование чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Задаем токен бота
bot = Bot(token="7650675509:AAH4pXEjnyFnlSF0sFef4pi0NoCOlQOiYoU")

# Создаем диспетчер
dp = Dispatcher()

# Приветствие бота
@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer("Привет! Это бот, который отвечает на запросы.")

# Хэндлер на команду /test1
@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")

# Регистрация хэндлера cmd_test2
dp.message.register(cmd_test2, Command('test2'))

# Запуск процесса поллинга новых апдейтов
async def main():
    logging.info("Запуск бота...")
    await dp.start_polling(bot)
    logging.info("Бот запущен...")

if __name__ == "__main__":
    asyncio.run(main())