"""Telegram bot handlers."""
# pylint: disable=E0401,R0903

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from tools.zodiac import fetch_zodiac_sign


class ZodiacDate(StatesGroup):
    """Zodiac case steps."""
    inputting_zodiac_date = State()


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    """Handling /start command."""
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(StateFilter(None), Command("zodiac"))
async def zodiac_handler(msg: Message, state: FSMContext):
    """Handling /zodiac command."""
    await msg.answer("Введите дату рождения (в формате дд.мм.гггг)")
    # добавить от пользователя ожидание msg
    await state.set_state(ZodiacDate.inputting_zodiac_date)


@router.message(ZodiacDate.inputting_zodiac_date)
async def process_zopdiac_date(msg: Message, state: FSMContext):
    """Fetch zodiac sign."""
    sign = fetch_zodiac_sign(msg.text)
    await state.clear()
    if sign:
        await msg.answer(sign)
    else:
        await msg.answer("Что-то не так с датой")


@router.message()
async def message_handler(msg: Message):
    """Handling any user massage."""
    await msg.answer(f"Твой ID: {msg.from_user.id}")
