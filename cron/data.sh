#!/bin/bash
FILE="/tmp/last_min"
if [ -f $FILE ]
then {
	cp /tmp/last_min /tmp/previous_min;
	~/cron/data_new_collector.sh;
	~/cron/data_new_parser.py > /tmp/last_min;
}
else {
	~/cron/data_new_collector.sh;
	~/cron/data_new_parser.py > /tmp/last_min;
	cp /tmp/last_min /tmp/previous_min
}
fi
