from io import StringIO
import pytest
input = 'Hello world!'
in_stream = io.BytesIO(input.encode('utf-8'))
sys.stdin = io.TextIOWrapper(in_stream, encoding='utf-8')
def test_double(self):
    self.setattr('sys.stdin', in_stream)
    assert in_stream == 'Hello world!'
