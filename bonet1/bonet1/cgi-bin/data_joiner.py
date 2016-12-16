#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re


def average(list1, list2):
	return [(list1[i] + list2[i])/2 for i in range(len(list1))]  


def colored_float(string, color):
	if color == 'red':
		print('<span style="color:#FF0000"> {0:.2f}</span>'.format(string), end=' ')
	if color == 'yellow':	
		print('<span style="color:#FFFF00">{0:.2f}</span>'.format(string), end=' ')


with open("/var/vhosts/bonet1/data/last_min") as last_min:
	with open("/var/vhosts/bonet1/data/previous_min") as prev_min:
		# Load average
		last_avg =list( map(float, last_min.readline().split()))
		prev_avg = list(map(float, prev_min.readline().split()))
		print('<p><strong>Load Average</strong>:', end=' ')
		avg = average(last_avg, prev_avg)
		for elem in avg:
			if elem >= 0.9:
				colored_float(elem, 'red')
			elif elem >=0.8:
				colored_float(elem, 'yellow')
			else:
				print('{0:.2f}'.format(elem), end=' ')
		print('</p>')
		# CPU
		print('<h3>CPU Load</h3>')
		cpu_names = last_min.readline().split()
		last_val =  list(map(float, last_min.readline().split()))
		dump = prev_min.readline().split()
		prev_val = list(map(float, prev_min.readline().split()))
		avg = average(last_val, prev_val)
		print('<table class="brd"><tr>')
		for name in cpu_names:
			print('<th>{}</th>'.format(name))
		print('</tr> \n <tr>')
		for elem in avg:
			print('<td>{0:.2f}</td>'.format(elem))		
		print('</table>')
		#Disk Load
		print('<h3>Disk Load</h3>')
		disk_names = last_min.readline().split()
		devices_names = last_min.readline().split()
		devices_vals_last = [ list(map(float, last_min.readline().split())) for i in range(len(devices_names))]
		prev_min.readline()
		prev_min.readline()
		devices_vals_prev = [ list(map(float, prev_min.readline().split())) for i in range(len(devices_names))] 
		avg = [ average(devices_vals_last[i], devices_vals_prev[i]) for i in range(len(devices_names))]
		print('<table class="brd"><tr>\n<th>Devices: </th>\n')
		for name in disk_names:
			print('<th>{}</th>'.format(name))
		print('</tr>\n')
		for i in range(len(devices_names)):
		    print('<tr><th>{}</th>'.format(devices_names[i]))
		    [print('<td>{0:.2f}</td>'.format(val)) for val in avg[i]]
		    print('</tr>')
		print('</table>')
		# Disk blocks
		print('<h3>Disk Space Information</h3>')
		print('<h4>Free Space</h4>')
		fs_num = int(last_min.readline())
		space_names = last_min.readline().split()
		prev_min.readline()
		prev_min.readline()
		fs_data_last = [] 
		fs_data_prev = []
		for i in range(fs_num):
		    fs_splited_last = last_min.readline().split()
		    fs_splited_prev = prev_min.readline().split()
		    if not fs_splited_last[5] == '/dev' and not re.search('/sys',fs_splited_last[5]):
		   	 fs_data_last.append(fs_splited_last)
		   	 fs_data_prev.append(fs_splited_prev)
		for i in range(len(fs_data_last)):
			avg_list = []
			for j in range(len(space_names) - 1):
                            letter = fs_data_last[i][j][len(fs_data_last[i][j])-1]
                            if letter =='G':
                                val = '{0:.2f}'.format((float(fs_data_last[i][j].rstrip('G')) + float(fs_data_prev[i][j].rstrip('G')))/2)
                                print('{}{}'.format(val, letter))
                            elif letter == 'M':	
                                val = '{0:.0f}'.format((float(fs_data_last[i][j].rstrip('M')) + float(fs_data_prev[i][j].rstrip('M'))/2)
                            elif letter == '%':
                                val = '{}'.format((int(fs_data_last[i][j].rstrip('%')) + int(fs_data_prev[i][j].rstrip('%'))/2)
                                print('{}{}'.format(val, letter))
                            else:
                                print('{}'.format(fs_data_last[i][j]))
