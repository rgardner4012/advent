#!/usr/local/bin/python3.6

with open('input.txt', 'r') as expenseReport:
	for x in expenseReport.readlines():
		print(x)
		yang = 2020 - int(x)
		print(yang)
		if x == yang:
			print('match!')

