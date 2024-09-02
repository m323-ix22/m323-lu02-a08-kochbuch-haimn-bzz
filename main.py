"""
A08
"""

import json


def load_recipe(json_string):
    return json.loads(json_string)


def adjust_recipe(recp, num_people):
    factor = num_people / recp['servings']
    adjusted_ingredients = {ingredient: int(amount * factor) for ingredient, amount in recp['ingredients'].items()}
    return {
        'title': recp['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')

    recipe = load_recipe(recipe_json)
    print('Original Recipe:', recipe)

    adjusted_recipe = adjust_recipe(recipe, 2)
    print('Adjusted Recipe for 2 people:', adjusted_recipe)

    adjusted_recipe = adjust_recipe(recipe, 8)
    print('Adjusted Recipe for 8 people:', adjusted_recipe)
