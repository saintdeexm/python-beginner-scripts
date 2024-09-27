# usimg while loop
sum_while = 0
i = 1
while i <=100:
    sum_while += i
    i += 1
    print("Sum using while loop:",sum_while)
# using for loop
sum_for = 0
for i in range(1, 101):
    sum_for += i
print("sum using foor loop:", sum_for)    

# print numbers from 10 to 1
i = 10
while i >= 1:
    print(i, end='')
    i -= 1
    
# function that prints each element of a list line by line
def print_list_element(list):
    for item in list :
        print(item)
        
my_list = [1, 2, 3, 4, 5, ]
print_list_element(my_list)   

#square numbers from 1 to 15
for i in range(1,16):
    print(i**2)     
    
# max num in a list using loop

def find_max(list):
    max_num = list[0]
    for num in list:
        if num > max_num:
            max_num  = num
            return max_num
        
my_list = [10, 20 ,30, 40, 50, 60, 70, 80, 90, 100]                 
print("Max number:",find_max(my_list))             

# prime num between 1 and 500
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1) :
        if num % i == 0:
            return False
        return True
    
    for i in range(1, 501):
        if is_prime(i):
            print(i, end='')
            
# count even and odd num in a list
numbers = [2, 3, 4, 7, 9, 12, 13, 15, 22, 24]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 ==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
        print("Even numbers:", even_numbers )
        
# multiplication table from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
        print()                            

# pattern using loop
for i in range(1, 6):
    for j in range(1, i +1):
        print(j, end=' ')
        print()