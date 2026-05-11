from functions.get_file_content import get_file_content 


def print_debug_tests():
    print("\nResult for lorem.txt, should be truncated:")
    test_one_result = get_file_content("calculator", "lorem.txt")
    print(f"Function result:  {test_one_result}")

    print("\nResult for main.py:")
    test_two_result = get_file_content("calculator", "main.py")
    print(f"Function result:  {test_two_result}")

    print("\nResult for pkg/calculator.py:")
    test_three_result = get_file_content("calculator", "pkg/calculator.py")
    print(f"Function result:  {test_three_result}")

    print("\nResult for /bin/cat, should return error string:")
    test_four_result = get_file_content("calculator", "/bin/cat")
    print(f"Function result:  {test_four_result}")

    print("\nResult for pkg/does_not_exist.py, should return error string:")
    test_five_result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Function result:  {test_five_result}")

if __name__ == "__main__":
    # TODO: unittest
    print_debug_tests()
