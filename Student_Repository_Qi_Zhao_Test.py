"""
This is HW08 unittest scripts. Written By Qi Zhao. Testing the following methods and class: date_arithmetic()-> Tuple[datetime, datetime, int]
file_reader(str, int, str, bool) -> Iterator[List[str]], class FileAnalyzer
"""
import unittest
import os

from typing import Dict
from HW08_Qi_Zhao import *

class HW08Test(unittest.TestCase):
    def test_date_arithmetic(self) -> None:
        self.assertTrue(date_arithmetic() == (datetime(2020,3,1), datetime(2019,3,2), 241))
        
    def test_file_reader(self) -> None:
        my_path: str = os.path.dirname(__file__)
        file_path: str = os.path.join(my_path, "hw08_test.txt")
        foo_path: str = os.path.join(my_path, "hw08_foo.txt")
        error_file_path: str = os.path.join(my_path, "hw08_test_error.txt")
        self.assertEqual(list(file_reader(file_path, 3)), [["CWID","Name","Major"],["123","Jin He","Computer Science"],
                                                        ["234","Nanda Koka","Software Engineering"],
                                                        ["345","Benji Cai","Software Engineering"]])
        with self.assertRaises(ValueError) as context:
            list(file_reader(error_file_path, 3))
        self.assertTrue("hw08_test_error.txt has 4 fields on line 1 but expected 3" in str(context.exception))
        with self.assertRaises(FileNotFoundError):
            list(file_reader(foo_path, 3))
            
class HW08FileAnalyzerTest(unittest.TestCase):
    my_path:str = os.path.dirname(__file__)
    foo_path:str = "/foo"
    def test_analyze_files(self) -> None:
        fa = FileAnalyzer(self.my_path)
        result: Dict[str, Dict[str, int]] = {
        '0_defs_in_this_file.py': {
            'class': 0,
            'function': 0,
            'line': 3,
            'char': 57
            }, 
        'file1.py': {
            'class': 2,
            'function': 4,
            'line': 25,
            'char': 270
            },
        'HW08_Qi_Zhao.py': {
            'class': 1,
            'function': 5,
            'line': 93,
            'char': 4026
            },
        'HW08_Test_Qi_Zhao.py': {
            'class': 2,
            'function': 4,
            'line': 67,
            'char': 2469
            },
        }
        self.assertEqual(fa.files_summary, result)
    
    def test_pretty_print(self) -> None:
        fa = FileAnalyzer(self.my_path)
        fa.pretty_print()
    
if __name__ == '__main__':
    unittest.main()