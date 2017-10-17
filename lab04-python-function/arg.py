#!/usr/bin/env python3

def connect(ipaddr, ports):
	print("IP: ", ipaddr)
	print("Ports: ", ports)
	ipaddr = '10.10.10.1'
	ports.append(8080)


if __name__ == "__main__":
	ipaddr = '192.168.1.1'
	ports = [22,23,24]
	print("before connect:")
	print("IP: ", ipaddr)
	print("Ports: ", ports)

	print("In connect:")
	connect(ipaddr, ports)

	print("After connect:")
	
	print("IP: ", ipaddr)
	print("Ports: ", ports)
