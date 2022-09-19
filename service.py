import re
from typing import Generator, Any


def filter_(data: Generator, param: str) -> list[str]:
    return list(filter(lambda x: param in x, data))


def map_(data: Generator, param: str) -> list[str]:
    column: int = int(param)
    return list(map(lambda x: x.split(' ')[column], data))


def unique_(data: Generator, *args: Any, **kwargs: Any) -> list[str]:
    return list(set(data))


def sorted_(data: Generator, param: str) -> list[str]:
    revers_param: bool = True if param == 'desc' else False
    return sorted(data, reverse=revers_param)


def limit_(data: Generator, param: str) -> list[str]:
    limit_number: int = int(param)
    return list(data)[:limit_number]


def file_generator(file_name: str) -> Generator:
    for row in open(f"data/{file_name}", 'r'):
        yield row


def regex_(data: Generator, param: str) -> list:
    res = re.compile(param)
    return list(filter(lambda x: re.search(res, x), data))
