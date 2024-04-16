from denysenko_ROT13 import input 
import sys
def test_stdin(monkeypatch):
    monkeypatch.setattr('sys.stdin', input )
    assert input == sys.stdin.read()
