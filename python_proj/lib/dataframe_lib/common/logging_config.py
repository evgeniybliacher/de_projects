import logging
import sys

import structlog

from dataframe_lib.common.logging_types import Logger


def configure_logging(
    log_level: int = logging.DEBUG,
) -> None:
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=log_level,
    )

    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(
                fmt="iso",
                utc=True,
            ),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            log_level
        ),
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


def create_logger(
    name: str,
    **context: object,
) -> Logger:
    logger = structlog.get_logger(name)

    if context:
        logger = logger.bind(**context)

    return logger