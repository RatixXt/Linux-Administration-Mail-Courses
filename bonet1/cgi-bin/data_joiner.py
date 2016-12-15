#!/bin/python3
with open("/var/vhosts/bonet1/data/last_min") as file_handler:
	print("{} I'm data joiner!".format(file_handler.read()))
