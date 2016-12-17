#!/bin/bash

exec()
{
	if [ $USER = "root" ]
	then
	{
		$1
	}
	else
	{
		sudo $1
	}
	fi
}

exec "apt-get install nginx"
