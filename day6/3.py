'''
题⽬：
1.创建Person类，属性有姓名、年龄、性别，创建⽅法personInfo,打印这个⼈的信息
2.创建Student类，继承Person类，属性有学院college，班级class，重写⽗类personInfo⽅法，除了调⽤⽗类⽅法打印个⼈信息外，将学⽣的学院、班级信息也打印出来
3.重写 str ⽅法，返回student的信息。
程序分析：善⽤搜索引擎；查询Python魔术⽅法
'''


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print(self.name)
        print(self.age)
        print(self.gender)


class Student(Person):
    def __init__(self, name, age, gender, college, cls):
        super().__init__(name, age, gender)
        self.college = college
        self.cls = cls

    def personInfo(self):
        super().personInfo()
        print(self.college)
        print(self.cls)

    def __str__(self):
        return f"name: {self.name}\nage: {self.age}\ngender: {self.gender}\ncollege:{self.college}\nclass:{self.cls}"
