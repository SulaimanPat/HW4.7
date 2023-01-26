from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from config import ADMINS

class FSMMentor(StatesGroup):
    name = State()
    direction = State()
    age_mentor = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("You cannot register any mentors")
    else:
        await FSMMentor.name.set()




async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id']=message.message_id
        data['name']=message.text
    await FSMMentor.next()
    await message.answer("Какое направление у ментора?")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction']=message.text
    await FSMMentor.next()
    await message.answer("Сколько лет ментору?")


async def load_age_mentor(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши только числа")
    elif not 15<int(message.text)<70:
        await message.answer("Не проходишь по возрасту")
    else:
        async with state.proxy() as data:
            data['age_mentor']=message.text
        await FSMMentor.next()
        await message.answer("Какая группа?"
                             )


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group']=message.text
        await message.answer(f'{data["id"]} {data["name"]} {data["direction"]} '
                             f'{data["age_mentor"]} \n\n{data["group"]}')
    await FSMMentor.next()
    await message.answer("Все верно?")


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await message.answer("Great")
    elif message.text.lower() == "заново":
        await FSMMentor.name.set()
        await message.answer("Имя ментора?")
    else:
        await message.answer("Не понял")

async def cancel_regmentor(message: types.Message, state: FSMContext):
    current_state= await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ваша анкета отменена")

def register_handlers_admin_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_regmentor, Text(equals="cancel", ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['regmentor'])
    dp.register_message_handler(load_name, state=FSMMentor.name)
    dp.register_message_handler(load_direction, state=FSMMentor.direction)
    dp.register_message_handler(load_age_mentor, state=FSMMentor.age_mentor)
    dp.register_message_handler(load_group, state=FSMMentor.group)
    dp.register_message_handler(submit, state=FSMMentor.submit)

