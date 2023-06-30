from datetime import UTC
from zoneinfo import ZoneInfo

import dep_pkg

from pyrs import rs_sys_tz, sys_tz


def test_sys_tz():
    assert sys_tz() == ZoneInfo("Etc/UTC")


def test_rs_sys_tz():
    assert rs_sys_tz() == UTC


def test_other_pkg():
    assert dep_pkg.some_func()
