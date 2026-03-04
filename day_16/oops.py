'''
class flipkart:
    discount =0
    @classmethod
    def updatediscount(cls,newdiscount):
        print("came to discount")
        cls.discount = newdiscount
    @staticmethod
    def banner():
        print("welcomeeeeeeeeeee!!!!!!!!!!")
 
    def userinfo(self,name,ph):
        self.name = name
        self.ph = ph
        print(name)
        print(ph)
    






sneha = flipkart()

komali = flipkart("komali","345678i9oijh")

flipkart.updatediscount(200)
sneha.updatediscount(200)
sneha.userinfo("sneha","123456789")
komali = flipkart()
rishika = flipkart()



'''



class Instagram:
    def __init__(self,name1,password):
        self.name1 = name1
        self.password = password
        print(name1)
        print(password)

rishika = Instagram("rishika","123456")












































