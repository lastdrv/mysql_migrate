import sys
from utils.utils import sql_old, sql_new, log


def count_old(table: str, db: str) -> str:
    return sql_old(f'select count(*) from {db}.{table}', db)


def count_new(table: str, db: str) -> str:
    return sql_new(f'select count(*) from {db}.{table}', db)


def start(db: str):
    tables = sql_old(f'show tables from {db}', db).split('\n')[:-1]
    log.info(f'База {db}. Всего таблиц {len(tables)}')
    for table in tables:
        log.info(f'для {table}...')
        log.info(f'в старой записей {count_old(table, db)}')
        log.info(f'в новой  записей {count_new(table, db)}')


if __name__ == '__main__':
    # TODO сделать чтобы не глазами смотреть совпадения цифр, а выводить предупреждения о несовпадении
    log.info('Сравнение количества записей потаблично в старой и в новых базах (на разных серверах)')
    if len(sys.argv) != 2:
        log.info('Параметры запуска python3 diff.py <имя_базы>')
        exit(1)
    start(sys.argv[1])
