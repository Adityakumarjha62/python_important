# Reverse a string:

a="aditya"
rev=""
for i in a:
    rev =  i + rev
print(rev)    

# check palindrome

a="madam"
rev = ""
for i in a:
    rev = i + rev
if rev == a:
    print(True)
else:
    print(False)    

# find largest number in a list:

list=[12,67,34,98,45,76,87,99,23,45,68,90]
largest=list[0]
for i in list:
    if i > largest:
        largest=i
print(largest)

# find second largest number:

arr=[12,67,34,98,45,76,87,99,23,45,68,90]
largest=second_largest=arr[0]
for i in arr:
    if i > largest:
        largest=second_largest
        largest=i
    elif i > second_largest and i != largest:
        second_largest=i
print(second_largest)    

# check prime number

n=18
for i in range(n,2):
    if n % 2 ==0:
        print("not Prime")
        break
else:
    print("prime")    

# count vowels in a string:

a="hello"
count=0
for i in a:
    if i in "aeiou,AEIOU":
        count+=1
print(count)        
    
# find even and odd number:

n=int(input("Enter a number:"))   
if n % 2 ==0:
    print("even")  
else:
    print("odd")    

# find sum of digit:

n=1020
sum = 0
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
print("sum of digit",sum)    

# Find Factorial 

n=5
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(factorial)    

# print Fibonacci series:

a=0
b=1
for i in range(7):
    print(a)
    c=a+b
    a=b
    b=c

# remove duplicate from a list    

list=[1,2,2,3,3,4,5]
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)        

# short a list:

list=[5,8,2,9,1,3,4,7,6]
list.sort()
print(list)

# find missing number:

n=[1,2,3,4,5,6,8,9]
for i in range(1,10):
    if i not in n:
        print("missing value",i)

# find duplicate number:

n=[1,2,3,3,4,5,5]
duplicate=[]
for i in n:
    if n.count(i) > 1 and i not in duplicate:
        duplicate.append(i)
print("duplicate number",duplicate)        

# count frequency of character;

a="hello"
counted = []
for i in a:
    if i not in counted:
        print(i, a.count(i))
        counted.append(i)

a="hello"
for i in a:
    print(i,a.count(i))


