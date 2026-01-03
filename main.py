from random import randint
a=randint(1,100)
num=int(input("Guess the number : "))
if num==a:
    print(f"you guessed number {a} at first move")
else:
    for i in range (1,101):
        if a<num:
            print("lower your guess")
        else:
            print("increase your guess")
        
        num=int(input("Guess the number again : "))
        if a==num:
            print(f"you guessed the number {a} at move {i}")
            break
        
   
   







