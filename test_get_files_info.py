import unittest
from functions.get_files_info import get_files_info 


class TestGetFilesInfo(unittest.TestCase):
    def setUp(self):
        self.test_function = get_files_info

    def test_one(self):
        result = self.test_function("calculator", ".")
        expected_result = "Result for current directory:\n  - main.py: file_size=719 bytes, is_dir=False\n  - tests.py: file_size=1331 bytes, is_dir=False\n  - pkg: file_size=44 bytes, is_dir=True"
        self.assertEqual(result, expected_result)

    def test_two(self):
        result = self.test_function("calculator", ".")
        expected_result = "Result for current directory:\n  - main.py: file_size=719 bytes, is_dir=False\n  - tests.py: file_size=1331 bytes, is_dir=False\n  - pkg: file_size=44 bytes, is_dir=True"

    def test_three(self):
        result = self.test_function("calculator", ".")
        expected_result = "Result for current directory:\n  - main.py: file_size=719 bytes, is_dir=False\n  - tests.py: file_size=1331 bytes, is_dir=False\n  - pkg: file_size=44 bytes, is_dir=True"

    def test_four(self):
        result = self.test_function("calculator", ".")
        expected_result = "Result for current directory:\n  - main.py: file_size=719 bytes, is_dir=False\n  - tests.py: file_size=1331 bytes, is_dir=False\n  - pkg: file_size=44 bytes, is_dir=True"

def print_debug_tests():
    print("\nResult for current directory:")
    test_one_result = get_files_info("calculator", ".")
    print(f"Function result:  {test_one_result}")

    print("\nResult for 'pkg' directory:")
    test_two_result = get_files_info("calculator", "pkg")
    print(f"Function result:  {test_two_result}")
    
    print("\nResult for '/bin' directory:")
    test_three_result = get_files_info("calculator", "/bin")
    print(f"Function result:  {test_three_result}")
    
    print("\nResult for '../' directory:")
    test_four_result = get_files_info("calculator", "../")
    print(f"Function result:  {test_four_result}")


if __name__ == "__main__":
    # TODO: unittest.main()
    print_debug_tests()
