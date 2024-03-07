# Worked Exercise 3.1 and 2 
sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except: 
    print("Error, please enter numeric input")
    quit()

#print(fh, fr)
if fh>40:
    print("Overtime")
    reg = fr * fh 
    otp = (fh - 40.0) * (fr * 0.5)
    #print(reg,otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh*fr
print("Pay:",xp)

# Exercise 5.1
num = 0 
tot = 0.0 
# infinite loop 
while True: 
    sval = input("Enter a number: ")
    if sval == 'done' :
           break
    try:
        fval = float(sval)
    except: 
        print("invalid input")
        continue
    print(fval)
    num = num + 1 
    tot = tot + fval 

print("ALL DONE")
print(tot,num,tot/num)

# Number Guessing Game 

import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): 
        top_of_range = int(top_of_range)
        if top_of_range <= 0: 
            print("Please type a number larger than 0 next time.")
            quit() 
else: 
    print("Please type a number next time.")
    quit()

random_number = random.randrange(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit(): 
        user_guess = int(user_guess)
    else: 
        print("Please type a number next time.")
        continue

    if user_guess == random_number: 
        print("You got it!")
        break
    elif user_guess > random_number: 
            print("You were above the number!")
    else: 
        print("You were below the number!")

print("You got it in", guesses, "guesses")


