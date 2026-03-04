class Snapchat:
    def __init__(self,username,password,friends):
        self.username=username
        self.__password=password
        self._friends=friends
    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.password=new_password
    @property
    def oprFriends(self):
        return self._friends
    @oprFriends.setter
    def oprFriends(self,newfriend):
        self._friends.append(newfriend)
komali=Snapchat('komali','12345',['sneha','rishika'])
print(f"Name before modification:{komali.username}")
komali.username='lavanya'
print(f"Name after modification:{komali.username}")
print(f"Password before modification:{komali.getpassword()}")
komali.setpassword('K@123')
print(f"Password after modification:{komali.getpassword()}")
print(f"Friends before modification:{komali.oprFriends}")
komali.oprFriends='divya'
print(f"Friends after modification:{komali.oprFriends}")