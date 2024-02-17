import json
from check_functions import check_pattern


def load() -> dict:
    json_records = {'first record': {'text': "Hello World!", 'date': "17.02.2024"},
                    'some record': {'text': "some note",  'date': "17.02.2024"}, }
    try:
        with open("notes.json", "r", encoding="utf-8") as fh:
            json_records = json.loads(fh.read())
    except:
        print("Загрузка заметок из файла")

    return json_records


def add(notebook: dict) -> dict:
    title = input("Введите заголовок заметки: ")
    for key, el in notebook:
        if key.lowercase == title.lowercase:
            print("Запись с таким заголовком уже имеется в заметках !")
            print("Добавление данных отменено")
            return

    phones = input("Введите текст заметки: ")

    dateOfNote = date.today()

    record = dict()
    record[title] = {'text': phones, 'date': dateOfNote}
    
    return notebook.update(record)


def save(notebook : dict) -> dict:
    with open("notes.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(notebook, ensure_ascii=False))
    return notebook


def show(notebook : dict) -> dict:
    for key, values in notebook.items():
        print(key, values)
    return notebook


def search(notebook : dict) -> dict:
    for key, values in notebook.items():
        print(key, values)
    return notebook


def change(notebook : dict) -> dict:
    for key, values in notebook.items():
        print(key, values)
    return notebook


def delete(notebook : dict) -> dict:
    for key, values in notebook.items():
        print(key, values)
    return notebook