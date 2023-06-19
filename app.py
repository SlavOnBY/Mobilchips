#from loader import bot, Dispatcher
from code import file_load
#async def on_shutdown(dp):
#    await bot.close()

if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    file_load()
    executor.start_polling(dp, skip_updates=True)

