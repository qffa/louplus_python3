#!/usr/bin/env python3

import sys

try:
	salary_value = int(sys.argv[1])
except:
	print("input invalid")
	exit()


tax_begin_point = 3500

salary_for_tax = salary_value - tax_begin_point


if salary_for_tax <= 0:
	tax_rate = 0
	tax_sub_value = 0

elif salary_for_tax < 1500:
	tax_rate = 0.03
	tax_sub_value = 0

elif salary_for_tax < 4500:
	tax_rate = 0.1
	tax_sub_value = 105

elif salary_for_tax < 9000:
	tax_rate = 0.2
	tax_sub_value = 555

elif salary_for_tax < 35000:
	tax_rate = 0.25
	tax_sub_value = 1005

elif salary_for_tax < 55000:
	tax_rate = 0.30
	tax_sub_value = 2755

elif salary_for_tax < 80000:
	tax_rate = 0.35
	tax_sub_value - 5505

else:
	tax_rate = 0.45
	tax_sub_value = 13505


tax_value = salary_for_tax * tax_rate - tax_sub_value


print(format(tax_value,".2f"))



