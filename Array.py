from __future__ import print_function
from __future__ import unicode_literals

# Here we talk about the position of the arguments that how much they are important if the position ar wrong then it will creat an error.

def person(name,age=18):

    print(name)
    print(age)
    age = age-5
    print(age)
# Here we talk about the keyword argument that if the position is not correct still it will work by using the keyword


person('Hamid',20) #position argument
person(age = 20 ,name ='Hamid') #keyword argument

# default argument if one of them is not assigned a value

person('Hamid') #default argument

def sum(name,**b): # Keyword Variable length argument
    #print(name)
    for i,j in b.items():
        print(i,j)



sum(name ='Hamid',city='Kabul',age = 20,mob =1234)



