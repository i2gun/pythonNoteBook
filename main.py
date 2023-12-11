import command_fucntions

loopGoOn = True
phonebook = command_fucntions.load()
commands = {"add": command_fucntions.add, "save": command_fucntions.save, "show": command_fucntions.show,
            "search": command_fucntions.search, "change": command_fucntions.change,
            "quit": command_fucntions.finish, "exit": command_fucntions.finish}

while loopGoOn:
    print("-----------------------")
    print("Вам доступны следующие команды: ", *commands)
    command = input("Введите новую команду: ")
    print("-----------------------")
    try:
        commands[command]()
    except:
        print("Неверная комманда")

# Урок 8. Работа с файлами

# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник
# с внешним хранилищем информации, и чтоб был реализован основной функционал -
# просмотр, сохранение, импорт, поиск, удаление, изменение данных.
#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных
#
# Формат сдачи: ссылка на свой репозиторий в гитхаб.
