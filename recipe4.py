import json
from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter

# Version 4 of the recipe analyzer. Compared to V3, this one prints the top three ingredient pairs regardless of their scores.
# I also fixed a bug about printing just 1 recipe's ingredients.

# declarations
recipes = []
ingredients = []
# paired_recipes is a list of recipes with the user-defined item to be used later
paired_recipes = []
# ingredient_scores is the dictionary of counts for each ingredient being paired with the user-defined item
ingredient_scores = defaultdict(int)

i = 0
j = 0
k = 0

all_stopwords = ['/', 'cup', 'of', 'cups', 'sifted', 'melted', 'pint', 'chilled', 'salted', 'unsalted', 'fresh', 'frozen', 'thawed', 'dried', 'kernels', 'roasted', 'marinated', 'package', 'packages', 'unchilled', 'drained', 'and', 'of', ',', 'pieces', 'piece', 'chopped', 'cubed', 'diced', 'sliced', 'gram', 'grams', 'oz', 'ounce', 'ounces', 'teaspoon', 'tablespoon', 'teaspoons', 'tablespoons', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'half', 'third', 'fourth', 'fifth', '0.25', '.25', '1/2', '1/3', '1/4', '1/5', '3/4', '2/3', '2/5', '3/5', '1/8', 'warm', 'shredded', 'optional', '(optional)', 'active', 'dry', 'instant']

def listToString(s):
	str1 = " "
	return str1.join(s)

for line in open('allrecipes-recipes.json', 'r'):
	recipes.append(json.loads(line))
	ingredients.append(recipes[i].get('ingredients'))
	i += 1

paired_recipes = []


# This limit was used during testing, and can be used by those with weaker machines
#ingredients = ingredients[0:100]
print("Looking through " + str(range(len(ingredients))) + "recipe sets of ingredients...")


search_ingredient = input("I'm looking for foods that go with:\n")

# gets user-input ingredient to look for partners of
print("Looking for ingredients to pair with " + search_ingredient + "...")

x_ingredient = search_ingredient 

# searches the ingredients data to store recipes with that ingredient
for recipe in ingredients:
	for food_item in recipe:
		if food_item.find(x_ingredient) != -1:
			paired_recipes.append(recipe)
			break

print("Found " + str(len(paired_recipes)) + " recipes with that ingredient.")
# prints as many recipes as the user wants recipes; this can be changed
x = input("How many recipes' ingredients do you want to see?\n")
y = int(x)
while y > 0:
	if y == 1:
		print(paired_recipes[0])
	else:
		print(paired_recipes[y])
	y -= 1


# this cleans up the ingredient, so for example 1/2 cup butter becomes butter
for ingredient_list in paired_recipes:
	for other_ingredient in ingredient_list:
		split_words = other_ingredient.split()
		cleaned_words = [word for word in split_words if word.lower() not in all_stopwords]
		ingredient_scores[listToString(cleaned_words)] += 1	

# this allows the sorting by descending order of the count score
d = OrderedDict(sorted(ingredient_scores.items(), key=itemgetter(1), reverse=True))

# this prints the top three ingredient pairs and their scores; this is changeable.
for pair_d in d:
	if k < 3:
		print((pair_d) + ": " + str(ingredient_scores[pair_d]))
		k += 1
	else:
		exit(0)




