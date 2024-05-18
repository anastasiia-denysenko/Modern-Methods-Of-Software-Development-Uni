import  denysenko_ROT13 as rot
import sys
def test_stdin():
    assert rot.input == rot.sys.stdin.read()
