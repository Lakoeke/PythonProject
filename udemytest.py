import random

#print("How many times do I have to tell you to clean up your room:")
#data = int(input())
#if isinstance(data, int):
#    for x in range(data):
#        print("Clean up your room")
#elif isinstance(data, str):
#    print("Please enter an integer")

#for num in range(1, 21):
#    if num % 2 == 0:
#        print(f"{num} is even")
#    elif num == 4 or num == 13:
#        print(f"{num} is unlucky")
#    else:
#        print(f"{num} is odd")

#x = 1
#while x < 10:
#    print("\U0001f600" * x)
#    x += 1

#msg = input("Hey how's it going? ")
#while msg != "stop copying me":
#    print(msg)
#    msg = input()

random_number = random.randint(1,10)
while True:
    msg = input("Guess a number between 1 and 10: ")
    msg = int(msg)
    if msg > random_number:
        print("too high")
    elif msg < random_number:
        print("too low")
    else:
        print("You guessed it you won!")
        play_again = input("Do you want to keep playing? (y/n)")
        if play_again == "y":
            random_number = random.randint(1,10)
            msg = None
        else:
            print("thank you for playing")
            break



