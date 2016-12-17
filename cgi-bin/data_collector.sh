#!/bin/bash
		
# First is load average
top -b -n 1 | grep -e "[0-9]*\.[0-9]*, [0-9]*\.[0-9]*, [0-9]*\.[0-9]*" -o > /var/vhosts/bonet1/data/temp/load_avg;
# Second is cpu
iostat | grep -A 2 avg-cpu: > /var/vhosts/bonet1/data/temp/cpu;
# Third is Disk Load
iostat | grep -A 1000 Device > /var/vhosts/bonet1/data/temp/disk-load;
# Disk information: blocks
df -h > /var/vhosts/bonet1/data/temp/disk-data;
# Disk information: INodes
df -h -i > /var/vhosts/bonet1/data/temp/disk-inodes;
# Net Load
cat /proc/net/dev > /var/vhosts/bonet1/data/temp/net-load;
