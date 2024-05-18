import rot13denysenko
import unittest
import sys
import unittest.mock
class TestROT13(unittest.TestCase):
    def test_if_function_works(self):
        self.assertEqual(ROT_13().ROT13(ROT_13().ROT13("Hello world")), "Hello world")
    def test_exit_code(self):
        with self.assertRaises(SystemExit) as cm:
            if ROT_13().ROT13(ROT_13().ROT13("Hello world")) == "Hello world":
                sys.stdout.write("Hello world!")
                sys.exit(0)
            else:
                print('The function does not work', file=sys.stderr)
                sys.exit(1)
            the_exception = cm.exception
            self.assertEqual(the_exception.code, 0)
    def test_stdin(self):
        denysenko_ROT13.raw_input = lambda _: 'Hello world!'
        ng = denysenko_ROT13.ROT_13()
        ng.get_name()
        self.assertEquals(ng.name, 'Hello world!')
class TestStdoutStderr(unittest.TestCase):
    def test_stdout(self, mockStdout):
        self.TestROT13.test_exit_code()
        mockStdout.write.assert_has_calls([
            mock.call("Hello world!")
        ])
    def test_stderr(self, mockStdout):
        self.TestROT13.test_exit_code()
        mockStdout.assert_not_called()
if __name__ == '__main__':
    unittest.main()
