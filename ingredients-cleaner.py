import json
import os

# Recipe Database Ingredients Cleaner

# Declarations
recipes = []
ingredients = []
cleaned_words = {"cleaned_ingredients": []}
i = 0

# The list of words to remove from the ingredients list to get the main ingredient word
all_stopwords = [',', '/', 'cup', 'of', 'cups', 'freshly', 'ground', 'sifted', 'melted', 'pint', 'chilled', 'salted', 'unsalted', 'fresh', 'frozen', 'thawed', 'dried', 'kernels', 'roasted', 'marinated', 'package', 'packages', 'unchilled', 'drained', 'and', 'of', ',', 'pieces', 'piece', 'chopped', 'cubed', 'diced', 'sliced', 'gram', 'grams', 'oz', 'ounce', 'ounces', 'teaspoon', 'tablespoon', 'teaspoons', 'tablespoons', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'half', 'third', 'fourth', 'fifth', '0.25', '.25', '1/2', '1/3', '1/4', '1/5', '3/4', '2/3', '2/5', '3/5', '1/8', 'warm', 'shredded', 'optional', '(optional)', 'active', 'dry', 'instant']

# Open the json files for reading and writing
fin = open('allrecipes-recipes.json', 'r+')
fout = open('allcleanrecipes.json', 'w')

# Goes through the lines in the json file
for line in fin:
	# Loads each line or recipe as data
	data = json.loads(line)
	# Resets the cleaned words dictionary for each line or recipe
	cleaned_words = {"cleaned_ingredients": []}
	# For each food item in a recipe's ingredients
	for food_item in data["ingredients"]:

		# Cleans the ingredients words (remove the words in all_stopwords)
		split_words = food_item.split()
		cleaned_words["cleaned_ingredients"].append([word for word in split_words if word.lower() not in all_stopwords])

		# Adds the cleaned words to the json data to each line		
		data.update(cleaned_words)

	# Writes the data to a new line as an update		
	json.dump(data, fout)
	fout.write("\n")
	# Prints which line was just completed
	i += 1
	print("Line " + str(i))

# Closes the files
fin.close()
fout.close()


