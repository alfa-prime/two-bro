from typing import Any

from aiogram.dispatcher import FSMContext
from aiogram import types

from messages import replies
from keyboards import kb_generator

from _ds_bot.core import dp as dp_ds
from _py_bot.core import dp as dp_py


async def get_user_firstname_or_username(message: Any) -> str:
    return message.username if not message.first_name else message.first_name


async def start_proccesing(message: types.Message, state: FSMContext):
    await state.finish()
    keyboard = await kb_generator(["search", "offer"], row_width=2)
    if message.from_user.is_bot:
        username = await get_user_firstname_or_username(message.chat)
        await message.edit_text(replies.begin.format(name=username), reply_markup=keyboard)
    else:
        username = await get_user_firstname_or_username(message.from_user)
        await message.answer(replies.begin.format(name=username), reply_markup=keyboard)


@dp_ds.message_handler(commands=['start'], state='*')
@dp_py.message_handler(commands=['start'], state='*')
async def command_start(message: types.Message, state: FSMContext):
    await start_proccesing(message, state)


@dp_ds.callback_query_handler(text="start", state="*")
@dp_py.callback_query_handler(text="start", state="*")
async def callback_start(call: types.CallbackQuery, state: FSMContext):
    await start_proccesing(call.message, state)
    await call.answer()
