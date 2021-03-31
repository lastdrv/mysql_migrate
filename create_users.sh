#!/bin/bash

# Экспорт создания пользователей с паролями

# TODO скрипт немного не доделан
# он генерит строки вида
# CREATE USER 'user'@'host' IDENTIFIED WITH 'mysql_native_password' AS '*XXX' REQUIRE NONE PASSWORD EXPIRE DEFAULT ACCOUNT UNLOCK;
# а надо
# CREATE USER 'user'@'host' IDENTIFIED BY PASSWORD '*XXX';
# либо доделать либо править руками выхлоп


mysql -u${AND_USER} -p${AND_PASS_OLD} -h${AND_IP_OLD} -e"
	select concat('show create user ','\'',user,'\'@\'',host,'\'') from mysql.user
	" > user_list_with_header.txt

sed '1d' user_list_with_header.txt > ./user.txt

while read user; do  
	mysql -u${AND_USER} -p${AND_PASS_OLD} -h${AND_IP_OLD} -e"$user" > user_grant.txt; sed '1d' user_grant.txt >> user_privileges.txt;
	echo "flush privileges" >> user_privileges.txt; 
done < user.txt

awk '{print $0";"}'  user_privileges.txt > user_pass_final.sql
rm user.txt user_list_with_header.txt user_grant.txt user_privileges.txt
