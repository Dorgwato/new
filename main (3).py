import config
import logging
import asyncio
import random
import datetime
from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from base import SQL  # подключение класса SQL из файла base

db = SQL('db.db')  # соединение с БД
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

#Клавиатуры
buttons_back = [
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
kb_back = InlineKeyboardMarkup(inline_keyboard=buttons_back)

buttons_back1 = [
        [InlineKeyboardButton(text="Назад", callback_data="back1")]
    ]
kb_back1= InlineKeyboardMarkup(inline_keyboard=buttons_back1)

buttons_back2 = [
        [InlineKeyboardButton(text="Назад", callback_data="back2")]
    ]
kb_back2= InlineKeyboardMarkup(inline_keyboard=buttons_back2)

buttons_back3 = [
        [InlineKeyboardButton(text="Назад", callback_data="back3")]
    ]
kb_back3= InlineKeyboardMarkup(inline_keyboard=buttons_back3)

buttons_back4 = [
        [InlineKeyboardButton(text="Назад", callback_data="back4")]
    ]
kb_back4= InlineKeyboardMarkup(inline_keyboard=buttons_back4)

buttons_level = [
        [InlineKeyboardButton(text="Простой", callback_data="easy")],
        [InlineKeyboardButton(text="Средний", callback_data="medium"),
        InlineKeyboardButton(text="Сложный", callback_data="hard")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
kb_level = InlineKeyboardMarkup(inline_keyboard=buttons_level)

buttons_task = [
        [InlineKeyboardButton(text="Задачи на эрудицию", callback_data="erodition")],
        [InlineKeyboardButton(text="Задачи на реакцию веществ", callback_data="reaction"),
        InlineKeyboardButton(text="Задачи из ОГЭ", callback_data="OGE")],
        [InlineKeyboardButton(text="Учебные материалы", callback_data="link")],
        [InlineKeyboardButton(text="Назад", callback_data="back1")]
    ]
kb_task = InlineKeyboardMarkup(inline_keyboard=buttons_task)

buttons_tip = [
        [InlineKeyboardButton(text="16 задача", callback_data="16task")],
        [InlineKeyboardButton(text="18 задача", callback_data="18task"),
        InlineKeyboardButton(text="19 задача", callback_data="19task")],
        [InlineKeyboardButton(text="Назад", callback_data="back2")]
    ]
kb_tip = InlineKeyboardMarkup(inline_keyboard=buttons_tip)
buttons_subject = [
        [InlineKeyboardButton(text="Химия", callback_data="chemistry")],
        [InlineKeyboardButton(text="Биология", callback_data="biology")],
        [InlineKeyboardButton(text="Установить время напоминания", callback_data="time")],
        [InlineKeyboardButton(text="Мои очки", callback_data="score"),
        InlineKeyboardButton(text="Обратная связь", callback_data="calback")]
    ]
kb_subject = InlineKeyboardMarkup(inline_keyboard=buttons_subject)

buttons_biology = [
        [InlineKeyboardButton(text="9 задача", callback_data="9taskBiology")],
        [InlineKeyboardButton(text="17 задача", callback_data="17taskBiology"),
        InlineKeyboardButton(text="19 задача", callback_data="19taskBiology")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]
kb6 = InlineKeyboardMarkup(inline_keyboard=buttons_biology)
async def send_message():
    while True:
        users = db.get_all_users()
        current_time = datetime.datetime.now().strftime("%H:%M")
        for i in range(len(users)):
            if current_time == users[i][4]:
                await bot.send_message(chat_id=users[i][0], text="Пора заниматься, для начала занятия напиши: /start")
        await asyncio.sleep(59)  # Ожидание 60 секунд перед проверкой времени снова


@dp.message()
async def start(message):
    global answer
    id = message.from_user.id
    if not db.user_exist(id):#если пользователя нет в бд
        db.add_user(id)#добавляем
        await message.answer("Привет, это бот по химии и биологии, он поможет тебе со сдачей экзаменов."
                         " Для начала выбери предмет", reply_markup=kb_subject)
    status = db.get_status(id)
    if message.text == "/start" or status == 0:
        db.update_status(id, 0)
        await message.answer("Привет, это бот по химии и биологии, он поможет тебе со сдачей экзаменов."
                         " Для начала выбери предмет", reply_markup=kb_subject)
    status = db.get_status(id)

    if status == 1:
        ans = message.text.replace(".",",")
        ans = ans.lower()
        if ans == answer:
            score = db.get_score(id)
            db.update_score(id, score+1)
            db.update_status(id, 0)
            await message.answer("Молодец, ты ответил верно", reply_markup=kb_task)
        else:
            await message.answer("Неверно, попробуй еще раз")
    #Выбор времени получения напоминания
    if status == 5:
        tr = 0
        if  len(message.text) == 5 and ':' in message.text:
            ans1 = message.text.split(':')
            if len(ans1) == 2:
                try:
                    if  0 <= int(ans1[0]) <= 23:
                        tr = tr+1
                    else:
                        await message.answer("Неправильный формат времени, попробуй еще раз", reply_markup=kb_back)
                    if  0 <= int(ans1[1]) <= 59:
                        tr = tr + 1
                    else:
                        await message.answer("Неправильный формат времени, попробуй еще раз", reply_markup=kb_back)
                except:
                    await message.answer("Неправильный формат времени, попробуй еще раз", reply_markup=kb_back)
        else:
            await message.answer("Неправильный формат времени, попробуй еще раз", reply_markup=kb_back)
        if tr == 2:
            db.update_time(id, message.text)
            db.update_status(id, 0)
            await message.answer(f"Все прошло успешно, вам будет приходить напоминание в {message.text}", reply_markup=kb_back)


#когда пользователь нажал на inline кнопку
@dp.callback_query()
async def start_call(call):
    global answer
    id = call.from_user.id
    if not db.user_exist(id):#если пользователя нет в бд
        db.add_user(id)#добавляем
#Отправка ссылки на доп. материал
    if call.data == "link":
        link = db.get_all_link()
        s = "Ссылки на дополнительные материалы: \n"
        for i in range(len(link)):
            s+= f"{link[i][1]} \n {link[i][2]}\n"
        await call.message.edit_text(s, reply_markup=kb_back2)

#Обратная связь
    if call.data == "calback":
        await call.message.edit_text("Если появились вопросы, можешь задать их нам: @chebupelka_maller", reply_markup=kb_back)

    if call.data == "time":
        db.update_status(id, 5)
        await call.message.edit_text("Для установки времени, отправь время в формате 00:00", reply_markup=kb_back)

#Счет пользователя
    if call.data == "score":
        score = db.get_score(id)
        await call.message.edit_text(f"Ваш счет: {score}", reply_markup=kb_back)

#Возвращение на выбор предмета
    if call.data == "back":
        db.update_status(id, 0)
        await call.message.edit_text("Выбери предмет", reply_markup=kb_subject)

#Возвращение на выбор уровня сложности
    if call.data == "back1":
        db.update_status(id, 0)
        await call.message.edit_text("Выбери сложность", reply_markup=kb_level)

#Возвращение на выбор задания по химии
    if call.data == "back2":
        db.update_status(id, 0)
        await call.message.edit_text("Выбери тип задачи", reply_markup=kb_task)

#Возвращение на выбор задания из ОГЭ по химии
    if call.data == "back3":
        db.update_status(id, 0)
        await call.message.edit_text("Выбери тип задачи", reply_markup=kb_tip)

#Возвращение на выбор задания из ОГЭ по биологии
    if call.data == "back4":
        db.update_status(id, 0)
        await call.message.edit_text("Выбери тип задачи", reply_markup=kb6)
#Chemistry
    if call.data == "chemistry":
        await call.message.edit_text("Выбери сложность", reply_markup=kb_level)
#Выбор сложности
    if call.data == "easy":
        db.update_level(id, level="easy")
        await call.message.edit_text("Выбери тип задачи", reply_markup=kb_task)
    if call.data == "medium":
        db.update_level(id, level="medium")
        await call.message.edit_text("Выбери тип задачи", reply_markup=kb_task)
    if call.data == "hard":
        db.update_level(id, level="hard")
        await call.message.edit_text("Выбери тип задачи", reply_markup=kb_task)
    if call.data == "OGE":
        await call.message.edit_text("Выбери номер задания из ОГЭ", reply_markup=kb_tip)
#Биология
    if call.data == "biology":
        await call.message.edit_text("Выбери номер задания из ОГЭ", reply_markup=kb6)
#Задания по химии
    if call.data == "reaction":
        level = db.get_level(id)
        n = random.randint(1, 3)
        if level == "easy":
            db.update_status(id, 1)
            task = db.get_react_easy(n)
            answer = str(db.get_react_answer_easy(n))
            await call.message.edit_text(f"{task}", reply_markup=kb_back2)
        if level == "medium":
            db.update_status(id, 1)
            task = db.get_react_medium(n)
            answer = str(db.get_react_answer_medium(n))
            await call.message.edit_text(f"{task}", reply_markup=kb_back2)
        if level == "hard":
            db.update_status(id, 1)
            task = db.get_react_hard(n)
            answer = str(db.get_react_answer_hard(n))
            await call.message.edit_text(f"{task}", reply_markup=kb_back2)
    if call.data == "erodition":
        n = random.randint(1, 5)
        level = db.get_level(id)
        if level == "easy":
            db.update_status(id, 1)
            task = db.get_erod_easy(n)
            answer = str(db.get_erod_answer_easy(n))
            await call.message.edit_text(f"{task}", reply_markup=kb_back2)
        if level == "medium":
            db.update_status(id, 1)
            task = db.get_erod_medium(n)
            answer = str(db.get_erod_answer_medium(n))
            await call.message.edit_text(f"{task}", reply_markup=kb_back2)
        if level == "hard":
            db.update_status(id, 1)
            task = db.get_erod_hard(n)
            answer = str(db.get_erod_answer_hard(n))
            await call.message.edit_text(f"{task}", reply_markup=kb_back2)
    if call.data == "16task":
        n = random.randint(1, 5)
        db.update_status(id, 1)
        task = db.get_16task(n)
        task = task.split("!")
        w = ""
        for i in range(len(task)):
            w += f"{task[i]}\n"
        answer = str(db.get_16task_answer(n))
        await call.message.edit_text(f"{w}", reply_markup=kb_back3)
    if call.data == "18task":
        n = random.randint(1, 5)
        db.update_status(id, 1)
        task = db.get_18task(n)
        answer = str(db.get_18task_answer(n))
        await call.message.edit_text(f"{task}", reply_markup=kb_back3)
    if call.data == "19task":
        n = random.randint(1, 6)
        db.update_status(id, 1)
        task = db.get_19task(n)
        answer = str(db.get_19task_answer(n))
        await call.message.edit_text(f"{task}", reply_markup=kb_back3)

 #Задания по биологии
    if call.data == "9taskBiology":
        n = random.randint(1, 4)
        db.update_status(id, 1)
        task = db.get_BIO_9task(n)
        task = task.split("!")
        w = ""
        for i in range(len(task)):
            w+=f"{task[i]}\n"
        answer = str(db.get_BIO_9task_answer(n))
        await call.message.edit_text(f"{w}", reply_markup=kb_back4)
    if call.data == "17taskBiology":
        n = random.randint(1, 4)
        db.update_status(id, 1)
        task = db.get_BIO_17task(n)
        task = task.split("!")
        w = ""
        for i in range(len(task)):
            w+=f"{task[i]}\n"
        answer = str(db.get_BIO_17task_answer(n))
        await call.message.edit_text(f"{w}", reply_markup=kb_back4)
    if call.data == "19taskBiology":
        n = random.randint(1, 4)
        db.update_status(id, 1)
        task = db.get_BIO_19task(n)
        task = task.split("!")
        w = ""
        for i in range(len(task)):
            w+=f"{task[i]}\n"
        answer = str(db.get_BIO_9task_answer(n))
        await call.message.edit_text(f"{w}", reply_markup=kb_back4)
    #if call.data == "yes": проверка нажатия на кнопку
    #await call.answer("Оповещение сверху")
    #await call.message.answer("Отправка сообщения")
    #await call.message.edit_text("Редактирование сообщения")
    await bot.answer_callback_query(call.id)#ответ на запрос, чтобы бот не зависал

async def main():
    asyncio.create_task(send_message())  # Запускаем цикл отправки сообщений в отдельном потоке
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
