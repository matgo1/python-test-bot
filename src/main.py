import asycncio
import logging
import sys
from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

from src.configure import config


async def main():
    # Set logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelanames)s - %(message)s",
        stream=sys.stdout,
    )

    # Construct Bot
    bot = Bot(
        token=config.BOT_TOKEN.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    # Create Dispatcher
    dp = Dispatcher()

    # Include all all routers
    dp.include_router(get_handlers_routers())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)  # Start bot's polling

    except Exception as error:
        logging.error(f"Error in starting bot: {error}")

    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot was succesfully turned off")
