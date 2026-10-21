class Employee:
    company = "HP"
    def get_salary(self):#  self is a way to refering the object the class wahich is being created
        return 34000
    
    
e = Employee()
print(e.get_salary())
print(e.company)