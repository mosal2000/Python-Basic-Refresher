from typing import List


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result):
        self.grades.append(result)


zaid = Student("Zaid")
zaid.take_exam(90)
print(zaid)

# -- as dataclass --

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    grades: List[int] = field(
        default_factory=list
    )  # if we want to run a function, use default_factory and it will run the function to generate the default

    def take_exam(self, result):
        self.grades.append(result)


zaid = Student("Zaid")

zaid.take_exam(90)
print(zaid.grades)
print(zaid)
