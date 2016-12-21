#!/bin/bash
		
# First is load average
# top -b -n 1 | grep -e "[0-9]*\.[0-9]*, [0-9]*\.[0-9]*, [0-9]*\.[0-9]*" -o > ~/temp/load_avg;
# Second is cpu
iostat | grep -A 2 avg-cpu: > ~/temp/cpu;
# Third is Disk Load
iostat -x | grep -A 1000 Device > ~/temp/disk-load;
# Disk information: blocks
df -h > ~/temp/disk-data;
# Disk information: INodes
df -h -i > ~/temp/disk-inodes;
# Net Load
cat /proc/net/dev > ~/temp/net-load;
# Listens sockets
# cat /proc/net/tcp > ~/temp/listens;
