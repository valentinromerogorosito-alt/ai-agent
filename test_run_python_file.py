from functions.run_python_file import run_python_file


def print_debug_tests():
    print("\nResult for main.py, should return with calculator usage:")
    test_one_result = run_python_file("calculator", "main.py")
    print(f"Function result:  {test_one_result}")
    
    print("\nResult for main.py [\"3 + 5\"], should run the calculator:")
    test_two_result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"Function result:  {test_two_result}")

    print("\nResult for tests.py, should run the tests succesfully:")
    test_three_result = run_python_file("calculator", "tests.py")
    print(f"Function result:  {test_three_result}")

    print("\nResult for ../main.py, should return an error:")
    test_four_result = run_python_file("calculator", "../main.py")
    print(f"Function result:  {test_four_result}")

    print("\nResult for nonexistent.py, should return an error:")
    test_five_result = run_python_file("calculator", "nonexistent.py")
    print(f"Function result:  {test_five_result}")

    print("\nResult for lorem.txt, should return an error:")
    test_six_result = run_python_file("calculator", "lorem.txt")
    print(f"Function result:  {test_six_result}")

if __name__ == "__main__":
    # TODO: unittest
    print_debug_tests()
