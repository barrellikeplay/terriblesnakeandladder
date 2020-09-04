from time import sleep
from os import system
from random import randint

print("Snakes and ladders")
input("Press enter to continue")
system('cls')
sleep(1)
Playnum = int(0)
Comnum = int(0)

while True:
    while True:
        print("Your Square = " + str(Playnum))
        print("Computer Square = " + str(Comnum))
        print("Hint: Rise = 1, 4, 9, 21, 28, 36, 51, 71, 80(Instant Win)")
        print("Fall = 16, 48, 49, 56, 62, 64, 87, 93, 95, 98")
        input("Press enter to roll dice")
        system('cls')
        sleep(2)
        DiceP = int(randint(1, 6))
        print("Dice roll = " + str(DiceP))
        Playnum = Playnum + DiceP
        if Playnum > 100:
            print("Ouch you roll over")
            sleep(2)
            Playnum = int(Playnum) - 100
            Playnum = int(Playnum) - (int(Playnum) * 2)
            Playnum = int(Playnum) + 100
            system('cls')
        if Playnum == 1:
            Playnum = 38
        if Playnum == 4:
            Playnum = 14
        if Playnum == 9:
            Playnum = 31
        if Playnum == 21:
            Playnum = 42
        if Playnum == 28:
            Playnum = 84
        if Playnum == 36:
            Playnum = 44
        if Playnum == 51:
            Playnum = 67
        if Playnum == 71:
            Playnum = 91
        if Playnum == 80:
            Playnum = 100
        if Playnum == 16:
            Playnum = 6
        if Playnum == 48:
            Playnum = 26
        if Playnum == 49:
            Playnum = 11
        if Playnum == 56:
            Playnum = 53
        if Playnum == 62:
            Playnum = 10
        if Playnum == 64:
            Playnum = 60
        if Playnum == 87:
            Playnum = 24
        if Playnum == 93:
            Playnum = Playnum - 20
        if Playnum == 96:
            Playnum = Playnum - 20
        if Playnum == 98:
            Playnum = Playnum - 20
        if Playnum == 100:
            break
        if Playnum < 100:
            print("Your Square = " + str(Playnum))
        if DiceP < 6:
            break
        if DiceP == 6:
            print("Well you roll again")
            sleep(2)
            system('cls')
    if Playnum == 100:
        break
    print("Computer Turn")
    sleep(1)
    system('cls')
    while True:
        sleep(2)
        DiceC = int(randint(1, 6))
        print("Dice roll (Computer) = " + str(DiceC))
        Comnum = Comnum + DiceC
        if Comnum > 100:
            print("The computer roll over :D")
            sleep(2)
            Comnum = int(Comnum) - 100
            Comnum = int(Comnum) - (int(Comnum) * 2)
            Comnum = int(Comnum) + 100
            system('cls')
        if Comnum == 1:
            Comnum = 38
        if Comnum == 4:
            Comnum = 14
        if Comnum == 9:
            Comnum = 31
        if Comnum == 21:
            Comnum = 42
        if Comnum == 28:
            Comnum = 84
        if Comnum == 36:
            Comnum = 44
        if Comnum == 51:
            Comnum = 67
        if Comnum == 71:
            Comnum = 91
        if Comnum == 80:
            Comnum = 100
        if Comnum == 16:
            Comnum = 6
        if Comnum == 48:
            Comnum = 26
        if Comnum == 49:
            Comnum = 11
        if Comnum == 56:
            Comnum = 53
        if Comnum == 62:
            Comnum = 10
        if Comnum == 64:
            Comnum = 60
        if Comnum == 87:
            Comnum = 24
        if Comnum == 93:
            Comnum = Comnum - 20
        if Comnum == 95:
            Comnum = Comnum - 20
        if Comnum == 98:
            Comnum = Comnum - 20
        if Comnum == 100:
            break
        if Comnum < 100:
            print("Computer Square = " + str(Comnum))
        if DiceC < 6:
            break
        if DiceC == 6:
            print("Well The Computer roll again")
            sleep(2)
            system('cls')
    if Comnum == 100:
        break
    print("Your turn")
    sleep(1)
    system('cls')
if Playnum == 100:
    print("Wow you are Lucky. You Win :D")
    sleep(5)
    exit()
if Comnum == 100:
    print("Aww man you are Unlucky. The Computer Win :(")
    sleep(5)
    exit()
