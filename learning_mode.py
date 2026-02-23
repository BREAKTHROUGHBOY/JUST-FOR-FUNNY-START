#ReEstablishment

print("Hello, Trillionare !")
import random

list = [i for i in range(1,7)]
attempts = 0

print(">>>  TRY U'R LUCKY NUMBER / ATTEMPT  <<<\n")

while True:
    
    inp  = input("P : PLAY, X : Quit  -->>  ".upper())

    if inp.lower() == "x":
        print("TQ FOR VISITING !")
        break

    elif inp.lower() == "p":
        number = random.choice(list)
        side1 = random.choice(["-", "^", "%", "#", "@", "!", "="])
        side2 = random.choice(["-", "^", "%", "#", "@", "!", "="])

        randoomm = f"\n       | {side1}  {number}  {side2} |"
        attempts += 1

        print(randoomm)

        if side1 == side2:

            print("\n///   Congrats, U Got it   ///".upper())
            print(f"///   NO.of attempts = {attempts}\n   Lucky Number = {number}\n    Lucky sign = {side1}   ///".upper())
            break

        else:
            print("!!!  > Try, Again <  !!!\n\n".upper())

print("ReEstablishment Successful !!!")