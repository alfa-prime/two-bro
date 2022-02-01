from aiogram import types

from _ds_bot.core import dp as dp_ds
from _py_bot.core import dp as dp_py


@dp_ds.message_handler()
@dp_py.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
