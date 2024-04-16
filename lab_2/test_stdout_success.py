import denysenko_ROT13 as rot
import sys
output = str(rot.ROT13(rot.input))+"\n"+str(rot.ROT13(rot.ROT13(rot.input)))
def test_stdout_success():
    assert output == rot.sys.stdout.read()
