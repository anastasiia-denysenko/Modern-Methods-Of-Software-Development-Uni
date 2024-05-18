import  denysenko_ROT13 as rot
import sys
def test_stdin_fail():
    if rot.input != rot.sys.stdin.read():
        pytest.fail("input is not written to stdin.")
