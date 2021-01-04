"""
This is HW11 Written By Qi Zhao. This file contains following functions and Class: HW10 
"""
import os
from typing import List, Tuple, Iterator, Dict
from prettytable import PrettyTable

class HW11:
    """ HW11 summarize student, instructor, and grades data in given universities. """
    def __init__(self, directory: str, university: str) -> None:
        """ initialize the instance and  """
        self.directory:str = directory
        self.university:str = university
        self.instructors:List[Tuple[str, str, str]] = []
        self.students:List[Tuple[str, str, str]] = []
        self.grades:List[Tuple[str, str, str, str]] = []
        self.majors:List[Tuple[str, str, str]] = []
        self.majors_summary:Dict[str, Tuple[List[str], List[str]]] = dict()
        self.student_summary:Dict[str,List[str,str,List[str],List[str],List[str],float]] = dict()
        self.my_path:str = ""
        self.gpa_table:Dict[str, float] = {
                                            "A":4.0, "A-":3.75,"B+":3.25,"B":3.0,"B-":2.75,"F":0.0,
                                            "C+":2.25, "C":2.0,"C-":0.0,"D":0.0,"D+":0.0,"D-":0.0,
                                        }
        self.analyze()
        
    def file_reader(self, fields:int, sep:str, header=False) -> Iterator[List[str]]:
        """ file_reader() to read field-separated text files and yield a tuple with all of the values 
            from a single line in the file on each call to next()
        """
        try:
            fp = open(self.my_path,'r')
        except FileNotFoundError:
            raise
        with fp:
            line_count: int = 0
            for my_line in fp:
                line_count += 1
                my_line = my_line.strip('\n')
                my_list:list = [ item for item in my_line.split(sep) ]
                if len(my_list) != fields:
                    raise ValueError(f"{self.my_path} has {len(my_list)} fields on line {line_count} but expected {fields}")
                else:
                    yield tuple(my_list)
    
    def analyze(self):
        """ read different files from repo and update students, instructors, and grades info.
        """
        # start to update students 
        self.my_path = os.path.join(self.directory,'students.txt')
        students_list:List = list(self.file_reader(3,'\t'))
        self.students.extend(students_list)
        # update instructors
        self.my_path = os.path.join(self.directory,'instructors.txt')
        instructors_list:List = list(self.file_reader(3,'\t'))
        self.instructors.extend(instructors_list)
        # update grades
        self.my_path = os.path.join(self.directory,'grades.txt')
        grades_list:List[Tuple[str,str,str,str]] = list(self.file_reader(4,'\t'))
        new_grades_list:List[Tuple[str,str,str,str]] = []
        for item1,item2,item3,item4 in grades_list[1:]:
            new_grades_list.append((item1,item2,self.gpa_table[item3],item4))
        self.grades.extend(new_grades_list)
        # update majors
        self.my_path = os.path.join(self.directory,'majors.txt')
        majors_list:List = list(self.file_reader(3,'\t'))
        self.majors.extend(majors_list)
    
    def pretty_print(self):
        """ print all the data through prettytable for students, instructors, and grades
        """
        x = PrettyTable() # print students
        x.field_names = ["CWID", "Name", "Major"]
        for item in self.students[1:]:
            my_row = []
            my_row.extend(item)
            x.add_row(my_row)
        print(x)
        
        y = PrettyTable() # print instructors
        y.field_names = ["CWID", "Name", "Department"]
        for item in self.instructors[1:]:
            my_row = []
            my_row.extend(item)
            y.add_row(my_row)
        print(y)
        
        z = PrettyTable() # print grades
        z.field_names = ["Student CWID", "Course Name", "Letter Grade", "Instructor CWID"]
        for item in self.grades:
            my_row = []
            my_row.extend(item)
            z.add_row(my_row)
        print(z)
        
        m_s = PrettyTable() # print major summary
        self.majors_summarize()
        print("Major Summary")
        m_s.field_names = ["Major", "Required Courses", "Electives"]
        for item1,items2 in self.majors_summary.items():
            my_row = []
            my_row.append(item1)
            my_row.extend(items2)
            m_s.add_row(my_row)
        print(m_s)
        
        # student_s = PrettyTable() # print student summary
        # self.student_summarize()
        # print("Student Summary")
        # student_s.field_names = ["CWID", "Name", "Major", "Complete Courses", "Remaining Required", "Remaining Electives", "GPA"]
        # for item1,items2 in self.student_summary.items():
        #     my_row = []
        #     my_row.append(item1)
        #     my_row.extend(items2)
        #     student_s.add_row(my_row)
        # print(student_s)
        
    def majors_summarize(self):
        """ generate major summary for each majors
        """
        for item1, item2, item3 in self.majors[1:]:
            if item1 in self.majors_summary.keys():
                if item2 == 'R':
                    self.majors_summary[item1][0].append(item3)
                else:
                    self.majors_summary[item1][1].append(item3)
            else:
                if item2 == 'R':
                    self.majors_summary[item1] = ([item3],[])
                else:
                    self.majors_summary[item1][1] = ([],[item3])
                    
    # def student_summarize(self):
    #     """ generate student summary for each students
    #     """
    #     for cwid, item2, major in self.students[1:]:
    #        self.student_summary[cwid] = [item2, major, [], self.majors_summary[major][0], self.majors_summary[major][1], 0.0]
    #     for cwid, c_name, item3 in self.grades[1:]:
    #         self.student_summary[cwid][2].append(c_name)
    #         self.student_summary[cwid][-1] = (float(item3)*(len(self.student_summary[cwid][2]-1)+float(self.student_summary[cwid][-1]))/len(self.student_summary[cwid][2])
    #         if (c_name == self.majors_summary[this_major][0]):
    #             self.student_summary[cwid][3].remove(c_name)
    #         else:
    #             self.student_summary[cwid][4].remove(c_name)