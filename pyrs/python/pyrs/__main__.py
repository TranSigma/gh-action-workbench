from pyrs import rs_sys_tz, sys_tz


def main():
    py_tz = sys_tz()
    rs_tz = rs_sys_tz()
    print(  # noqa: T201
        f"Local timezone according to:\nPython: {py_tz} of type {type(py_tz)}\nRust: {rs_tz} of type {type(rs_tz)}"
    )


if __name__ == "__main__":
    main()
