def countdown(n): #defining a function
    newcountdown =[] #creating a list to print the new countdown in it
    while n >= 0: #identifying what my number will be and until what number the countdown will go on
        newcountdown.append(n) #adding the numbers to the list (append)
        n=n-1 #stating how the numbers will print by saying number to add to the list will be the number minus one so 5 minus one is 4 and so forth till we reach zero.

    return newcountdown#here we will call the function to return us the list which we call newcountdow

print(countdown(5))    #this is the print command which will print the new function. 


def printreturn(list): #define the function
    print(list[0]) #what is happenning here? we are printing the index value 0 from our list
    return list[0:2] #what is happening here? we are returning the indexes from zero to end
print(printreturn([7,40]))


def firstpluslength(newlist):#why do I have to state (newlist) here in the paranthesis
    
    print(newlist[0]) #why do I have to put a zero here?
    return len(newlist) #what is the return statement asking me to do?
print (firstpluslength([55,46,2])) #why do i say both return and print for my function? 


def valuesgreaterthansecond (list):
    if len(list)<2:
        return False
    thenewlist=[]
    for val in list:
        if val>list[1]:
            thenewlist.append(val)
    print(len(thenewlist))
    return thenewlist

print(valuesgreaterthansecond([100,200,360,40,20,60]))
print(valuesgreaterthansecond([43,56,78,88,99,34,45]))    


def lengthandvalue (size,value):
    anothernewList=[]
    for i in range(size):
        anothernewList.append(value)
    return anothernewList
print(lengthandvalue(10,2))        
