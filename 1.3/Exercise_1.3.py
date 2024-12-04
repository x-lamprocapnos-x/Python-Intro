# Initialize lists
recipes_list = []
ingredients_list = []

# Define the take_recipes function
def take_recipes():
    name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (minutes): "))
    ingredients = input("Enter the ingredients, serperated by commas: ").split(", ")
    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }
    return recipe

# Main program login
n = int(input("How many recipes would you like to add?"))

for i in range(n):
    recipe = take_recipes()
    # Update ingredients list
    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)

    # Add the recipe to recipes_list
    recipes_list.append(recipe)
    

# Detemine difficulty levels
for recipe in recipes_list:
    cooking_time = recipe["cooking_time"]
    num_ingredients = len(recipe["ingredients"])
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients > 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients > 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    recipe["difficulty"] = difficulty

# Print the results
print("Recipes List: ")
for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking time (minutes): ", recipe["cooking_time"])
    print("Ingredients: ", ", ".join(recipe["ingredients"]))
    print("Difficulty: ", recipe["difficulty"])

# Sort ingredients alphabetically
ingredients_list.sort()

# Print all ingredients
print("Ingredients List: ")
for ingredient in ingredients_list:
    print(ingredient)
