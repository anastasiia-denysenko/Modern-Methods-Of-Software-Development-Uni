import denysenko_ROT13 as rot
import sys
output = str(rot.ROT13(rot.input))+"\n"+str(rot.ROT13(rot.ROT13(rot.input)))
def test_stdin_fail():
    if output != rot.sys.stdout.read():
        pytest.fail("Output is not written to stdout.")
