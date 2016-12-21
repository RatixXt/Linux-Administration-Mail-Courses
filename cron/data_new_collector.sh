#!/bin/bash
		
# First is load average
# top -b -n 1 | grep -e "[0-9]*\.[0-9]*, [0-9]*\.[0-9]*, [0-9]*\.[0-9]*" -o > ~/temp/load_avg;
# Second is cpu
iostat | grep -A 2 avg-cpu: > /tmp/cpu;
# Third is Disk Load
iostat -x | grep -A 1000 Device > /tmp/disk-load;
# Disk information: blocks
df -h > /tmp/disk-data;
# Disk information: INodes
df -h -i > /tmp/disk-inodes;
# Net Load
cat /proc/net/dev > /tmp/net-load;
# Listens sockets
# cat /proc/net/tcp > ~/temp/listens;
