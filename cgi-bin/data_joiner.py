#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import os.path
import os


def average(list1, list2):
	return [(list1[i] + list2[i])/2 for i in range(len(list1))]  


def colored_float(string, color):
	if color == 'red':
		print('<span style="color:#FF0000"> {0:.2f}</span>'.format(string), end=' ')
	if color == 'yellow':	
		print('<span style="color:#FFFF00">{0:.2f}</span>'.format(string), end=' ')


def colored_table(string, color):
        if color == 'red':
                print('<td><span style="color:#FF0000">{}</span></td>'.format(string), end=' ')
        if color == 'yellow':
                print('<td><span style="color:#FFFF00">{}</span></td>'.format(string), end= ' ')

def colored_table_float(string, color):
        if color == 'red':
                print('<td><span style="color:#FF0000">{0:.2f}</span></td>'.format(string), end=' ')
        if color == 'yellow':
                print('<td><span style="color:#FFFF00">{0:.2f}</span></td>'.format(string), end= ' ')


def listen_sockets():
	listens = []
	with open("/proc/net/tcp") as file_handler:
		lines = file_handler.readlines()
		for l in lines:
			ls = l.split()
			if ls[3] == '0A':
				lp = ls[1].split(':')
				ip = str(lp[0])
				pair = "%s.%s.%s.%s:%s" %( int(ip[6:8], 16), int(ip[4:6], 16), int(ip[2:4], 16), int(ip[0:2], 16), int(lp[1], 16))
				listens.append(str(pair))
		return listens

with open("/home/temp/last_min") as last_min:
	with open("/home/temp/previous_min") as prev_min:
		# Load average
		avg = os.getloadavg()
#		last_avg =list( map(float, last_min.readline().split()))
#		prev_avg = list(map(float, prev_min.readline().split()))
		print('<p><strong>Load Average</strong>:', end=' ')
#		avg = average(last_avg, prev_avg)
		for elem in avg:
			if elem >= 0.9 or elem <= 0.05:
				colored_float(elem, 'red')
			elif elem >=0.8 or elem <=0.1:
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
		for i in range(len(avg)):
			if i != 2:
				print('<td>{0:.2f}</td>'.format(avg[i]))
			elif avg[i] >=90:
				print('<td><span style="color:#FF0000">{0:.2f}</span</td>'.format(avg[i]))
			elif avg[i] >=80:
				print('<td><span style="color:#FFFF00">{0:.2f}</span</td>'.format(avg[i]))
			else:
				print('<td>{0:.2f}</td>'.format(avg[i]))
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
			[print('<td>{0:.2f}</td>'.format(avg[i][j])) for j in range(6)]
			for j in range(6, len(avg[i])):
				if avg[i][j] >= 90 or (j == 7 and avg[i][j] >= 0.9):
					colored_table_float(avg[i][j], 'red')
				elif avg[i][j] >= 80 or (j == 7 and avg[i][j] >= 0.8):
					colored_table_float(avg[i][j], 'yellow')
				else:
					print('<td>{0:.2f}</td>'.format(avg[i][j]))
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
		    if not fs_splited_last[0] == 'tmpfs' or fs_splited_last[0] == 'udev':
		   	 fs_data_last.append(fs_splited_last)
		   	 fs_data_prev.append(fs_splited_prev)
		print('<table class="brd"><tr>')
		[print('<th>{}</th>'.format(space_names[i])) for i in range(5)]
		print('<th>{} {}</th>'.format(space_names[5],space_names[6]))
		print('</tr>')
		for i in range(len(fs_data_last)):
			print('<tr>')
			for j in range(len(space_names) - 1):
                            letter = fs_data_last[i][j][len(fs_data_last[i][j])-1]
                            if letter =='G':
                                val = '{0:.2f}'.format((float(fs_data_last[i][j].rstrip('G')) + float(fs_data_prev[i][j].rstrip('G')))/2)
                                print('<td>{}{}</td>'.format(val, letter))
                            elif letter == 'M':	
                                val = '{0:.0f}'.format((float(fs_data_last[i][j].rstrip('M')) + float(fs_data_prev[i][j].rstrip('M')))/2)
                                print('<td>{}{}</td>'.format(val, letter))
                            elif letter == '%':
                                val = (int(fs_data_last[i][j].rstrip('%')) + int(fs_data_prev[i][j].rstrip('%')))//2
                                if val >= 90:
                                    colored_table('{}{}'.format(val, letter), 'red')
                                elif val >= 80:
                                    colored_table('{}{}'.format(val, letter), 'yellow')
                                else:
                                    print('<td>{}{}</td>'.format(val, letter))
                            else:
                                print('<td>{}</td>'.format(fs_data_last[i][j]))
			print('</tr>')
		print('</table>')
		# INodes
		print('<h4>Free INodes</h4>')
		fs_num = int(last_min.readline())
		space_names = last_min.readline().split()
		prev_min.readline()
		prev_min.readline()
		fs_data_last = [] 
		fs_data_prev = []
		for i in range(fs_num):
		    fs_splited_last = last_min.readline().split()
		    fs_splited_prev = prev_min.readline().split()
		    if not fs_splited_last[0] == 'tmpfs' or fs_splited_last[0] == 'udev':
		   	 fs_data_last.append(fs_splited_last)
		   	 fs_data_prev.append(fs_splited_prev)
		print('<table class="brd"><tr>')
		[print('<th>{}</th>'.format(space_names[i])) for i in range(5)]
		print('<th>{} {}</th>'.format(space_names[5],space_names[6]))
		print('</tr>')
		for i in range(len(fs_data_last)):
			print('<tr>')
			for j in range(len(space_names) - 1):
                            letter = fs_data_last[i][j][len(fs_data_last[i][j])-1]
                            if letter =='G':
                                val = '{0:.2f}'.format((float(fs_data_last[i][j].rstrip('G')) + float(fs_data_prev[i][j].rstrip('G')))/2)
                                print('<td>{}{}</td>'.format(val, letter))
                            elif letter == 'K':	
                                val = '{0:.0f}'.format((float(fs_data_last[i][j].rstrip('K')) + float(fs_data_prev[i][j].rstrip('K')))/2)
                                print('<td>{}{}</td>'.format(val, letter))
                            elif letter == '%':
                                val = (int(fs_data_last[i][j].rstrip('%')) + int(fs_data_prev[i][j].rstrip('%')))//2
                                if val >= 90:
                                    colored_table('{}{}'.format(val, letter), 'red')
                                elif val >= 80:
                                    colored_table('{}{}'.format(val, letter), 'yellow')
                                else:
                                    print('<td>{}{}</td>'.format(val, letter))
                            else:
                                print('<td>{}</td>'.format(fs_data_last[i][j]))
			print('</tr>')
		print('</table>')
		# Net Load
		inf_names = last_min.readline().split()
		rec_names = last_min.readline().split()
		trans_names = last_min.readline().split()
		prev_min.readline()
		prev_min.readline()
		prev_min.readline()
		rec_avg = []
		trans_avg = []
		for i in range(len(inf_names)):
			rec_last = list(map(int, last_min.readline().split()))
			rec_prev = list(map(int, prev_min.readline().split()))
			rec_avg.append(list(map(int, average(rec_last, rec_prev ))))
			trans_last = list(map(int, last_min.readline().split()))
			trans_prev = list(map(int, prev_min.readline().split()))
			trans_avg.append(list(map(int, average(trans_last, trans_prev))))
