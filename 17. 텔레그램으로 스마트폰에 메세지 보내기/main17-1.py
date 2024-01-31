import telegram
import asyncio

token = "6554981239:AAEbHU0Oj2HhPYqgfixmkC-mQ6opaKrwo3k"


async def main():
    bot = telegram.Bot(token)
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
