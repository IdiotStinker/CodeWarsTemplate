with open("input.txt", "r") as f:
	INPUT = f.read().split("\n")

from references.algorithms.convertbase import convertbase

print(convertbase("12", 10, 2))