#		Цельная таблица - плохо читается в elinks :(
#		print('<h3>Net Load</h3><table class="brd"><tr><th>Interface</th><th colspan="{}" align="center">Recieved</th><th colspan="{}" align="center">Transmitted</th></tr>'.format(len(rec_names), len(trans_names)))
#		print('<tr><td></td>')
#		[print('<th>{}</th>'.format(name)) for name in rec_names]
#		[print('<th>{}</th>'.format(name)) for name in trans_names]
#		print('</tr>')
#		for i in range(len(inf_names)):
#			print('<tr><td>{}</td>'.format(inf_names[i]))
#			[print('<td>{}</td>'.format(val)) for val in rec_avg[i]]
#			[print('<td>{}</td>'.format(val)) for val in trans_avg[i]]
#			print('</tr>')
#		print('</table>')
		print('<h3>Net Load</h3><h4>Transmitted</h4><table class="brd"><tr><th>Interface</th><th colspan="{}" align="center">Recieved</th></tr>'.format(len(rec_names)))
		print('<tr><td></td>')
		[print('<th>{}</th>'.format(name)) for name in rec_names]
		print('</tr>')
		for i in range(len(inf_names)):
			print('<tr><td>{}</td>'.format(inf_names[i]))
			[print('<td>{}</td>'.format(val)) for val in rec_avg[i]]
			print('</tr>')
		print('</table>')
		print('<h4>Recieved</4><table class="brd"><tr><th>Interface</th><th colspan="{}" align="center">Transmitted</th></tr>'.format(len(trans_names)))
		print('<tr><td></td>')
		[print('<th>{}</th>'.format(name)) for name in trans_names]
		print('</tr>')
		for i in range(len(inf_names)):
			print('<tr><td>{}</td>'.format(inf_names[i]))
			[print('<td>{}</td>'.format(val)) for val in trans_avg[i]]
			print('</tr>')
		print('</table>')

		#Listens sockets
		print('<h3>Listen TCP sockets</h3><table class="brd"><tr><th>Sockets</th></tr>')
		listens = listen_sockets()
		for socket in listens:
			print('<tr><td>{}</td></tr>'.format(socket))
		print('</table>')
