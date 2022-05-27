import eel
import random

eel.init('front')

children_list = ["Students' names", "one-by-one"]


@eel.expose
def main_children_list_former() -> list:
    random.shuffle(children_list)
    return children_list


eel.start('main.html', size=(700, 700), mode='chrome')
