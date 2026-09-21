# Iterate 0 to 10 using for loop, do the same using while loop.
from matplotlib.pylab import number


for i in range(0,11):
    print(i)

#2 Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10,0,-1):
    print(i)
#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
for i in range(1,8):
    for j in range(1,i+1):
        print("#",end="")
    print()    

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
even_sum=0
odd_sum=0
for i in range(0,101):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i
print("The sum of all even number is =",even_sum)        
print("The sum of all odd number is =",odd_sum)        


# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for i in range(0,101):
    sum = sum + i
print("The sum of all numbers is =",sum)

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in  range(0,100):
    if i % 2 != 0:
        print(i)

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
programming_languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in programming_languages:
    print(i)

# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,101):
    if i % 2 == 0:
        print(i)
# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100 
 
for i in range(0,11):
    print(i,"x",i,"=",i*i)
    
# *
# **
# ***
# ****
# *****
for i in range(0,11):
    print(i,"x",i,"=",i*i)

for i in range (1,6):
    for j in range(1,i+1):
        print("*",end="")    
    print()

# *****
# ****
# ***
# **
# *
for i in range(6,0,-1):
    for j in range(1,i):
        print("*",end="")
    print()  

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
n=5
for i in range(1,11):
    print(n,"x",i,"=",n*i)      

# Find the largest number
n=[33,77,55,88,34,77,12,54,76,99,654,73,83]
largest = n[0]
for i in n:
    if i > largest:
        largest = i
print("The largest number is =", largest)


# Find the smallest number
n=[33,77,55,88,34,77,12,54,76,99,654,73,83]
smallest = n[0]
for i in n:
    if i < smallest:
       smallest = i
print("The smallest number is =", smallest)

for i in range(1,101):
    if i % 3 == 0:
        print(i)

# print factorial of a number     
n=5
factorial = 1
for i in range(1,n+1):
    factorial = factorial *i
print("The factorial of n is =", factorial)





# Find the second largest number
n=[33,77,55,88,34,77,12,54,76,99,654,73,83]
largest = second = float('-inf')
for i in n:
    if i > largest:
       second = largest
       largest = i
    elif i > second and i != largest:
        second = i
print("The second largest number is =",second)        