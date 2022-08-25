import telebot  # импортируем библиотеку для создания ТГ-ботов
from telebot import types  # импортируем модуль для создания кнопок чата

bot = telebot.TeleBot('')  # присваиваем токен бота из ТГ


@bot.message_handler(commands=['help'])  # обработчик для считывания команд пользователя
def helper(message):
    help_message = '<b>/help</b> - вывести справку по функциональностям\n<b>/view_words</b> - показать список ' \
                   'сохранённых слов\n<b>/view_dict</b> - показать собранный it-словарь\n<b>/to_do_list</b> - ' \
                   'показать список дел\n<b>/view_links</b> - показать сохранённые ссылки\n<b>add_word \"слово\"' \
                   '</b> - добавить слово во временный массив чтобы изучить его значение в будущем\n<b>add_dict \"' \
                   'слово - значение\"</b> - добавить слово и его определение в словарь\n<b>add_todo \"описание ' \
                   'задачи\"</b> - добавить задачу в список дел\n<b>add_link</b> - сохранить ссылку\n<b>del_word' \
                   ' \"слово\"</b> - удалить слово из временного массива\n<b>del_dict \"слово\"</b> - удалить слово' \
                   ' и его описание из словаря\n<b>del_todo \"номер задачи\"</b> - удалить задачу под указанным ' \
                   'номером из списка дел\n<b>del_link \"номер ссылки\"</b> - удалить ссылку под указанным номером'
    bot.send_message(message.chat.id, help_message, parse_mode='html')


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f'Привет <b>{message.from_user.first_name}</b>! Видимо ты услышал что-то новое от своих коллег с ' \
                f'работы и хочешь записать это, чтобы потом внимательнее изучить или сохранить?'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    # параметры: 1 - размер кнопок одинаковый на компе и телефоне, 2 - количество кнопок в строке - 3 шт
    help_button = types.KeyboardButton('/help')
    start_button = types.KeyboardButton('/start')
    view_words_button = types.KeyboardButton('/view_words')
    view_dict_button = types.KeyboardButton('/view_dict')
    to_do_list_button = types.KeyboardButton('/to_do_list')
    view_links_button = types.KeyboardButton('/view_links')
    markup.add(help_button, start_button, view_words_button, view_dict_button, to_do_list_button, view_links_button)
    # через message.chat.id обращаемся к нашему с ботом чату, отправляем сообщение, формат отправки parse_mode
    # используем html чтобы иметь возможность управлять видом текста с помощью тагов
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


#  просмотр сохранённых слов
@bot.message_handler(commands=['view_words'])
def view_words(message):
    send_mess = f'<b>{message.from_user.first_name}</b>, вот список новых, для тебя, слов к изучению:'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
    with open("temp_word.txt", 'r', encoding='utf-8') as file:
        words_list = [line.strip() for line in file.readlines()]
        bot.send_message(message.chat.id, ', '.join(words_list), parse_mode='html')


#  просмотр it-словаря
@bot.message_handler(commands=['view_dict'])
def view_dict(message):
    send_mess = f'<b>{message.from_user.first_name}</b>, вот собранный тобою it-словарик:'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
    with open("it_dict.txt", 'r', encoding='utf-8') as file:
        list_values = [line.strip() for line in file.readlines()]
        bot.send_message(message.chat.id, '\n'.join(list_values), parse_mode='html')


#  просмотр to do листа
@bot.message_handler(commands=['to_do_list'])
def to_do_list(message):
    send_mess = f'<b>{message.from_user.first_name}</b>, вот твой список дел:'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
    with open("todo_list.txt", 'r', encoding='utf-8') as file:
        todo_list = [line.strip() for line in file.readlines()]
        bot.send_message(message.chat.id, '\n'.join(todo_list), parse_mode='html')


#  просмотр списка ссылок
@bot.message_handler(commands=['view_links'])
def view_links(message):
    send_mess = f'<b>{message.from_user.first_name}</b>, вот список сохранённых ссылок:'
    bot.send_message(message.chat.id, send_mess, parse_mode='html')
    with open("links.txt", 'r', encoding='utf-8') as file:
        links = [line.strip() for line in file.readlines()]
        bot.send_message(message.chat.id, '\n'.join(links), parse_mode='html')


