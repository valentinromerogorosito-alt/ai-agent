from functions.write_file import write_file 


def print_debug_tests():
    print("\nResult for writing lorem.txt, content='wait, this isn't lorem ipsum':")
    test_one_result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Function result:\n  {test_one_result}")

    print("\nResult for writing pkg/morelorem.txt, content='lorem ipsum dolor sit amet':")
    test_two_result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Function result:\n  {test_two_result}")

    print("\nResult for writing /tmp/temp.txt, content='this should not be allowed':")
    test_three_result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Function result:\n  {test_three_result}")



if __name__ == "__main__":
    # TODO: unittest
    print_debug_tests()   
