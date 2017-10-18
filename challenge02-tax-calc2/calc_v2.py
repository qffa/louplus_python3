#!/usr/bin/env python3

import sys



def salary_calc(base_salary):

	social_insurance_rate = {"pension": 0.08, "medical":0.02, "unemployment":0.005, "house_founding":0.06, "birth":0, "injury":0}

	social_insurance_rate_sum = sum(list(social_insurance_rate.values()))

	salary_slip = {}
	
	salary_slip['social_insurance'] = base_salary * social_insurance_rate_sum


	tax_begin_point = 3500

	salary_for_tax = base_salary * (1 - social_insurance_rate_sum) - tax_begin_point


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


	salary_slip['tax'] = salary_for_tax * tax_rate - tax_sub_value

	salary_slip['net_salary'] = base_salary - salary_slip['social_insurance'] - salary_slip['tax']

	salary_slip['base_salary'] = base_salary


	return(salary_slip)





for i in range((len(sys.argv) - 1)):

	try:
		emp_id = int(sys.argv[i + 1].split(":")[0])
		emp_base_salary = int(sys.argv[i + 1].split(":")[1])
	except:
		print("Parameter Error")
		exit()
		
#	print(emp_id, emp_base_salary)
	
	salary_slip = salary_calc(emp_base_salary)
	
	print("%d:%.2f" % (emp_id,salary_slip['net_salary']))

	print(salary_slip)


