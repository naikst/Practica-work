import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from lounge_aiogram.practical_work_aiogram.api_token import TOKEN

# Задаем логирование чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Задаем токен бота
bot = Bot(TOKEN)

# Создаем диспетчер
dp = Dispatcher()


TEXT = """
/help - Выводит информацию о боте
/start - запуск бота
"""

# Приветствие бота
@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer("Привет! Это бот, который отвечает на запросы.")

# Хэндлер на команду
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.reply(TEXT)

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
    await bot.delete_webhook(drop_pending_updates=True) # Указываем что ранние были запроса
    # от пользователя не будет при запуске обрабатывать запросы ранее которые были

if __name__ == "__main__":
    asyncio.run(main())