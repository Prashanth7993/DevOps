class Person:
    # def __init__(self,fname,age):
    #     self.fname = fname
    #     self.age=age
    # def printing(self):
    #     return f'Fname={self.fname},Age={self.age}'
    def __init__(self,fname='default_name',age=0):
        self.fname = fname
        self.age=age
        self.skills=[]
    def printing(self):
        return f'Fname={self.fname},Age={self.age}, skills={self.skills}'
    
    def skills_insertion(self,skills):
        self.skills.append(skills)

class Student(Person):
    def __init__(self, fname='default_name', age=0):
        super().__init__(fname, age)
        
    def printing(self):
        return f'{super().printing()}, studentId={self.studentId}'
    pass

s1 = Student(22,"ram")
#s1.skills_insertion("c")
print(s1.printing())

# p=Person("dev",22)
p=Person()
# print(p.fname," ",p.age)
print(p.printing())
p.skills_insertion("python")