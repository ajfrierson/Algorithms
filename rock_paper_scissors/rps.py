#!/usr/bin/python

import sys


def rock_paper_scissors(n):
		rps = ["rock", "paper", "scissors"]
		allPlays = [[]]
		plays = allPlays * 3**((n))
		print(f"I'm the plays: {plays}")
		if n <= 0:
				return plays
		for roundNumber in range(n, n+1):
				print(f" i'm the round: {roundNumber}")
				print(f" i'm allPlays: {allPlays}")
				if n == 1:
						plays = [['rock'], ['paper'], ['scissors']]
						pass
				else:
						print(f"plays is this long: {len(plays)}")
						for x in range(0, len(plays), 3):
							print(f" x is {x}")
							print(f" all plays at {x} is: {plays[x]}")
							plays[x] = [rps[0], rps[x // 3]]
							print(f"test plays {plays}")
						for y in range(1, len(plays), 3):
							print(f" round {y}")
							print(f" all plays at {y} is: {plays[y]}")
							plays[y] = [rps[1], rps[y // 3]]
							print(f"test plays {plays}")
						for z in range(2, len(plays), 3):
							print(f" round {z}")
							print(f" all plays at {z} is: {plays[z]}")
							plays[z] = [rps[2], rps[z // 3]]
							print(f"test plays {plays}")

		print(f" i'm Final allPlays: {plays}")
		return plays


if __name__ == "__main__":
		if len(sys.argv) > 1:
				num_plays = int(sys.argv[1])
				print(rock_paper_scissors(num_plays))
		else:
				print('Usage: rps.py [num_plays]')