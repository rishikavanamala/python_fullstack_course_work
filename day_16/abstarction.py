
#encapsulation
class snapchat:
    def __init__(self,username,password,friends):
        self.username = username
        self.__password1 = password #PRIVATE
        self._friends1 = friends #protected
    def getinfo(self):
        print(self.username)
        print(self.__password1)
        print(self._friends1)
    @property
    def protected_var(self):
        print("came to this  property function")
        return self._friends1
    @protected_var.setter
    def protected_var(self,new_friend):
        print("came to second function")
        self._friends1.append(new_friend)



sakeeth = snapchat("sakeeth","123@",["praveen","sapnil"])
sakeeth.getinfo()
p = sakeeth.protected_var
print(p)
sakeeth.protected_var = "rahul"
p1= sakeeth.protected_var
print(p1)






#abstraction:
from abc import ABC, abstractmethod
class class1:
    def common(self):
        print("this is the common function")
    @abstractmethod
    def fun1(self):
        pass
    @abstractmethod
    def fun2(self):
        pass
class class2(class1):
    def fun1(self):
        print("class 2 fun1 ")
    def fun2(self):
        print("class 2 fun2")
class class3(class1):
    def fun1(self):
        print("class 3 fun1")
    def fun2(self):
        print("class 3 fun 2")


obj2 = class2()
obj3 = class3()
obj2.fun1()
obj2.fun2()
obj3.fun1()
obj3.fun2()


#polymorphism

class classa:
    def fun1(self):
        print("this is fun1 class1")

class classb(classa):
    def fun1(self):
        print("this is classb")

obj1 = classa()
obj2 = classb()
obj1.fun1()
obj2.fun1()





















































































