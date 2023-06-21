from pyrs import sys_tz, rs_sys_tz
import dep_pkg
from datetime import timezone
from zoneinfo import ZoneInfo


def test_sys_tz():
    assert sys_tz() == ZoneInfo('Etc/UTC')


def test_rs_sys_tz():
    assert rs_sys_tz() == timezone.utc


def test_other_pkg():
    assert dep_pkg.some_func()
