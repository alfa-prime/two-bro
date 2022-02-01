from aiogram.dispatcher import FSMContext
from aiogram import types

from messages import replies
from keyboards import kb_generator

from _ds_bot.core import dp as dp_ds
from _py_bot.core import dp as dp_py

from .states import States


@dp_ds.callback_query_handler(text="search", state='*')
@dp_py.callback_query_handler(text="search", state='*')
async def ask_term_for_search(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.SEARCH[0])
    await call.message.edit_text(replies.ask_term_for_search)
    await call.answer()


@dp_ds.message_handler(state=States.SEARCH)
@dp_py.message_handler(state=States.SEARCH)
async def output_term_search_result(message: types.Message, state: FSMContext):
    # todo: подумать надо ли проверять введеный термин или нет, если да, то как?
    # todo: дальнейшая логика -> запрос к API -> получение и обработка ответа -> выдача ответа пользователю
    search_input_value = message.text
    keyboard = await kb_generator(["search_again", "start_again"], row_width=2)
    await message.answer(replies.taken_term_for_search.format(term=search_input_value), reply_markup=keyboard)

