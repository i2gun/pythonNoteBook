import json
from check_functions import check_pattern


def load() -> dict:
    json_contacts = {"Дядя Ваня": {'phones': [8311654654, 89654515], 'birthday': "05.05.1990", 'email': "12@ya.ru"},
                     "Дядя Вася": {'phones': [54654541]}}
    try:
        with open("contacts.json", "r", encoding="utf-8") as fh:
            json_contacts = json.loads(fh.read())
    except:
        print("Загрузка тестового телефонного справочника")

    return json_contacts


def add(phonebook: dict) -> dict:
    pattern = (r"^([А-ЯA-Z]|[А-ЯA-Z][\x27а-яa-z]{1,}|[А-ЯA-Z][\x27а-яa-z]{1,}\-([А-ЯA-Z][\x27а-яa-z]{1,}|" +
               "(оглы)|(кызы)))\040[А-ЯA-Z][\x27а-яa-z]{1,}(\040[А-ЯA-Z][\x27а-яa-z]{1,})?$")
    fullname = check_pattern(1, pattern, "Введите полное имя", False, 1)
    for key, el in phonebook:
        if key == fullname:
            print("Запись с таким именем уже имеется в справочнике !")
            print("Добавление данных отменено")
            return

    pattern = r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$"
    phones = check_pattern(1, pattern, "Введите номер телефона", True, 10)
    for el in phonebook:
        if len(set(el["phones"] & phones)) > 0:
            print("Один из телофоных номеров уже имеется в справочникес !")
            print("Добавление данных отменено")
            return

    pattern = "%m/%d/%y"
    birthday = check_pattern(2, pattern, "Введите дату родения", True, 1)

    pattern = r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$"
    email = check_pattern(1, pattern, "Введите электронную почту", True, 1)
    for el in phonebook:
        if el["email"] == email:
            print("Такой почтовый ящик уже существует в справочнике !")
            print("Добавление данных отменено")
            return

    record = dict()
    record[fullname] = {'phones': phones}
    if birthday != "":
        record[fullname]['birthday'] = birthday
    if email != "":
        record[fullname]['email'] = email
    
    return phonebook.update(record)


def save(phonebook : dict) -> dict:
    with open("contacts.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phonebook, ensure_ascii=False))
    return phonebook


def show(phonebook : dict) -> dict:
    for key, values in phonebook.items():
        print(key, values)
    return phonebook


def search(phonebook : dict) -> dict:
    for key, values in phonebook.items():
        print(key, values)
    return phonebook


def change(phonebook : dict) -> dict:
    for key, values in phonebook.items():
        print(key, values)
    return phonebook


def delete(phonebook : dict) -> dict:
    for key, values in phonebook.items():
        print(key, values)
    return phonebook