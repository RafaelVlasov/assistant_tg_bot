# assistant_tg_bot
Телеграм-бот написан для:
- сохранения профессионально-новых для меня слов, чтобы не забыть изучить их значения, если в тот момент на это нет времени;
- записи новых слов в словарь (слово и его определение), чтобы в будущем была возможность вернуться к этой информации;
- записи задач (наподобие todo-листа);
- сохранение ссылок на полезные ресурсы которые подсказывают коллеги.

Функциональности:
- /help - вывести справку по функциональностям
- /view_words - показать список сохранённых слов
- /view_dict - показать собранный it-словарь
- /to_do_list - показать список дел
- /view_links - показать сохранённые ссылки
- add_word "слово" - добавить слово во временный массив чтобы изучить его значение в будущем
- add_dict "слово - значение" - добавить слово и его определение в словарь
- add_todo "описание задачи" - добавить задачу в список дел
- add_link "ссылка" - сохранить ссылку
- del_word "слово" - удалить слово из временного массива
- del_dict "слово" - удалить слово и его описание из словаря
- del_todo "номер задачи" - удалить задачу из списка дел
- del_link "номер ссылки" - удалить ссылку под указанным номером

Дополнительно:
Все данные записываются непосредственно в .txt файлы чтобы обеспечить сохранение информации в случае непредвиденной остановки програмного кода
