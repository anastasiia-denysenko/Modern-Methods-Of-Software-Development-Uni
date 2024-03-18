from dumb_code_denysenko import function1, function2
def test_function1_faliure():
    if function1(1) == "incorrect":
        pytest.fail("The function works incorrectly.")

def test_function2_faliure():
    if function2(2) == "incorrect":
        pytest.fail("The function works incorrectly.")
