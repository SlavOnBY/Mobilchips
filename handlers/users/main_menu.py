from aiogram import Dispatcher,types

from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.menu_buttons import menu_keyboard
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from aiogram.types.web_app_info import WebAppInfo

from code import main_code

@dp.message_handler(commands=['start','help'])
async def start(message : types.message):

    #await bot.send_message(message.chat.id, "Привет, {0.first_name}! Я бот для поиска в прайсе Mobilchips. \n"
    #                       "Для поиска просто наберите модель латинскими буквами".format(message.from_user))
    await message.answer("test",reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(text="test", web_app=WebAppInfo(url="https://mobilchips.by/"))))



@dp.message_handler(content_types=['text'])
async def search(message: Message, state: FSMContext):
    model = message.text.upper()
    async with state.proxy() as data:
        data['model'] = model

    await bot.send_message(message.chat.id, "Что будем искать {0.first_name}?".format(message.from_user),
                           reply_markup=menu_keyboard)


@dp.callback_query_handler(text_contains="LCD")
async def choose_lcd(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    async with state.proxy() as data:
        model = data['model']
        item_name = callback_data.split(":")[-1]
    result = main_code(model, item_name)
    #print(result)
    if result == 0:
        await call.message.answer(text='Не повезло ' + '😭\n' +
                                       'Попробуйте изменить данные поиска')
    else:
        await state.finish()
        await call.message.answer_photo(photo=types.InputFile('table_plotly.png'), disable_notification= True)



@dp.callback_query_handler(lambda call: call.data == "name:Стёкла")
async def choose_glass(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    async with state.proxy() as data:
        model = data['model']
        item_name = callback_data.split(":")[-1]
    result = main_code(model, item_name)
    if result == 0:
        await call.message.answer(text='Не повезло ' + '😭\n' +
                                       'Попробуйте изменить данные поиска')
    else:
        await state.finish()
        await call.message.answer_photo(photo=types.InputFile('table_plotly.png'))


@dp.callback_query_handler(text_contains="АКБ")
async def choose_akb(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    async with state.proxy() as data:
        model = data['model']
        item_name = callback_data.split(":")[-1]
    result = main_code(model, item_name)
    if result == 0:
        await call.message.answer(text='Не повезло ' + '😭\n' +
                                       'Попробуйте изменить данные поиска')
    else:
        await state.finish()
        await call.message.answer_photo(photo=types.InputFile('table_plotly.png'))



@dp.callback_query_handler(text_contains="Разъёмы")
async def choose_conn(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    async with state.proxy() as data:
        model = data['model']
        item_name = callback_data.split(":")[-1]
    result = main_code(model, item_name)
    if result == 0:
        await call.message.answer(text='Не повезло ' + '😭\n' +
                                       'Попробуйте изменить данные поиска')
    else:
        await state.finish()
        await call.message.answer_photo(photo=types.InputFile('table_plotly.png'))


@dp.callback_query_handler(text_contains="Корпуса")
async def choose_korp(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    async with state.proxy() as data:
        model = data['model']
        item_name = callback_data.split(":")[-1]
    result = main_code(model, item_name)
    if result == 0:
        await call.message.answer(text='Не повезло ' + '😭\n' +
                                       'Попробуйте изменить данные поиска')
    else:
        await state.finish()
        await call.message.answer_photo(photo=types.InputFile('table_plotly.png'))


@dp.callback_query_handler(text_contains="Химия")
async def choose_chem(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    callback_data = call.data
    async with state.proxy() as data:
        model = data['model']
        item_name = callback_data.split(":")[-1]
    result = main_code(model, item_name)
    if result == 0:
        await call.message.answer(text='Не повезло ' + '😭\n' +
                                       'Попробуйте изменить данные поиска\n'
                                       'Например A125, флюс, Sigma и т.д')
    else:
        await state.finish()
        await call.message.answer_photo(photo=types.InputFile('table_plotly.png'))




