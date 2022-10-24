import random
number =  input("enter a number: ")
if number.isdigit():
     number = int(number)
     if number <= 0:
         print("enter a number larger then a 0")
         quit()
else:
    print("enter a digit next time!")

random_number = input(random.randint(0,number))
guess = int(input("guess the number: "))
guesse = 0
while True:
    guesse +=1
    if



