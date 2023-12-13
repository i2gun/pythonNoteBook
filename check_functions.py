import re
import datetime


def check_date(pattern: re, text: str) -> bool:
    try:
        datetime.datetime.strptime(text, pattern)
    except Exception:
        return False
    return True


def check_func(check_type: int, pattern: re, text: str) -> bool:
    if check_type == 1:
        return re.fullmatch(re.compile(pattern), text)
    elif check_type == 2:
        return check_date(pattern, text)


def check_pattern(check_type: int, pattern: re, msg: str, check_for_quit: bool, item_num: int) -> tuple[set, str]:
    keep_looping = True
    out = set() if item_num > 1 else ""
    while keep_looping and item_num > 0:
        text = input(msg + (", либо 'q' для выхода: " if check_for_quit else ": "))
        if check_func(check_type, pattern, text):
            if type(out) is set:
                if text in set:
                    print("Такая запись уже вводилась !")
                    continue
                out.append(text)
            else:
                out = text
            item_num -= 1
        else:
            if check_for_quit and text == "q":
                keep_looping = False
            else:
                print("Введено неверное значение")
    return out