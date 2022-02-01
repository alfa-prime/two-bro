from aiogram.dispatcher import FSMContext
from aiogram import types

from messages import replies
from keyboards import kb_generator

from _ds_bot.core import dp as dp_ds
from _py_bot.core import dp as dp_py

from .states import States


@dp_ds.callback_query_handler(text="offer", state='*')
@dp_py.callback_query_handler(text="offer", state='*')
async def ask_term_for_search(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(States.OFFER[0])
    await call.message.edit_text(replies.ask_term_to_offer)
    await call.answer()


@dp_ds.message_handler(state=States.OFFER)
@dp_py.message_handler(state=States.OFFER)
async def output_term_offer_result(message: types.Message, state: FSMContext):
    # todo: подумать надо ли проверять введеный термин или нет, если да, то как?
    # todo: дальнейшая логика -> отправка предложенного термина на модерацию
    offer_input_value = message.text
    keyboard = await kb_generator(["offer_again", "start_again"], row_width=2)
    await message.answer(replies.taken_term_to_offer.format(term=offer_input_value), reply_markup=keyboard)
