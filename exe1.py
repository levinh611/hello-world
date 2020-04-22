class MyClass:
    def __init__(self, Name, Age, Gender, DateOfBirth, Math):
        self.name = Name
        self.age = Age
        self.gender = Gender
        self.date = DateOfBirth
        self.math = Math
    def Gioithieu(self):
        return 'Xin chao toi la ' + self.name
    def Hi(self):
        return 'Xin chao toi ' + self.age +  'tuoi'

class School(MyClass):
    def __init__(self, Name, Age, Gender, DateOfBirth, Math , Teacher):
        MyClass.__init__(self, Name, Age, Gender, DateOfBirth, Math)
        self.teacher = Teacher

    def get_teacher(self):
        return '%s taught by %s'%(self.name , self.teacher)


if __name__ == "__main__":
    x = MyClass('Le Vinh', '19' , 'Male', '6/11/2001',9)
    y = School('Le Vinh', '19' , 'Male', '6/11/2001',9,'Mrs.Hoa')
    print(y.get_teacher())



