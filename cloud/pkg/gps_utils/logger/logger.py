""" Provides better logging """
import json
from typing import Any, Dict, Optional, List
from google.cloud import logging as gcp_logger  # pip installed via "google-cloud-logging"
import logging as py_logger

# Instantiates a gcp logging client client, with a debug log level
# this posts logs to the gcp stackdriver logs.
client = gcp_logger.Client()
client.setup_logging(log_level=py_logger.DEBUG)
_internal_logger = client.logger('incode-logger')

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
        }

        if kwargs != {}:
            json_print.update(kwargs)

        # default=str spits out everything that is not json searlisable as a string.
        # Nasty, but required to deal with things like datetime.datetime objects
        logs: Dict[str, str] = json.loads(json.dumps(json_print, default=str))

        # This prints to stdout - read by stackdriver
        _internal_logger.log_struct(logs)
