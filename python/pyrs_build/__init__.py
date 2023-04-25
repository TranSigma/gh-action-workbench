from .pyrs_build import *
from zoneinfo import ZoneInfo
import tzlocal


__doc__ = pyrs_build.__doc__
if hasattr(pyrs_build, "__all__"):
    __all__ = pyrs_build.__all__


def sys_tz() -> ZoneInfo:
    return tzlocal.get_localzone().unwrap_shim()
