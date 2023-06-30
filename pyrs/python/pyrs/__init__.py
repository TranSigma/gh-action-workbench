from zoneinfo import ZoneInfo

import dep_pkg
import tzlocal

from .pyrs import *

__doc__ = pyrs.__doc__  # noqa: A001
if hasattr(pyrs, "__all__"):
    __all__ = pyrs.__all__


def sys_tz() -> ZoneInfo:
    dep_pkg.some_func()
    return tzlocal.get_localzone().unwrap_shim()
