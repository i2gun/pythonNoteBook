def select_all():
    cur.execute("SELECT * FROM users;")
    return cur.fetchall()


def add_values():
    cur.execute("INSERT INTO users VALUES (1,'Ваня','Петров');")
    cur.execute("INSERT INTO users VALUES (2,'Сергей','Сергеев');")


def select_ivan():
    cur.execute("SELECT * FROM users WHERE name = 'Ваня';")
    return cur.fetchall()


choice = choicebox("Выберите запрос", "Главная форма",
                   ['Все записи', "Только Ваня"])