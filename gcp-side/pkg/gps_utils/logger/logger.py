""" Provides better logging """
import json
from typing import Any, Dict, Optional, List
from time import ctime


class logger:
    @staticmethod
    def debug(msg: Any, *args, **kwargs) -> None:
        logger._print_formatted("DEBUG", msg, args, **kwargs)

    @staticmethod
    def info(msg: Any, *args, **kwargs) -> None:
        logger._print_formatted("INFO", msg, args, **kwargs)

    @staticmethod
    def warn(msg: Any, *args, **kwargs) -> None:
        logger._print_formatted("WARNING", msg, args, **kwargs)

    @staticmethod
    def error(msg: Any, *args, **kwargs) -> None:
        logger._print_formatted("ERROR", msg, args, **kwargs)

    @staticmethod
    def crit(msg: Any, *args, **kwargs) -> None:
        logger._print_formatted("CRITICAL", msg, args, **kwargs)

    @staticmethod
    def _print_formatted(level: str, msg: Any, *args, **kwargs) -> None:

        args: List[Optional[Any]] = list(args[0])

        message: str = str(msg)

        if args:
            message: str = message + ' ' + ' '.join(map(str, args))

        # construct the desired logging format here
        json_print: Dict[str, str] = {
            'severity': level,
            'message': message,
            'timestamp': ctime(),
        }

        if kwargs != {}:
            json_print.update(kwargs)

        # default=str spits out everything that is not json searlisable as a string.
        # Nasty, but required to deal with things like datetime.datetime objects
        logs = json.dumps(json_print, default=str)

        # This prints to stdout - read by stackdriver
        print(logs)
