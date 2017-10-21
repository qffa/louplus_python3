#!/usr/bin/env python3

import sys, getopt, configparser
from multiprocessing import Process, Queue
from datetime import datetime


class UserData(object):

	baseinfo = {}
	salaryslip = []

	def __init__(self, userfile):
		
		with open(userfile, 'r') as file:
			for line in file:
				uid = int(line.split(',')[0])
				basesalary = float(line.split(',')[1])

				self.baseinfo[uid] = basesalary


	def calculator(self, config):
		i = 0
		for uid, basesalary in self.baseinfo.items():
			if basesalary < config['jishul']:
				basevalue = config['jishul']
			elif basesalary > config['jishuh']:
				basevalue = config['jishuh']
			else:
				basevalue = basesalary

			self.salaryslip.append([])
			self.salaryslip[i].append(uid)
			self.salaryslip[i].append(basesalary)
			self.salaryslip[i].append(basevalue * (config['yanglao'] + config['yiliao'] + config['shiye'] + config['gongshang'] + config['shengyu'] + config['gongjijin']))
			
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

			t = datetime.now()
			t = datetime.strftime(t, '%Y-%m-%d %H:%M:%S')

			self.salaryslip[i].append(t)

			i += 1

	


	def dumptofile(self, outputfile):

		with open(outputfile, 'w') as file:

			for i in self.salaryslip:
				file.write(str(i[0]) + ',' + str(format(i[1],'.2f')) + ',' + str(format(i[2],'.2f')) + ',' + str(format(i[3],'.2f')) + ',' + str(format(i[4],'.2f')) + ',' + i[5] + '\n')









q = Queue()



def readcfg(cfgfile, cityname):
	

	config = configparser.ConfigParser()
	config.read(cfgfile)

	for section in config.sections():
		if section == cityname:
			section_data = config[section]
		else:
			section_data = config['DEFAULT']

	data = {}
	for key in section_data:
		data[key] = section_data.getfloat(key)


	q.put(data)


def calculator(userfile):

	config = q.get()
	userdata = UserData(userfile)
	userdata.calculator(config)

	q.put(userdata.salaryslip)



def dump(userfile,outputfile):

	data = q.get()
	userdata = UserData(userfile)

	userdata.salaryslip = data
	userdata.dumptofile(outputfile)




def main():

	def usage():
		print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'c:C:d:o:h', ['help'])
	except getopt.GetoptError as err:
		print(err)
		usage()
		sys.exit(2)


	for opt_name, opt_value in opts:
		if opt_name in ('-h', '--help'):
			usage()
			sys.exit()
		elif opt_name == '-C':
			cityname = opt_value
		elif opt_name == '-c':
			cfgfile = opt_value
		elif opt_name == '-d':
			userfile = opt_value
		elif opt_name == '-o':
			outputfile = opt_value
		else:
			assert False, "Unhandled option"






	p1 = Process(target=readcfg, args =(cfgfile,cityname))

	p2 = Process(target=calculator, args = (userfile,))
	
	p3 = Process(target=dump, args=(userfile,outputfile,))


	p1.start()
	p1.join()
	p2.start()
	p2.join()
	p3.start()
	p3.join()

if __name__ == '__main__':
	main()



