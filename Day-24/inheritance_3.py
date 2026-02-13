class PersonalDetails:
    def __init__(self,name):
        self.Name = name
    def personaldetialsoutput(self):
        print(f"{self.name}")
class OccupationDetails:
    def __init__(self,income):
        self.income  = income
    def occupationdetails(self):
        print(f"{self.income}")

class EmployeeFor(PersonalDetails,OccupationDetails):
    def __init__(self, name,income):
        PersonalDetails.__init__(self,name)
        OccupationDetails.__init__(self,income)
    def alldetails(self):
        print(f"the name of employee : {self.name} and the income of em[ployee is {self.income}")
    
emp = EmployeeFor()
emp.alldetails()