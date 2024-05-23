import rot13denysenko
from pytest import *
import sys
def test_stdout_stderr(capsys):
    otput_rot13("Hello world!")
    captured = capsys.readouterr()
    assert captured.out == "Uryyb jbeyq!"
    assert captured.err == "Starting process...\n"
def test_exit_code(ROT_13.ROT13("Hello world!")):
    with pytest.raises(SystemExit) as e:
        ROT_13.ROT13("Hello world!")
    assert e.type == SystemExit
    assert e.value.code == 0
