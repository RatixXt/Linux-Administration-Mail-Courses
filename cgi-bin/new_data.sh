#!/bin/bash
cp /var/vhosts/bonet1/data/last_min /var/vhosts/bonet1/data/previous_min;
./data_collector.sh; 
./data_parser.py > /var/vhosts/bonet1/data/last_min;
./data_joiner.py  
