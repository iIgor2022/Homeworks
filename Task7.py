import os
from pprint import pprint

def open_recepies():
    BASE_PATH = os.getcwd()
    FILE_NAME = 'recepies.txt'

    with open(os.path.join(BASE_PATH, FILE_NAME), 'r', encoding='UTF-8') as file_obj:
        cook_book = {}
        for line in file_obj:
            cook_book[line.strip()] = []
            count_ingredients = int(file_obj.readline().strip())
            for items in range(count_ingredients):
                ingredients = file_obj.readline().split('|')
                cook_book[line.strip()].append(
                    dict(ingridient_name=ingredients[0].strip(), quantity=int(ingredients[1].strip()),
                         measure=ingredients[2].strip()))
            file_obj.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = open_recepies()
    ingridients_list = {}
    for dish in dishes:
        for ingridients in cook_book[dish]:
            if ingridients['ingridient_name'] not in ingridients_list:
                ingridients_list[ingridients['ingridient_name']] = {'quantity': ingridients['quantity'] * person_count,
                                                                    'measure': ingridients['measure']}
            else:
                ingridients_list[ingridients['ingridient_name']]['quantity'] += ingridients['quantity'] * person_count

    pprint(ingridients_list)


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински', 'Фахитос'], 2)
