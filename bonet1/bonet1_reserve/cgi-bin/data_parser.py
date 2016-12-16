#!/usr/bin/python3
import re
# Parse Load average
with open("/var/vhosts/bonet1/data/temp/load_avg") as file_handler:
	load_avg = re.sub('[,]',' ',file_handler.readline()).split()
	print(*load_avg, sep=' ')
# Parse CPU Load
with open("/var/vhosts/bonet1/data/temp/cpu") as file_handler:
	cpu_names = file_handler.readline().lstrip('avg-cpu: ').split()
	cpu_val = file_handler.readline().split()
	print(*cpu_names, sep=' ')
	print(*cpu_val, sep=' ')
# Parse Disk Load
with open("/var/vhosts/bonet1/data/temp/disk-load") as file_handler:
	names = file_handler.readline().lstrip('Device: ').split()
	devices = file_handler.readlines()
	devices_names = []
	devices_vals = []
	for device in devices:
		if len(device) > 1:
			device_split = device.split()
			devices_names.append(device_split[0])
			devices_vals.append([float(device_split[i]) for i in range(1,len(device_split))])
	print(*names, sep=' ')
	print(*devices_names, sep=' ')
	[print(*vals, sep=' ') for vals in devices_vals]
with open("/var/vhosts/bonet1/data/temp/disk-data") as file_handler:
	space_names = file_handler.readline()
	other = file_handler.readlines()	
	print(len(other))
	print(space_names, end=' ')
	print(*other, end=' ')
