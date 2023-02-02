import pytest
import time_calc

def test_same_period():
        assert time_calc.add_time("3:30 PM", "2:12") == "5:42 PM"

def test_same_day():
        assert time_calc.add_time("2:30 AM", "14:12") == "4:42 PM"


