import json
import re
import datetime


def check_date(pat, txt):
    try:
        datetime.datetime.strptime(txt, pat)
    except:
        return False
    return True

def check_func(type, pat, txt):
    if type == 1:
        print("11")
        return re.fullmatch(re.compile(pat), txt)
    elif type == 2:
        return check_date(pat, txt)


def check_pattern(check_type, pat, msg, check_for_quit, item_num):
    keep_looping = True
    out = list() if item_num > 1 else ""
    print(type(out))
    show_msg = msg + (", либо 'q' для выхода: " if check_for_quit else ": ")
    while keep_looping and item_num > 0:
        text = input(show_msg)
        if check_func(check_type, pat, text):
            if type(out) is list:
                print("22")
                out.append(text)
            else:
                print("33")
                out = text
            item_num -= 1
        else:
            if check_for_quit and text == "q":
                keep_looping = False
            else:
                print("Введено неверное значение")
    return out


def load() -> set:
    temp_contacts = {"Дядя Ваня": {'phones': [8311654654, 89654515],
                                   'birthday': "05.05.1990",
                                   'email': "12@ya.ru"
                                   },
                     "Дядя Вася": {'phones': [54654541]}
                     }
    try:
        with open("contants.json", "r", encoding="utf-8") as fh:
            temp_contacts = json.loads(fh.read())
    except:
        print("Загрузка тестового телефонного справочника")
    return temp_contacts


def add():
    global phonebook

    pattern = r"[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?"
    message = "Введите полное имя"
    fullname = check_pattern(1, pattern, message, False, 1)

    pattern = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    message = "Введите правильный номер телефона"
    phones = check_pattern(1, pattern, message, True, 10)

    pattern = "%m/%d/%y"
    message = "Введите дату родения"
    birthday = check_pattern(2, pattern, message, True, 1)

    # pattern = r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"	
    # pattern = r"^\w+[\w-\.]*\@\w+((-\w+)|(\w*))\.[a-z]{2,3}$"
    pattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    
    message = "Введите адрес электронной почты"
    email = check_pattern(1, pattern, message, True, 1)

    print("3")
    
    phonebook[fullname] = {'phones': phones }
    if birthday != "":
        phonebook[fullname]['birthday'] = birthday
    if email != "":
        phonebook[fullname]['email'] = email


def save():
    global phonebook
    with open("contants.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))

def show():
    global phonebook
    for key, values in phonebook.items():
        print(key, values)


def search():
    global phonebook
    for key, values in phonebook.items():
        print(key, values)


def change():
    global phonebook
    for key, values in phonebook.items():
        print(key, values)

def finish():
    global loopGoOn
    loopGoOn = False


loopGoOn = True
phonebook = load()
commands = {"add": add, "save": save, "show": show, "search": search, "change": change, "quit": finish, "exit": finish}

print("Вам доступны следующие команды: ", *commands)

while loopGoOn:
    print("-----------------------")
    show()
    print("-----------------------")
    command = input("Введите новую команду: ")
    try:
        commands[command]()
        show()
    except:
        print("Неверная комманда")



# Урок 8. Работа с файлами

# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации,
# и чтоб был реализован основной функционал - просмотр, сохранение, импорт, поиск, удаление, изменение данных.
#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести
# имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
#
# для отлично в группах надо выполнить или ТГ бот или ГУИ (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД
#
# ГУИ можно сделать просто на EasyGUI или Tkinter
#
# Формат сдачи: ссылка на свой репозиторий в гитхаб.