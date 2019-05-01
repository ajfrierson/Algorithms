#!/usr/bin/python

import argparse

def find_max_profit(prices):
	maxProfit = None
	for b in range(0, len(prices)):
		for s in range(prices.index(prices[b]) + 1, len(prices)):
			profit = prices[s] - prices[b]
			print(profit)
			if maxProfit == None:
				maxProfit = profit
			elif profit > maxProfit:
				temp = profit
				maxProfit = temp
		
		
	return maxProfit
	pass



if __name__ == '__main__':
	# This is just some code to accept inputs from the command line
	parser = argparse.ArgumentParser(description='Find max profit from prices.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
	args = parser.parse_args()

	print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))