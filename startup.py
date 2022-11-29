
# function definitions
import random
#random.randint(0, 1)
def rand(x):
    k= random.randint(0,(len(x)-1))
    return x[k]
def slow():
    num=0
    while True and num <1000:
        num+=1
print(random.randint(0, 1))
h=random.randint(2,7)
print (h)

# startup welcomes
print('This a life game (inspired by I.B, whoever she/he is) that is a bit more fun and with life choices')
print('i am gonna stop this chit-chat and start')
input('choose name')



#name choice
Relative=['Uncle', 'Aunt', 'Grand Mother', 'Dad' , 'Mom']
Named_after=['A star', 'a Porn Star', 'Sea food' 'your Dad']


#randoms
Binary=[0, 1]
sex=rand(Binary)
relative=rand(Relative)
named_after = rand(Named_after)
y=rand(Binary)


if y==0:
    print('You cant choose name. Your', str(relative), 'Chose for you')
else:
    print( 'You are named after ', str(named_after))





Countries=['Mexico', 'USA' , 'North Korea', 'China']
if Countries =='Mexico':
   name_list=[]
   death_list=[]
elif Countries=='USA':
    name_list=[]
    death_list =[]
elif Countries == 'North Korea':
    death_list=[]
    name_list =[]
elif Countries == 'China':
   death_list=[]
   name_list=[]

