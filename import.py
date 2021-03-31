import os
import sys

from utils.utils import MYSQL_HOST_NEW, MYSQL_USER, MYSQL_PASS_NEW, log


def start(db: str, catalog: str):
    list_sql = [os.path.join(os.path.dirname(os.path.abspath(__file__)), catalog, i) for i in os.listdir(catalog)]
    log.info(f'База {db}. Всего таблиц {len(list_sql)}')
    for sql_file in list_sql:
        log.info(f'импортируем {sql_file}...')
        command = f'/usr/bin/mysql -h {MYSQL_HOST_NEW} -D {db} -u {MYSQL_USER} -p{MYSQL_PASS_NEW} < "{sql_file}"'
        # TODO нужно сделать асинхронный импорт всех таблиц сразу
        os.popen(command).read()


if __name__ == '__main__':
    log.info('Импорт sql-дампов из каталога в новую базу')
    if len(sys.argv) != 3:
        log.info('Параметры запуска python3 import.py <имя_базы> <каталог_с_sql_файлами>')
        exit(1)
    start(sys.argv[1], sys.argv[2])
