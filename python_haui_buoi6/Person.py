class Person:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
    def display(self) -> str:
        return "ten "+self.name + ", tuoi: "+self.age
   

class Student(Person):
    def __init__(self, name, age,section):
        super().__init__(name, age)
        self.section =section
    def displayStudent(self):
        return super().display() + ",section: "+ self.section
    

st = Student('dat','20','software')
print(st.displayStudent())