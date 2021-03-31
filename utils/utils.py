import logging
import os

MYSQL_HOST_OLD = os.getenv('MYSQL_HOST_OLD')
MYSQL_HOST_NEW = os.getenv('MYSQL_HOST_NEW')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASS_OLD = os.getenv('MYSQL_PASS_OLD')
MYSQL_PASS_NEW = os.getenv('MYSQL_PASS_NEW')

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
log = logging.getLogger('')


def sql_old(request: str, db: str) -> str:
    command = f'/usr/bin/mysql -h {MYSQL_HOST_OLD} -D {db} -u {MYSQL_USER} -p{MYSQL_PASS_OLD} -N -e "{request};" 2> /dev/null'
    return os.popen(command).read()


def sql_new(request: str, db: str) -> str:
    command = f'/usr/bin/mysql -h {MYSQL_HOST_NEW} -D {db} -u {MYSQL_USER} -p{MYSQL_PASS_NEW} -N -e "{request};" 2> /dev/null'
    return os.popen(command).read()
