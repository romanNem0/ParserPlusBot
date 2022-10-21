from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters  # Способ создания приложений с указанием настроек
from selenium_parser import parse_hh
from config import auth_token

app = ApplicationBuilder().token(auth_token).build()

# Функция вызывается при получении сообщения
# upd - новая информация ТГ
# ctx - служебная информация
async def text_reply(upd: Update, _ctx):
    user_text = upd.message.text
    print(f"User: {user_text}")
    name = upd.message.from_user.full_name
    reply = f"Уважаемый {name}, запрос на получение количества вакансий '{user_text}' получен"
    print(reply)
    await upd.message.reply_text(reply)
    jobs_count = parse_hh(user_text)
    await upd.message.reply_text(f"Найдено вакансий: {jobs_count}, хорошего дня!")


# Handler - обработчик сообщения
handler = MessageHandler(filters.TEXT, text_reply)
# CommandHandler - для команд

# Прикрепляем обработчик к приложению
app.add_handler(handler)

app.run_polling()
