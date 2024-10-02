import os
import asyncio
import dotenv

from bot import Bot

dotenv.load_dotenv('.env')

async def run_bot():
    async with Bot() as bot:
        await bot.start(os.getenv('TOKEN'))

def main():
    asyncio.run(run_bot())


if __name__ == '__main__':
    main()