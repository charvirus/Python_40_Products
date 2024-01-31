from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, MessageHandler

token = "6554981239:AAEbHU0Oj2HhPYqgfixmkC-mQ6opaKrwo3k"


async def msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    if user_text == "안녕":
        await context.bot.send_message(chat_id=update.effective_chat.id,text="ㅎㅇ")
    elif user_text == "봇 조작":
        await context.bot.send_message(chat_id=update.effective_chat.id,text="어렵지? 계속 해봐 그 방법 밖에 없어")

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND),msg)

    application.add_handler(msg_handler)

    application.run_polling()
