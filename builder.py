from typing import Callable

import service

CMD_TO_SERVICE: dict[str, Callable] = {
    "filter": service.filter_,
    "map": service.map_,
    "unique": service.unique_,
    "sort": service.sorted_,
    "limit": service.limit_,
    "regex": service.regex_
}


def response_builder(path: str, cmd1: str, param1: str, cmd2: str, param2: str) -> list[str]:
    content = service.file_generator(path)
    step_one = CMD_TO_SERVICE[cmd1](data=content, param=param1)
    return CMD_TO_SERVICE[cmd2](data=step_one, param=param2)
