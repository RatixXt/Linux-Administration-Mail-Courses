#!/bin/bash
FILE="/var/vhosts/bonet1/data/last_min"
if [ -f $FILE ]
then {
	dat_file=`date +%s -r $FILE`
	dat=`date +%s`
	result=`expr $dat - $dat_file`
	temp=61
	if [[ $result < 61 ]]
	then ./new_data.sh
	else ./old_data.sh
	fi
}
else
{
	./old_data.sh
}
fi
