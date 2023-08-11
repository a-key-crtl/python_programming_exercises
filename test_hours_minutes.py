from hours_minutes import get_hours_minutes_seconds


def main():
    test_sec()
    test_min()
    test_min_with_sec()
    test_hours()
    test_zero()
    
    
    
    
def test_sec():
    assert get_hours_minutes_seconds(30) == "30s"

def test_min():
    assert get_hours_minutes_seconds(60) == "1m"

def test_min_with_sec():
    assert get_hours_minutes_seconds(90) == "1m 30s"

def test_hours():
    assert get_hours_minutes_seconds(3600) == "1h"
    assert get_hours_minutes_seconds(3661) == "1h 1m 1s"
    assert get_hours_minutes_seconds(90042) == "25h 42s"

def test_zero():
    assert get_hours_minutes_seconds(0) == "0s"