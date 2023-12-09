import json


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

    phones = list()
    fullname = input("Введите полное имя: ")
    numPhones = int(input("Введите количество телефонных номеров: "))
    for i in range(numPhones):
        phones.append(input("Введите номер телефона: "))
    birthday = input("Введите дату родения: ")
    email = input("Введите адрес электронной почты: ")
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
    command = input("Введите команду: ")
    try:
        commands[command]()
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