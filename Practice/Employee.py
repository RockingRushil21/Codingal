class Employee:
    def __init__(self,name,city,m_No,gender,designation):
        self.name=name
        self.m_No=m_No
        self.city=city
        self.gender=gender
        self.designation=designation

    def introEmployee(self):
        print("name = ",self.name)
        print("m_no = ",self.m_No)
        print("city = ",self.city)
        print("gender = ",self.gender)
        print("designation = ",self.designation) 

    def __del__(self):
        print("Obiect deleted successfully !!")  

e1 = Employee("Rushil","7013578589","Hyderabad","Male","Data Engineer")
e1.introEmployee() 

print(e1.name) 
print(e1.city)

        
