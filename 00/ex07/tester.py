import subprocess


def test_morse_encoder(input_text, expected_output):
    output = subprocess.check_output(["python", "sos.py", input_text],
                                     stderr=subprocess.STDOUT, text=True)
    if (output.strip() != expected_output.strip()):
        print(f"Test failed: Input: '{input_text}'")
        print(f"Expected: '{expected_output}', \nOutput: '{output.strip()}'\n")
        return 0
    else:
        assert output.strip() == expected_output.strip()
        print(f"Test passed: Input: '{input_text}'")
        print(f"Expected: '{expected_output}', \nOutput: '{output.strip()}'\n")
        return 1


if __name__ == "__main__":
    test_cases = [
        ("Hello World", ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."),
        ("123", ".---- ..--- ...--"),
        ("Python", ".--. -.-- - .... --- -."),
        ("%", "AssertionError: the arguments are bad"),
        ("Hello?123", "AssertionError: the arguments are bad"),
        ("   ", "/ / /"),
        ("", "AssertionError: the arguments are bad"),
    ]
    passed_tests = 0
    count_test = 0
    for input_text, expected_output in test_cases:
        count_test += 1
        print(f"\033[33m ------------- Teste: {count_test} --------- \033[0m")
        if (test_morse_encoder(input_text, expected_output)):
            print("\033[32m    OK\033[0m")
            passed_tests += 1
        else:
            print("\033[31m    FAIL\033[0m")

    color = "31m"
    if (count_test == passed_tests):
        color = "32m"

    print("\033["+color+"{} out of {} \
    tests passed\033[0m".format(passed_tests, len(test_cases)))
