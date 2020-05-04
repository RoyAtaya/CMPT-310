"""
To run this script:
	python shoppingCost.py

In order to pass the autograder your createPricesDict function should
return a dictionary like this:
{'Bananas': 1.56,
 'French fried potatoes': 2.61,
 ...
}
If you run the above script, a correct calculateShoppingCost function should return:

The final cost for our shopping cart is 35.58
"""

import csv

def calculateShoppingCost(productPrices, shoppingCart):
	finalCost = 0
	shoppingCartList = shoppingCart.keys()
	for item in shoppingCartList:
		cost = productPrices.get(item)*shoppingCart.get(item)
		finalCost+=cost
	return finalCost


def createPricesDict(filename):
	productPrice = {}
	input_file = open(filename,'r')
	for line in input_file:
		data = line.split(",")
		key, value = data[0], data[1]
		productPrice[key]= float(value)
	return productPrice


if __name__ == '__main__':
	prices = createPricesDict("Grocery.csv")
	myCart = {"Bacon": 2,
		      "Homogenized milk": 1,
		      "Eggs": 5}
	print("The final cost for our shopping cart is {}".format(calculateShoppingCost(prices, myCart)))
