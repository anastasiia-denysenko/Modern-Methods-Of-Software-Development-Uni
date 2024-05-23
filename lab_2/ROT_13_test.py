import rot13denysenko
from pytest import *
import sys
class Test_ROT13(TestCase):
    def test_stdout_stderr(capsys):
        otput_rot13("Hello world!")
        captured = capsys.readouterr()
        self.assertEqual(captured.out, "The output is: Uryyb jbeyq!")
        self.assertEqual(captured.err, "Starting process...\n")
    def test_exit_code(ROT_13.ROT13("Hello world!")):
        with pytest.raises(SystemExit) as e:
            otput_rot13("Hello world!")
        self.assertEqual(e.type, SystemExit)
        self.assertEqual(e.value.code, 0)
if __name__ == '__main__':
    pytest.main()
