import json
from check_functions import check_pattern


def load():
    json_contacts = {"Дядя Ваня": {'phones': [8311654654, 89654515], 'birthday': "05.05.1990", 'email': "12@ya.ru"},
                     "Дядя Вася": {'phones': [54654541]}}
    try:
        with open("contacts.json", "r", encoding="utf-8") as fh:
            json_contacts = json.loads(fh.read())
    except:
        print("Загрузка тестового телефонного справочника")

    return json_contacts


def add():
    global phonebook

    pattern = (r"^([А-ЯA-Z]|[А-ЯA-Z][\x27а-яa-z]{1,}|[А-ЯA-Z][\x27а-яa-z]{1,}\-([А-ЯA-Z][\x27а-яa-z]{1,}|" +
               "(оглы)|(кызы)))\040[А-ЯA-Z][\x27а-яa-z]{1,}(\040[А-ЯA-Z][\x27а-яa-z]{1,})?$")
    fullname = check_pattern(1, pattern, "Введите полное имя", False, 1)

    pattern = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    phones = check_pattern(1, pattern, "Введите номер телефона", True, 10)

    pattern = "%m/%d/%y"
    birthday = check_pattern(2, pattern, "Введите дату родения", True, 1)

    pattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    email = check_pattern(1, pattern, "Введите электронную почту", True, 1)

    phonebook[fullname] = {'phones': phones}
    if birthday != "":
        phonebook[fullname]['birthday'] = birthday
    if email != "":
        phonebook[fullname]['email'] = email


def save():
    global phonebook
    with open("contacts.json", "w", encoding="utf-8") as fh:
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