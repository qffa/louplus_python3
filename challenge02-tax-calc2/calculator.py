#!/usr/bin/env python3

import sys

l = []
for i in range((len(sys.argv) - 1)):
	l.append(tuple(sys.argv[i + 1].split(":")))

employee = dict(tuple(l))

print(employee)


def print_employee_tax(employee):

	for key, value in employee.items():
		try:
			empid = int(key)
			empsalary = int(value)
		except:
			print("Parameter Error")
			exit()
		
		print(empid,format(tax(empsalary),".2f"))



def tax(salary_value):
	social_insurance_rate = {"pension": 0.08, "medical":0.02, "unemployment":0.005, "house_founding":0.06, "birth":0, "injury":0}

	social_insurance_rate_sum = sum(list(social_insurance_rate.values()))


	tax_begin_point = 3500


	salary_for_tax = salary_value * (1 - social_insurance_rate_sum) - tax_begin_point


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


	return (salary_for_tax * tax_rate - tax_sub_value)


#	print(format(tax_value,".2f"))



print_employee_tax(employee)
