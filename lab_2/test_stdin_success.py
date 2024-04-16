from denysenko_ROT13 import input, sys.stdin 
import sys
def test_stdin():
    assert input == sys.stdin.read()
