#!/usr/bin/env python3

import sys

class Config(object):

	config = {}

	def __init__(self, configfile):

		with open(configfile, 'r') as file:
			for line in file:
			item = strip(line.split('=')[0])
			value = strip(line.split('=')[1])
			config[item] = value

	def get_config(self, item):
		
		return config[item]

def UserData(object):

	userdata = {}
	salaryslip = []

	def __init__(self, userdatafile):
		
		with open(userdatafile, 'r') as file:
			for line in file:
				uid = strip(line.split('=')[0])
				basesalary = strip(line.split('=')[1])

				userdata[uid] = basesalary


	def calculator(self, rate):
		
		for uid, basesalary in slef.userdata.items():
			if basesalary < rate.JiShuL:
				basevalue = rate.JishuL
			elif basesalary > rate.JishuH:
				basevalue = rate.JiShuH
			else:
				basevalue = basesalary

			i = 0
			salaryslip[i][0] = uid
			salaryslip[i][1] = basesalary
			salaryslip[i][2] = basevalue * (1 - rate.YangLao - rate.YiLiao - rate.ShiYe -rate.GongShang - rate.ShengYu - rate.GongJiJin)
			
			salary_for_tax = basesalary - salaryslip[i][2] - 3500




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


			salaryslip[i][3] = salary_for_tax * tax_rate - tax_sub_value

			salaryslip[i][4] = salaryslip[i][1] - salaryslip[i][2] - salaryslip[i][3]

			i += 1












for value in sys.argv[1:]:

	try:
		emp_id = int(value.split(":")[0])
		emp_base_salary = int(value.split(":")[1])
	except:
		print("Parameter Error")
		exit()
		
#	print(emp_id, emp_base_salary)
	
	salary_slip = salary_calc(emp_base_salary)
	
	print("%d:%.2f" % (emp_id,salary_slip['net_salary']))

#	print(salary_slip)


