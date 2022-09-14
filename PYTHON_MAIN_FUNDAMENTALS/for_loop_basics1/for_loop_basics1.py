def zero_to_onefifty():
    for i in range(0,151):
        print(i)

zero_to_onefifty()

def multiples_of_five():
    number= int(5)
    for i in range(5,1001):
        print(number*i)
multiples_of_five() 

def counting_dojo_way():
    for i in range(1,101):
        if i % int(10)==(0):
            print('coding')
        elif i % int(5)==(0):
            print('Coding Dojo')
        else:
            print(i)    
counting_dojo_way()
def odd_int():
    total=0
    for i in range(1,500):
        if i % (2) != (0):
            total=(total+i)
        print(total)
odd_int()

def minus_four():
    for i in range(208,0,-4):
        print(i)
minus_four()


def flex_count():
    for i in range (2,10):
        if i % 3 == 0:
            print(i)
    
flex_count()        


