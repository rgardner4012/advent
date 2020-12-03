#!/usr/local/bin/python3.6
#import wget
import requests

expenseReport = requests.get('https://adventofcode.com/2020/day/1/input')
print(expenseReport.text)