#  добавление и удаление данных
@bot.message_handler()
def add_and_del_data(message):
    if 'add_word' in message.text:
        send_mess = f'Отлично <b>{message.from_user.first_name}</b>! Я сохранил слово во временный массив, чтобы ' \
                    f'потом изучить его значение и занести в словарь '
        bot.send_message(message.chat.id, send_mess, parse_mode='html')
        with open("temp_word.txt", 'a', encoding='utf-8') as file:
            file.write(message.text[9:] + '\n')
    elif 'add_dict' in message.text:
        send_mess = f'Отлично <b>{message.from_user.first_name}</b>! Я сохранил слово и его определение в словарь'
        bot.send_message(message.chat.id, send_mess, parse_mode='html')
        with open("it_dict.txt", 'a', encoding='utf-8') as file:
            file.write(message.text[9:] + '\n')
    elif 'add_link' in message.text:
        send_mess = f'Отлично <b>{message.from_user.first_name}</b>! Я сохранил новую ссылку в список'
        bot.send_message(message.chat.id, send_mess, parse_mode='html')
        with open("links.txt", 'r', encoding='utf-8') as file:
            links = [line.strip() for line in file.readlines()]
        with open("links.txt", 'a', encoding='utf-8') as file:
            file.write(str(len(links) + 1) + ") " + message.text[9:] + '\n')
    elif 'add_todo' in message.text:
        send_mess = f'Отлично <b>{message.from_user.first_name}</b>! Я сохранил новую задачу в список дел'
        bot.send_message(message.chat.id, send_mess, parse_mode='html')
        with open("todo_list.txt", 'r', encoding='utf-8') as file:
            todo_list = [line.strip() for line in file.readlines()]
        with open("todo_list.txt", 'a', encoding='utf-8') as file:
            file.write(str(len(todo_list) + 1) + ") " + message.text[9:] + '\n')
    elif 'del_word' in message.text:
        with open("temp_word.txt", 'r', encoding='utf-8') as file:
            temp_list_words = [line.strip() for line in file.readlines()]
        if message.text[9:] in temp_list_words:
            for i in range(len(temp_list_words)):
                if temp_list_words[i] == message.text[9:]:
                    del temp_list_words[i]
                    send_mess = f'<b>{message.from_user.first_name}</b>, я удалил слово <b>{message.text[9:]}</b>' \
                                f' из списка '
                    bot.send_message(message.chat.id, send_mess, parse_mode='html')
                    with open("temp_word.txt", 'w', encoding='utf-8') as file:
                        for word in temp_list_words:
                            file.write(word + '\n')
                    break
        else:
            send_mess = f'<b>{message.from_user.first_name}</b>, я не нашёл слово <b>{message.text[9:]}</b> в списке'
            bot.send_message(message.chat.id, send_mess, parse_mode='html')
    elif 'del_dict' in message.text:
        with open("it_dict.txt", 'r', encoding='utf-8') as file:
            temp_list_dict = [line.strip() for line in file.readlines()]
        count = 0
        for i in range(len(temp_list_dict)):
            if message.text[9:] + ' -' in temp_list_dict[i]:
                del temp_list_dict[i]
                with open("it_dict.txt", 'w', encoding='utf-8') as file:
                    for word in temp_list_dict:
                        file.write(word + '\n')
                count += 1
                break
        if count > 0:
            send_mess = f'<b>{message.from_user.first_name}</b>, я удалил слово <b>{message.text[9:]}</b>' \
                        f' и его определение из словаря!'
            bot.send_message(message.chat.id, send_mess, parse_mode='html')
        else:
            send_mess = f'<b>{message.from_user.first_name}</b>, я не нашёл слово <b>{message.text[9:]}</b> в ' \
                        f'твоём словаре!'
            bot.send_message(message.chat.id, send_mess, parse_mode='html')
    elif 'del_todo' in message.text:
        with open("todo_list.txt", 'r', encoding='utf-8') as file:
            temp_todo_list = [line.strip() for line in file.readlines()]
        count = 0
        task = ''
        for i in range(len(temp_todo_list)):
            if message.text[9:] + ')' in temp_todo_list[i]:
                task = temp_todo_list[i]
                del temp_todo_list[i]
                count += 1
                with open("todo_list.txt", 'w', encoding='utf-8') as file:
                    todo_num = 1
                    for word in temp_todo_list:
                        file.write(str(todo_num) + word[1:] + '\n')
                        todo_num += 1
                break
        if count > 0:
            send_mess = f'<b>{message.from_user.first_name}</b>, я удалил задачу <b>{task[3:]}</b> из списка дел!'
            bot.send_message(message.chat.id, send_mess, parse_mode='html')
        else:
            send_mess = f'<b>{message.from_user.first_name}</b>, я не нашёл задачу под этим номером в твоём списке дел'
            bot.send_message(message.chat.id, send_mess, parse_mode='html')
    elif 'del_link' in message.text:
        with open("links.txt", 'r', encoding='utf-8') as file:
            temp_links_list = [line.strip() for line in file.readlines()]
        count = 0
        link = ''
        for i in range(len(temp_links_list)):
            if message.text[9:] + ')' in temp_links_list[i]:
                link = temp_links_list[i]
                del temp_links_list[i]
                count += 1
                with open("links.txt", 'w', encoding='utf-8') as file:
                    link_num = 1
                    for word in temp_links_list:
                        file.write(str(link_num) + word[1:] + '\n')
                        link_num += 1
                break
        if count > 0:
            send_mess = f'<b>{message.from_user.first_name}</b>, я удалил ссылку <b>{link[3:]}</b> из списка!'
            bot.send_message(message.chat.id, send_mess, parse_mode='html')
        else:
            send_mess = f'<b>{message.from_user.first_name}</b>, я не нашёл ссылку под этим номером в списке!'
            bot.send_message(message.chat.id, send_mess, parse_mode='html')
    else:
        send_mess = f'<b>{message.from_user.first_name}</b>, я не понимаю эту команду'
        bot.send_message(message.chat.id, send_mess, parse_mode='html')


#  устанавливаем запуск проекта на постоянную работу
bot.polling(none_stop=True)
