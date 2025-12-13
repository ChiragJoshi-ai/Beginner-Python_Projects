import random

a = random.randint(1,100)

while True:
    b = int(input("Guess the no. between 1-100: "))
    if a == b:
        print("Correct!!")
        choice = input("Do you want to continue? (y/n): ").lower()
        if choice == "y":
            a = random.randint(1,100)
            continue
        else:
            break
    elif a > b:
        print("Too Low")
    elif a < b:
        print("Too High")
    else:
        print("Enter No. Only")
        break