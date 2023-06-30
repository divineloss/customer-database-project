# defining the Person class with the required attibutes
class Person:
    def __init__(self, fname, lname, age, gender, income, status):  # attributes
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender
        self.income = income
        self.status = status

    def return_json(
        self,
    ):  # this is a method called return_json that takes in the argument/parameter called "self", which is already referenced in the Person object/class
        data = {
            "fname": self.fname,
            "lname": self.lname,
            "age": self.age,
            "gender": self.gender,
            "income": self.income,
            "status": self.status,
        }
        return data
