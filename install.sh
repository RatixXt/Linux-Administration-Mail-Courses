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

exec "apt install sysstat";
exec "apt-get install nginx";
exec "cp ./conf/nginx/balinux /etc/nginx/sites-available/";
exec "ln -s /etc/nginx/sites-available/balinux /etc/nginx/sites-enabled/balinux";
exec "apt-get install apache2";
exec "cp ./conf/apache2/ports.conf /etc/apache2/";
exec "cp ./conf/apache2/bonet1.conf /etc/apache2/sites-available/";
exec "a2ensite bonet1";
# Возможно надо будет удалять дефолтные сайты
exec "mkdir -p /var/vhosts/bonet1";
exec "cp -r ./bonet1 /var/vhosts/";
exec "chown www-data:www-data -R /var/vhosts/bonet1/data";
exec "service apache2 restart";
exec "service nginx restart";
