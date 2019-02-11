class Test:
   # name=''
    def setname(self,name):
        self.name = name
   # def __init__(self,name):
   #     self.name = name

class Test2(Test):
    def setname(self,name):
        self.name = name+' add'
    age=''

# my.name='aa'
my=Test()
my2=Test2()
my.setname('aa')
my2.setname('bb')
# my = Test('aa')
# my2 = Test2('bb')
my2.age = '25'
print(my.name,my2.name,my2.age,sep='\n',end='')