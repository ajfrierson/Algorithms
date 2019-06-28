#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
		maxSingleServings = None
		for ingredient, quantity in recipe.items():
				if ingredient in ingredients:
					for availableIngredient, availableQuantity in ingredients.items():
							if ingredient == availableIngredient:
									if quantity > availableQuantity:
										return 0
									maxSingle = availableQuantity // quantity
									if maxSingleServings == None:
										temp = maxSingle
										maxSingleServings = temp
									if maxSingle < maxSingleServings:
										temp = maxSingle
										maxSingleServings = temp
										
										pass
				else:
					return 0
		print(f"hello! i'm maxSingle: {maxSingleServings}")
		return maxSingleServings


if __name__ == '__main__':
				# Change the entries of these dictionaries to test
				# your implementation with different inputs
		recipe = { 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }
		ingredients = { 'milk': 1288, 'flour': 9, 'sugar': 95 }
		print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
				batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

