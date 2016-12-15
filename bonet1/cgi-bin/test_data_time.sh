#!/bin/bash

dat_file=`date +%s -r /var/vhosts/bonet1/data/test`
dat=`date +%s`
result=`expr $dat - $dat_file`
temp=61
if [[ $result < 61 ]]
then ./new_data.sh
else ./old_data.sh
fi
