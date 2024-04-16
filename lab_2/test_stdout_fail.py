import denysenko_ROT13 as rot
import sys
output = str(ROT13(input))+"\n"+str(ROT13(ROT13(input)))
def test_stdin_fail():
    if output != rot.sys.stdout.read():
        pytest.fail("Output is not written to stdout.")
