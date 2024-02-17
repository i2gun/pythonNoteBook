from json import loads, dumps
from datetime import date


def serialize_datetime(obj): 
    if isinstance(obj, date): 
        return obj.isoformat() 
    

def load() -> dict:
    json_records = {  1: {'title': "first record", 'text': "Hello World!", 'date': date.today()},
                      2: {'title': "some record",  'text': "some note",    'date': date.today()}, }
    try:
        with open("notes.json", "r", encoding="utf-8") as fh:
            # fh.write(dumps(notebook, ensure_ascii=False, default=serialize_datetime, ))
            json_records = loads(fh.read().replace("; ", ", "))
            print(json_records)
    except:
        print("Загрузка заметок из файла не удалась")
    
    return json_records


def add(notebook: dict) -> dict:
    if not notebook:
        notebook = dict()
        id = 0
    else:
        id = notebook.list() + 1

    title = input("Введите заголовок заметки: ")
    for key, value in notebook:
        if value['title'].lower() == title.lower():
            print("Запись с таким заголовком уже имеется в заметках !")
            print("Добавление данных отменено")
            return

    textOfNote = input("Введите текст заметки: ")
    notebook[id] = {'title': title, 'text': textOfNote, 'date': date.today()}
    
    return notebook


def save(notebook):
    with open("notes.json", "w", encoding="utf-8") as fh:
        fh.write(dumps(notebook, ensure_ascii=False, default=serialize_datetime, separators=("; ", ": ")))
    return notebook


def show(notebook):
    if not notebook:
        print("Записаня книга пуста")
        return
    
    for key, values in notebook.items():
        print(key, values)
        
    return notebook


def search(notebook):
    if not notebook:
        print("Записаня книга пуста")
        return

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
    if not notebook:
        print("Записаня книга пуста")
        return

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
    if not notebook:
        print("Записаня книга пуста")
        return

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