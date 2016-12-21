#!/usr/bin/python3
import re
import os.path

HOME = os.path.expanduser('~')
# Parse Load average
#with open(HOME+"/temp/load_avg") as file_handler:
#	load_avg = re.sub('[,]',' ',file_handler.readline()).split()
#	print(*load_avg, sep=' ')
# Parse CPU Load
with open(HOME+"/temp/cpu") as file_handler:
	cpu_names = file_handler.readline().lstrip('avg-cpu: ').split()
	cpu_val = file_handler.readline().split()
	print(*cpu_names, sep=' ')
	print(*cpu_val, sep=' ')
# Parse Disk Load
with open(HOME+"/temp/disk-load") as file_handler:
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
with open(HOME+"/temp/disk-data") as file_handler:
	space_names = file_handler.readline()
	other = file_handler.readlines()	
	print(len(other))
	print(space_names, end=' ')
	print(*other, end=' ')
with open(HOME+"/temp/disk-inodes") as file_handler:
	space_names = file_handler.readline()
	other = file_handler.readlines()	
	print(len(other))
	print(space_names, end=' ')
	print(*other, end=' ')
# Parse Net-Load
with open(HOME+"/temp/net-load") as file_handler:
	file_handler.readline()
	dump, r_names, t_names = file_handler.readline().split('|')
	r_names = r_names.split()
	t_names = t_names.split()
	inf_loads = [line.split(':',1) for line in file_handler.readlines()]
	rec =  []
	trans = []
	for line in inf_loads:
		split_line = line[1].split()
		rec.append([split_line[i] for i in range(len(r_names))])
		trans.append([split_line[i + len(r_names) - 1] for i in range(len(t_names))])
	[print(line[0], end=' ') for line in inf_loads]
	print()
	print(*r_names, sep=' ')
	print(*t_names, sep=' ')	
	for i in range(len(inf_loads)):
		this_rec = rec[i]
		print(*this_rec, sep=' ')
		this_trans = trans[i]
		print(*this_trans, sep=' ')
