from denysenko_ROT13 import in_stream
def test_double(monkeypatch):
    monkeypatch.setattr('sys.stdin', in_stream)
    assert in_stream == 'Hello world!'
