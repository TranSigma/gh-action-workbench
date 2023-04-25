from pyrs_build import sys_tz, rs_sys_tz
from datetime import timezone
from zoneinfo import ZoneInfo


def test_sys_tz():
    assert sys_tz() == ZoneInfo('Etc/UTC')


def test_rs_sys_tz():
    assert rs_sys_tz() == timezone.utc
