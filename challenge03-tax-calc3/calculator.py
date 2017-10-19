#!/usr/bin/env python3

import sys

class Config(object):

	config = {}

	def __init__(self, configfile):

		with open(configfile, 'r') as file:
			for line in file:
				item = line.split('=')[0].strip()
				value = float(line.split('=')[1].strip())
				self.config[item] = value

	def get_config(self, item):
		
		return self.config[item]

class UserData(object):

	userdata = {}
	salaryslip = []

	def __init__(self, userdatafile):
		
		with open(userdatafile, 'r') as file:
			for line in file:
				uid = line.split(',')[0]
				basesalary = float(line.split(',')[1])

				self.userdata[uid] = basesalary


	def calculator(self, rate):
		
		for uid, basesalary in self.userdata.items():
			if basesalary < rate['JiShuL']:
				basevalue = rate['JiShuL']
			elif basesalary > rate['JiShuH']:
				basevalue = rate['JiShuH']
			else:
				basevalue = basesalary

			i = 0
			self.salaryslip.append([])
			self.salaryslip[i].append(uid)
			self.salaryslip[i].append(basesalary)
			self.salaryslip[i].append(basevalue * (1 - rate['YangLao'] - rate['YiLiao'] - rate['ShiYe'] -rate['GongShang'] - rate['ShengYu'] - rate['GongJiJin']))
			
			salary_for_tax = basesalary - self.salaryslip[i][2] - 3500

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


			self.salaryslip[i].append(salary_for_tax * tax_rate - tax_sub_value)

			self.salaryslip[i].append(self.salaryslip[i][1] - self.salaryslip[i][2] - self.salaryslip[i][3])

			i += 1

	


	def dumptofile(self, outputfile):

		with open(outputfile, 'w') as file:

			for i in self.salaryslip:
				file.write(str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]) + ',' + str(i[3]) + ','  + '\n')






if __name__ == '__main__':

	args = sys.argv[1:]

	index = args.index('-c')
	cfgfile = args[index + 1]
			
	index = args.index('-d')
	userfile = args[index + 1]

	index = args.index('-o')
	outputfile = args[index + 1]



	rate = Config(cfgfile)
	userdata = UserData(userfile)

#	print(rate.config)
	
#	r = rate.get_config('JiShuL')
#	print (r)

	userdata.calculator(rate.config)
	print(userdata.salaryslip)

#	userdata.dumptofile(outputfile)

		



