from denysenko_ROT13 import input 
def test_double(monkeypatch):
    monkeypatch.setattr('sys.stdin', input )
    assert input == 'Hello world!'
