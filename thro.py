import random

n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess := to_be_guessed :
    guess = int(input("New number: "))
    if guess > 0:     
        print("Number too large")
    elif guess > to_be_guessed:
        print("Number too small")
    else: 
        print("sorry that you're giving up!")
        break
else:
    print("congratulations on you passed")            
    
# sum of the numbers fro the user till the enter stop
total_sum = 0
while True:
    user_input = input("Enter a number or type 'stop' to end: ")
    if user_input.lower() == 'stop':
     total_sum += int(user_input)
print("Total sum:", total_sum)
