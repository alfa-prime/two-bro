from collections import namedtuple
from typing import List

from aiogram import types

# Модель кнопки: Button(text = текст кнопки, action = текст, по которому отлавливается CallbackQuery)
Button = namedtuple('Button', 'text action')

# Все кнопки
BTNS: dict[str, Button] = {
    "start_again":   Button("К началу", "start"),
    "search":        Button("Поиск", "search"),
    "search_again":  Button("Новый поиск", "search"),
    "offer":         Button("Предложить", "offer"),
    "offer_again":   Button("Предложить еще", "offer"),
}


async def kb_generator(btn_lst: List[str], row_width: int = 1):
    btns = [types.InlineKeyboardButton(text=BTNS[btn].text, callback_data=BTNS[btn].action) for btn in btn_lst]
    keyboard = types.InlineKeyboardMarkup(row_width=row_width)
    keyboard.add(*btns)
    return keyboard
