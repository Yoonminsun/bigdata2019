class Test:
   # name=''
   #  def setname(self,name):
   #      self.name = name
   def __init__(self,name):
       self.name = name

class Test2(Test):
    age=''

# my.name='aa'
# my.setname('aa')
my = Test('aa')
my2 = Test2('bb')
my2.age = '25'
print(my.name,my2.name,my2.age,sep='\n',end='')