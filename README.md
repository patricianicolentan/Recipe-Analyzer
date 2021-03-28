# Recipe-Analyzer
The recipe5.py program analyzes a recipe database to find ingredients often used with a user-defined ingredient, to try to simulate what an experienced chef would intuitively 'know'. For example, does olive oil go with basil? Yes, 1,154 times in 91,000+ recipes! But not as much as garlic, which was paired with olive oil 2,239 times!

Customizable options include how many recipes' ingredient lists to print out, and how many times an ingredient must be a partner to be printed out.

The current database being used is the allrecipes database, accessed through https://archive.org/details/recipes-en-201706 with credit for that going to Zachary Vance.

IMPORTANT: The file allrecipes-recipes.json must be downloaded before this program can run, or the code must be adapted to use another recipe database.

NOTE: recipe-5.py is the latest version of the code.

# Ingredients-Cleaner

The ingredients-cleaner.py program goes through the entire JSON database (allrecipes-recipes.json) and cleans the ingredients list, similar to the recipe-analyzer program, but instead of doing so for ingredients that go with a user-input ingredient, this program cleans the whole database. The cleaned ingredients list is added as a new key or item to each JSON line.
