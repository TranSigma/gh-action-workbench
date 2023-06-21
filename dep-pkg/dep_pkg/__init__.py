'''Some local dependency.'''
import structlog

logger = structlog.stdlib.get_logger()

def some_func() -> bool:
    logger.info("I'm a function in dep-pkg.")
    return True
