# Tasks 1 and 2
import os
cook_book = {}

def get_cook_book(file_name):
    with open(f'{file_name}', encoding="utf-8") as f:
        for line in f:
            meal = line.strip()
            number_position = int(f.readline().strip())
            cook_book[meal] = []
            lines = f.readline().strip()
            while lines:
                ingredients = lines.split("|")
                composition_dict = {"ingredient_name": ingredients[0], "quantity": int(ingredients[1]), "measure": ingredients[2]}
                cook_book[meal].append(composition_dict)
                lines = f.readline().strip()
    return cook_book

print(get_cook_book('recipes.txt'))

def get_shop_list_by_dishes(meals, person_count):
    for key in meals:
        if key in cook_book.keys():
            print(key)
            for value in cook_book[key]:
                value['quantity'] *= person_count
                print(value)

            print()
        else:
            print(f'Рецепта для {key} нет в cook_book!')
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 4))