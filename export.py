import os
import sys

from utils.utils import MYSQL_HOST_OLD, MYSQL_USER, MYSQL_PASS_OLD, sql_old, log

export_path = '/home/user/tmp'

# исключить конкретные таблицы
exclude_tables = []
# исключить таблицы, в названии которых содержатся строки
exclude_templates = []


def mysqldump(table: str, db: str):
    command = f'/usr/bin/mysqldump {db} --skip-lock-tables --skip-add-locks --add-drop-table --result-file="{export_path}/{db}-{table}.sql" -u{MYSQL_USER} -h{MYSQL_HOST_OLD} -p{MYSQL_PASS_OLD} {table} 2>/dev/null'
    os.popen(command).read()


def start(db: str):
    tables = sql_old(f'show tables from {db}', db).split('\n')[:-1]
    log.info(f'База {db}. Всего таблиц {len(tables)}')
    for table in tables:
        if table in exclude_tables:
            log.info(f'исключили {table}')
            continue
        if exclude_templates:
            set_of_exclude = {table.find(exclude) for exclude in exclude_templates}
            if len(set_of_exclude) != 1 or set_of_exclude.pop() != -1:
                log.info(f'исключили {table}')
                continue
        log.info(f'экспортируем {table}...')
        mysqldump(table, db)


if __name__ == '__main__':
    log.info('Экспорт всех таблиц в sql-дампы')
    if len(sys.argv) != 2:
        log.info('Параметры запуска python3 export.py <имя_базы>')
        exit(1)
    start(sys.argv[1])
