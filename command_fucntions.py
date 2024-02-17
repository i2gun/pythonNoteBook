import json
from datetime import date


def load() -> dict:
    json_records = {  1: {'title': "first record", 'text': "Hello World!", 'date': date.today()},
                      2: {'title': "some record",  'text': "some note",    'date': date.today()}, }
    try:
        with open("notes.json", "r", encoding="utf-8") as fh:
            json_records = json.loads(fh.read())
    except:
        print("Загрузка заметок из файла")

    return json_records


def add(notebook: dict) -> dict:
    title = input("Введите заголовок заметки: ")
    for key, value in notebook:
        if key.lower() == title.lower():
            print("Запись с таким заголовком уже имеется в заметках !")
            print("Добавление данных отменено")
            return

    textOfNote = input("Введите текст заметки: ")

    record = dict()
    record[title] = {'text': textOfNote, 'date': date.today()}
    
    return notebook.update(record)


def save(notebook):
    with open("contacts.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(notebook, ensure_ascii=False))
    return notebook


def show(notebook):
    for key, values in notebook.items():
        print(key, values)
    return notebook


def search(notebook):
    res_list = list()

    search_text = input("    | Введите заголовок заметки либо его часть: ").strip()
    for key, value in notebook.items():
        if search_text in key:
            res_list.append(key + ": " + str(value))

    if res_list:
        print("    | Результаты поиска:")
        for el in res_list:
            print(el)
    else:
        print("    | По заданным критериям ничего не найдено")

    return notebook


def change(notebook):
    res_list = list()
    print("    |-----------------------")
    search_text = input("    | Введите заголовок заметки для внесения изменений: ").strip()
    print("    |-----------------------")
    for key in notebook.items():
        if search_text in key:
            res_list.append(key)

    if not res_list:
        print("    | Запись к внесению изменений не найдена")
        return notebook
    
    for k in res_list:
        print("Вносятся изменения в следующую запись:")
        print(notebook[k])
        print()
        textOfNote = input("Введите текст заметки: ")
        notebook[k] = {'text': textOfNote, 'date': date.today()}

    return notebook
    

def delete(notebook):
    res_list = list()
    print("    |-----------------------")
    search_text = input("    | Введите заголовок заметки для внесения изменений: ").strip()
    print("    |-----------------------")
    for key in notebook.items():
        if search_text in key:
            res_list.append(key)

    if not res_list:
        print("    | Запись к внесению изменений не найдена")
        return notebook
    
    for k in res_list:
        print("Запись к удалению: ")
        print(notebook[k])
        print()
        yes_no = input("Удалить запись? [введите только 'y' для удаления]").strip()

        if yes_no:
            print(">>>  Запись удалена: ")
            print(">>>  " + k + ": " + notebook.pop(k))
            print()

    return notebook