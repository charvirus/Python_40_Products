import asyncio
import telegram

token = "6554981239:AAEbHU0Oj2HhPYqgfixmkC-mQ6opaKrwo3k"
chat_id = "6885683105"


async def main():
    bot = telegram.Bot(token)
    async with bot:
        await bot.send_message(text="파이썬으로 보내는 메세지 입니다.", chat_id=chat_id)


if __name__ == '__main__':
    asyncio.run(main())
