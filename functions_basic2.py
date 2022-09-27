#1 Countdown

def countdown(num):
    answer=[]
    for i in range(num,0,-1):
        answer.append(i)
    print(answer)

countdown(5)


#2 Print and Return
def print_and_return(num1,num2):
    print(num1)
    return num2

print(print_and_return(1,2))


#3 First Plus Length

def first_plus_length(list):
    x = list[0] + len(list)
    print(x)

first_plus_length([1,2,3,4,5])


#4 Values Greater than Second

def values_greater_than_second(list2):
    new_list=[]
    y=0
    if len(list2)>1:
        for i in range(len(list2)):
            if list2[i]>list2[1]:
                new_list.append(list2[i])
                y+=1
        print(y)
        return (new_list)
    else:
        return(False)


print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([2]))


#5 This Length, That Value

def length_and_value(int1,int2):
    newlist2=[]
    for i in range(int1):
        newlist2.append(int2)
    print (newlist2)

length_and_value(4,7)
length_and_value(6,2)