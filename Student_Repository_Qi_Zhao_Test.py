"""
This is HW10 unittest scripts. Written By Qi Zhao. Testing the following methods and class: HW10
"""
import unittest

from Student_Repository_Qi_Zhao import *
from typing import List, Tuple, Iterator, Dict

class HW10Test(unittest.TestCase):
    test_path:str = os.path.dirname(__file__)
    
    def test_grades(self) -> None:
        stevens_data: "HW10" = HW10(self.test_path, "Stevens")
        stevens_data.pretty_print()
    
if __name__ == '__main__':
    unittest.main()