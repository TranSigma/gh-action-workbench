from .pyrs import *
import dep_pkg
from zoneinfo import ZoneInfo
import tzlocal


__doc__ = pyrs.__doc__
if hasattr(pyrs, "__all__"):
    __all__ = pyrs.__all__


def sys_tz() -> ZoneInfo:
    dep_pkg.some_func()
    return tzlocal.get_localzone().unwrap_shim()
