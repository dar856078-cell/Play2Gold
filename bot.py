import os
from telegram import (Update, InlineKeyboardButton, InlineKeyboardMarkup,
                      WebAppInfo, MenuButtonWebApp)
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
URL = os.environ["WEBAPP_URL"]  # https://<user>.github.io/<repo>/


async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    kb = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🎮 Играть", web_app=WebAppInfo(url=URL))]]
    )
    await update.message.reply_text("Добро пожаловать в Play2Gold!", reply_markup=kb)


async def post_init(app: Application):
    await app.bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text="Играть", web_app=WebAppInfo(url=URL))
    )


def main():
    app = Application.builder().token(TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()


if __name__ == "__main__":
    main()
