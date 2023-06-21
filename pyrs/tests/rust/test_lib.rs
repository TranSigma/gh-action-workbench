use chrono::offset::FixedOffset;
use pyrs::rs_sys_tz;


#[test]
fn test_rs_sys_tz()
{
    let tz = rs_sys_tz();
    let utc = FixedOffset::east_opt(0).unwrap();
    assert_eq!(tz, utc);
}
