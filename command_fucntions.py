from json import loads, dumps
from datetime import date


def serialize_datetime(obj): 
    if isinstance(obj, date): 
        return obj.isoformat() 


def load() -> dict:
    # json_records = {  0: {'title': "first record", 'text': "Hello World!", 'date': date.today()},
    #                   1: {'title': "some record",  'text': "some note",    'date': date.today()}, }
    try:
        with open("notes.json", "r", encoding="utf-8") as fh:
            json_records = loads(fh.read().replace("; ", ", "))
    except:
        print("Загрузка заметок из файла не удалась")
    
    return json_records


def add(notebook: dict) -> dict:
    if not notebook:
        notebook = dict()
        id = 0
    else:
        id = len(notebook)

    title = input("Введите заголовок заметки: ")
    for key, value in notebook.items():
        if value['title'].lower() == title.lower():
            print("Запись с таким заголовком уже имеется в заметках !")
            print("Добавление данных отменено")
            return notebook

    textOfNote = input("Введите текст заметки: ")
    notebook[id] = {'title': title, 'text': textOfNote, 'date': date.today()}
    
    return notebook


def save(notebook):
    if emptyCheck(notebook):
        return

    with open("notes.json", "w", encoding="utf-8") as fh:
        fh.write(dumps(notebook, ensure_ascii=False, default=serialize_datetime, separators=("; ", ": ")))
    print("Заметки успешно сохранены")
    return notebook


def show(notebook):
    if emptyCheck(notebook):
        return
    
    for key, values in notebook.items():
        print(key, values)
        
    return notebook


def search(notebook: dict) -> dict:
    res_list = findRecords(notebook)

    if res_list:
        print("    | Результаты поиска:")
        for el in res_list:
            print(el)
    else:
        print("    | По заданным критериям ничего не найдено")

    return notebook


def change(notebook):
    res_list = findRecords(notebook)

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
    

def delete(notebook: dict) -> dict:
    res_list = findRecords(notebook)

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


def emptyCheck(notebook: dict) -> bool:
    if not notebook:
        print("Записная книга пуста")
        return True
    return False


def findRecords(notebook: dict) -> dict:
    if emptyCheck(notebook):
        return

    res_list = list()

    print("    |-----------------------")
    search_text = input("    | Введите заголовок заметки для внесения изменений: ").strip()
    print("    |-----------------------")
    for key, value in notebook.items():
        if search_text in value['title']:
            res_list.append(key + ": " + str(value))
    
    return res_list