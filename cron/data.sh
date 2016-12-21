#!/bin/bash
cp /home/temp/last_min /home/temp/previous_min;
~/cron/data_new_collector.sh;
~/cron/data_new_parser.py > /home/temp/last_min;

