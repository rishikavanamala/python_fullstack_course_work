'''class Instagram:
    def __init__(self,name1):
        self.name1 = name1
        print(name1)
        
    def intili(self,name):
        self.name = name
        print("ur name got intilizaed")

    def reels(self):
        print(self.name)
        print("this is the reels features")
        
    def post(self):
        print("ths is the postfeature")
        

rishika = Instagram()
rishika.intili("rishika")
rishika.reels()

'''
class instagram1:
    def __init__(self,username):
        self.username = username
        # self.password = password
        print(f"Hey {self.username}, Welcome")
    def reels(self):
        print("You csn upload and scroll")
    def posts(self):
        print("you can upload ur pics")
class instagram2(instagram1): 
    def __init__(self, username):
        self.username = username
        #super().__init__(username)
    def story(self):
        print("You can upload a story")
class instagram3(instagram2):
    def __init__(self, username):
       #super().__init__(username)
       self.username = username
    def notes(self):
        print("You can write the notes")
rishi = instagram1('rishi')
rishi.reels()
rishi.posts()
sneha = instagram2('sneha')
sneha.reels()
sneha.posts()
sneha.story()
komli = instagram3('komli')
komli.reels()
komli.posts()
komli.story()
komli.notes()
