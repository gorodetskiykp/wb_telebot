"""Init wildberries telegram bot."""
# pylint: disable=E0401

import asyncio
import locale
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import creds
from handlers import router


async def main():
    """Create and configure telegram bot."""
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    bot = Bot(token=creds.TELE_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
