#!/bin/bash

# Экспорт прав пользователей

# FIXME иногда он вставляет двойную косую в выхлоп \\ такое надо вырезать
# когда в имени пользователя встречается нижнее подчёркивание

mysql -u${AND_USER} -p${AND_PASS_OLD} -h${AND_IP_OLD} -e"
	select concat('show grants for ','\'',user,'\'@\'',host,'\'') from mysql.user
	" > user_list_with_header.txt

sed '1d' user_list_with_header.txt > ./user.txt

while read user; do  
	mysql -u${AND_USER} -p${AND_PASS_OLD} -h${AND_IP_OLD} -e"$user" > user_grant.txt; sed '1d' user_grant.txt >> user_privileges.txt;
	echo "flush privileges" >> user_privileges.txt; 
done < user.txt

awk '{print $0";"}'  user_privileges.txt > user_privileges_final.sql
rm user.txt user_list_with_header.txt user_grant.txt user_privileges.txt
