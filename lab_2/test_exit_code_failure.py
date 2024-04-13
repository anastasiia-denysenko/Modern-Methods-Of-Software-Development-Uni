from denysenko_ROT13 import ROT13, test, code
def test_exit_code_faliure():
    if code != 0:
        pytest.fail("Exit code does not equal 0!")
