""" Provides better logging """
import json
import sys
from typing import Any, Dict, Optional, List


class slogger:
    @staticmethod
    def debug(msg: Any, *args, **kwargs) -> None:
        slogger._print_formatted("DEBUG", msg, args, **kwargs)

    @staticmethod
    def info(msg: Any, *args, **kwargs) -> None:
        slogger._print_formatted("INFO", msg, args, **kwargs)

    @staticmethod
    def warn(msg: Any, *args, **kwargs) -> None:
        slogger._print_formatted("WARNING", msg, args, **kwargs)

    @staticmethod
    def error(msg: Any, *args, **kwargs) -> None:
        slogger._print_formatted("ERROR", msg, args, **kwargs)

    @staticmethod
    def crit(msg: Any, *args, **kwargs) -> None:
        slogger._print_formatted("CRITICAL", msg, args, **kwargs)

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
        }

        if kwargs != {}:
            json_print.update(kwargs)

        # default=str spits out everything that is not json searlisable as a string.
        # Nasty, but required to deal with things like datetime.datetime objects
        logs: Dict[str, str] = json.loads(json.dumps(json_print, default=str))

        # This dumps the logs to stdout. From there stackdriver picks these up and
        # puts them into the gcp logging viewer.
        print(json.dumps(logs))
        sys.stdout.flush()
