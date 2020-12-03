#!/usr/local/bin/python3.6
collection = []
sorted = []
with open('input.txt', 'r') as expenseReport:
	for line in expenseReport:
		collection = int(line.strip())
		sorted = collection.sort()
	print(sorted)
print('solution=', solution)


