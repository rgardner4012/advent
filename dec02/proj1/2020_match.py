#!/usr/local/bin/python3.6

with open('input.txt', 'r') as expenseReport:
	passed = set()
	for line in expenseReport:
		yin = int(line.strip())
		yang = 2020 - yin
		if yang in passed:
			print('match!', yin, yang)
		else:
			passed.add(yin)

print('solution=', yin * yang)


