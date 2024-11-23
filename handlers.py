"""Telegram bot handlers."""
# pylint: disable=E0401

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    """Handling /start command."""
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message(Command("zodiak"))
async def start_handler(msg: Message):
    """Handling /zodiak command."""
    await msg.answer("Введите дату рождения")

# TODO: добавить обработку даты + API календаря зодиака


@router.message()
async def message_handler(msg: Message):
    """Handling any user massage."""
    await msg.answer(f"Твой ID: {msg.from_user.id}")
