#!/bin/bash
cp /var/vhosts/bonet1/data/last_min /var/vhosts/bonet1/data/previous_min
./data_collector.sh | python3 data_parser.py > /var/vhosts/bonet1/data/last_min
python3 data_joiner.py  
