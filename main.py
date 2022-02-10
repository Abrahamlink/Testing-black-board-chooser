import eel
import random

eel.init('front')

children_list = ['Агуреев Анатолий', 'Белов Леонид', 'Бикинин Клим',
                 'Блинов Антон', 'Будько Дмитрий', 'Зайцев Виктор',
                 'Зайцева Полина', 'Закирова Мария', 'Захарова Катя',
                 'Лавыгин Дмитрий', 'Мешавкин Дмитрий', 'Миронова Анастасия',
                 'Попов Сергей', 'Ройш Анастасия', 'Садовников Игорь',
                 'Скрябина Маргарита', 'Сошников Владислав', 'Тараканов Вадим',
                 'Чаткин Матвей', 'Шарипов Радмир', 'Юрьев Виталий']


@eel.expose
def main_children_list_former() -> list:
    random.shuffle(children_list)
    return children_list


eel.start('main.html', size=(700, 700), mode='chrome')
