from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb

class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    gender = State()
    region = State()
    photo = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type=="private":
        await FSMAdmin.name.set()
        await message.answer("Как тебя зовут?", reply_markup=client_kb.gender_markup)
    else:
        await message.answer('Пиши в личку!')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id']=message.from_user.id
        data['username']=message.from_user.username
        data['name']=message.text
    await FSMAdmin.next()
    await message.answer("Сколько лет?")


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши только числа")
    elif not 18<int(message.text)<70:
        await message.answer("Не проходишь по возрасту")
    else:
        async with state.proxy() as data:
            data['age']=message.text
        await FSMAdmin.next()
        await message.answer("Какой пол?",
                             reply_markup=client_kb.gender_markup)


async def load_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender']=message.text
    await FSMAdmin.next()
    await message.answer("Откуда ты?", reply_markup=client_kb.gender_markup)


async def load_region(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['region']=message.text
    await FSMAdmin.next()
    await message.answer("Отправь фото?")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo']=message.photo[0].file_id
        await message.answer_photo(
            data['photo'],
            caption=f'{data["name"]} {data["age"]} {data["gender"]} {data["region"]} \n\n{data["username"]}')
    await FSMAdmin.next()
    await message.answer("Всё верно?",
                         reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await message.answer("Great")
    elif message.text.lower() == "нет":
        await FSMAdmin.name.set()
        await message.answer("Как тебя зовут?", reply_markup=client_kb.gender_markup)
    else:
        await message.answer("Не понял")

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state= await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Ваша анкета отменена")

def register_handlers_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, Text(equals="cancel", ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_gender, state=FSMAdmin.gender)
    dp.register_message_handler(load_region, state=FSMAdmin.region)
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(submit, state=FSMAdmin.submit)

