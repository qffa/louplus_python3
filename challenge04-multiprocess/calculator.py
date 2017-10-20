#!/usr/bin/env python3

import sys
from multiprocessing import Process, Queue

class Config(object):

	config = {}

	def __init__(self, configfile):

		with open(configfile, 'r') as file:
			for line in file:
				item = line.split('=')[0].strip()
				value = float(line.split('=')[1].strip())
				self.config[item] = value

	def get_config(self):
		
		return self.config

class UserData(object):

	userdata = {}
	salaryslip = []

	def __init__(self, userdatafile):
		
		with open(userdatafile, 'r') as file:
			for line in file:
				uid = int(line.split(',')[0])
				basesalary = float(line.split(',')[1])

				self.userdata[uid] = basesalary


	def calculator(self, rate):
		i = 0
		for uid, basesalary in self.userdata.items():
			if basesalary < rate['JiShuL']:
				basevalue = rate['JiShuL']
			elif basesalary > rate['JiShuH']:
				basevalue = rate['JiShuH']
			else:
				basevalue = basesalary

			self.salaryslip.append([])
			self.salaryslip[i].append(uid)
			self.salaryslip[i].append(basesalary)
			self.salaryslip[i].append(basevalue * (rate['YangLao'] + rate['YiLiao'] + rate['ShiYe'] + rate['GongShang'] + rate['ShengYu'] + rate['GongJiJin']))
			
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
				file.write(str(i[0]) + ',' + str(format(i[1],'.2f')) + ',' + str(format(i[2],'.2f')) + ',' + str(format(i[3],'.2f')) + ',' + str(format(i[4],'.2f')) + '\n')




q = Queue()



def readdata(cfgfile):
	

	rate = Config(cfgfile)

	q.put(rate.config)
	

#	print (rate.get_config())



def calculator(userfile):

	rate = q.get()

	userdata = UserData(userfile)

	userdata.calculator(rate)

	q.put(userdata.slaryslip)

	print(rate)
	print(userdata.salaryslip)


def dump(outputfile):

	data = q.get()
	
	userdata.dumptofile(outputfile)





def main():

	args = sys.argv[1:]

	index = args.index('-c')
	cfgfile = args[index + 1]
			
	index = args.index('-d')
	userfile = args[index + 1]

	index = args.index('-o')
	outputfile = args[index + 1]





	p1 = Process(target=readdata, args =(cfgfile, userfile))

	p2 = Process(target=calculator)
	
	p3 = Process(target=dump, args=(outputfile,))


	p1.start()
	p2.start()
	p3.start()

if __name__ == '__main__':
	main()



