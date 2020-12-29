"""
This is HW08 Written By Qi Zhao. This file contains following functions: date_arithmetic()-> Tuple[datetime, datetime, int]
file_reader(str, int, str, bool) -> Iterator[List[str]], class FileAnalyzer
"""
from typing import List, Tuple, Iterator, Dict
from datetime import datetime, timedelta
from prettytable import PrettyTable

def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ a function date_arithmetic to use Python’s datetime module to answer the following questions:
        What is the date three days after Feb 27, 2020?
        What is the date three days after Feb 27, 2019?
        How many days passed between Feb 1, 2019 and Sept 30, 2019?
    """
    three_days_after_02272020: datetime = # your code goes here for calculation
    three_days_after_02272019: datetime = # your code goes here for calculation
    days_passed_02012019_09302019: int = # your code goes here for calculation

    return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019
 
def file_reader(path: str, fields:int, sep=',', header=False) -> Iterator[List[str]]:
    """ file_reader() to read field-separated text files and yield a tuple with all of the values 
        from a single line in the file on each call to next()
    """
    pass

class FileAnalyzer:
    """ FileAnalyzer that given a directory name, searches that directory for Python files """
    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict() 

        self.analyze_files() # summerize the python files data

    def analyze_files(self) -> None:
        """ a method that populate the summarized data into self.files_summary"""
        pass # implement your code here

    def pretty_print(self) -> None:
        """ a method that print out the pretty table from the data stored in the self.files_summary."""
        pass # implement your code here