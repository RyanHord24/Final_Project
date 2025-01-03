class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if (
            type(new_name) == str
            and len(new_name) >= 3
            and new_name.isalpha()
            and new_name[0].isupper()
        ):
            self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if type(new_age) == int and new_age > 11 and new_age < 18:
            self._age = new_age

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if type(new_grade) == str and (
            new_grade == "9th" or new_grade == "10th" or new_grade == "11th" or new_grade == "12th"
        ):
            self._grade = new_grade