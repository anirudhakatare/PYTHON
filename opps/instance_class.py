class Employee:
    company = "asus"
    
    def __init__(self,salary , name , bond , company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"the name of the employee is {self.name}. salary is {self.salary} the bond is for {self.bond}year car he have {self.company}")
    
    
e1 = Employee(34000,"ani",4,"tesla")
print(e1.company)
e1.get_info()


print(dir(e1))
