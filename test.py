# def Func1():
#   x = 233
#   def Func2(x):
#       x *=x
#       return x
#   return Func2(x)
# Func1()

# def ask(Position_number=0):#第一层函数
#     def b():#第二层函数
#         print('打开文件B')
#     def c():
#         print('打开文件C')
#     def d():
#         print('打开文件D')
#     if(Position_number==0):
#         return(b())
#     if(Position_number==1):
#         return(c())
#     if(Position_number==2):
#         return(d())
# ask()
# class Stu:
#     name=None
#     age=None
#     school="华南理工大学"#类变量，被所有学生实例共有
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printName_Age(self):
#         print("我叫"+self.name+","+"今年"+str(self.age)+"岁。")
#     def printSchool(self):
#         print("来自",Stu.school)
#     def printTotal(self):
#         print("类中方法调用其他方法")
#         self.printName_Age()
#         self.printSchool()
# stu=Stu("大哥",19)
# stu.printName_Age()
# stu.printSchool()
# print("*****类中函数调用其他函数********")
# stu.printTotal()