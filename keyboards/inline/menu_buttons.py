from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import my_callback

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
            [InlineKeyboardButton(text="Дисплей",callback_data=my_callback.new(item_name="LCD")),
            InlineKeyboardButton(text="Корпус",callback_data=my_callback.new(item_name="Корпуса")),
            InlineKeyboardButton(text="Стекло",callback_data=my_callback.new(item_name="Стёкла")),
            ],
            [
            InlineKeyboardButton(text="Разъем",callback_data=my_callback.new(item_name="Разъёмы")),
            InlineKeyboardButton(text="АКБ",callback_data=my_callback.new(item_name="АКБ")),
            InlineKeyboardButton(text="Химия",callback_data=my_callback.new(item_name="Химия"))
            ]
    ]
)