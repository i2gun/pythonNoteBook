from json import loads, dumps
from datetime import datetime as date


# ------- load -------------------------------------------------------------
def load() -> dict:
    json_records = {  0: {'title': "first record", 'text': "Hello World!", 'date': serialize_datetime(date.now())},
                      1: {'title': "some record",  'text': "some note",    'date': serialize_datetime(date.now())}, }
    try:
        with open("notes.json", "r", encoding="utf-8") as fh:
            json_records = loads(fh.read().replace("; ", ", "))
    except:
        print("Загрузка заметок из файла не удалась")

    return json_records

# ------- save -------------------------------------------------------------
def save(notebook):
    if emptyCheck(notebook):
        return

    with open("notes.json", "w", encoding="utf-8") as fh:
        fh.write(dumps(notebook, ensure_ascii=False, separators=("; ", ": ")))
    print("Заметки успешно сохранены")
    return notebook

# ------- add --------------------------------------------------------------
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
    notebook[id] = {'title': title, 'text': textOfNote, 'date': serialize_datetime(date.now())}
    print(id, ": ", notebook[id])

    return notebook

# ------- show -------------------------------------------------------------
def show(notebook):
    if emptyCheck(notebook):
        return
    
    for key, values in notebook.items():
        print(key, values)
        
    return notebook

# ------- search -----------------------------------------------------------
def search(notebook: dict) -> dict:
    res_list = findRecords(notebook)

    if res_list:
        print("    | Результаты поиска:")
        for el in res_list:
            print(el, ": ", notebook[el])
    else:
        print("    | По заданным критериям ничего не найдено")

    return notebook

# ------- change -----------------------------------------------------------
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
        notebook[k] = {'title': notebook[k]['title'], 'text': textOfNote, 'date': date.today()}
        print(k, ": ", notebook[k])

    return notebook
    
# ------- delete -----------------------------------------------------------
def delete(notebook: dict) -> dict:
    res_list = findRecords(notebook)

    if not res_list:
        print("    | Запись для удаления не найдена")
        return notebook

    for k in res_list:
        print("Запись к удалению: ")
        print(k, ": ", notebook[k])
        print()
        yes_no = input("Удалить запись? [введите только 'y' для удаления]").strip()

        if yes_no == 'y':
            print(">>>  Запись удалена: ")
            print(">>>  " + k + ": " + notebook.pop(k))
            print()

    return notebook

# ================== SERVICE FUNCTIONS ====================================

# ------- serialize_datetime ----------------------------------------------
def serialize_datetime(obj: date) -> str: 
    if isinstance(obj, date): 
        return obj.isoformat(timespec="minutes")

# ------- emptyCheck ------------------------------------------------------
def emptyCheck(notebook: dict) -> bool:
    if not notebook:
        print("Записная книга пуста")
        return True
    return False

# ------- findRecords -----------------------------------------------------
def findRecords(notebook: dict) -> list:
    if emptyCheck(notebook):
        return

    res_list = list()

    print("    |-----------------------")
    search_text = input("    | Введите заголовок заметки: ").strip()
    print("    |-----------------------")
    for key, value in notebook.items():
        if search_text in value['title']:
            res_list.append(key)
    
    return res_list