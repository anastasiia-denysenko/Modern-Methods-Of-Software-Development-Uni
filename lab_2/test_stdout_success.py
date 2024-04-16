from denysenko_ROT13 import *
import sys
import subprocess
from io import StringIO
from contextlib import redirect_stdout, redirect_stderr
output = str(ROT13(input))+"\n"+str(ROT13(ROT13(input)))
def stdout_stderr(self, string_input, expection_stdout, expection_stderr):
    with StringIO() as stdout_buf, StringIO() as stderr_buf:
        with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
            result = subprocess.run(["python", "lab2/denysenko_ROT13.py"], input=string_input, text=True, capture_output=True)
        captured_stdout = result.stdout
        captured_stderr = result.stderr
    self.assertEqual(captured_stdout, output)
    self.assertEqual(captured_stderr, "")
