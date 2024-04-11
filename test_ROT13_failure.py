from denysenko_ROT13 import ROT13, test
def test_function_faliure():
    if test() == "incorrect":
        pytest.fail("The function works incorrectly.")
