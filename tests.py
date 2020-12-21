#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2020
month = 12
day = 21

def test_code():
    assert main.divider(10, 2) == 5.0, " divider(10, 2) == 5.0 failed"
    assert main.divider(100, 4) == 25.0, " divider(100, 4) == 25.0 failed"
    assert main.divider(5, 4) == 1.25, " divider(5, 4) == 1.25 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
