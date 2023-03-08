from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    dishes = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({'name': name,
                                'quantity': quantity,
                                'measure': measure})
        file.readline()
        dishes[dish_name] = ingredients

pprint(dishes)


def get_shop_list_by_dishes(dishess, person_count):
    ingredients_need = {}
    for dish, ingredientss in dishes.items():
        if dish in dishess:
            for i in ingredientss:
                ingredients_quantity = int(i['quantity'])
                namee = i['name']
                measuree = i['measure']
                if namee not in ingredients_need.keys():
                    ingredients_need[namee] = {'measure': measuree,
                                               'quantity': ingredients_quantity * person_count}
                else:
                    ingredients_need[namee]['quantity'] += ingredients_quantity * person_count
    return ingredients_need


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))
