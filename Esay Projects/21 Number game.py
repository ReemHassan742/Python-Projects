def nearestMultiple(num):
   
    if num >= 4:
        return num + (4 - (num % 4))
    else:
        return 4

def lose():
    
    print("\n\nYOU LOST!")
    print("Better luck next time!")
    exit(0)

def check(xyz):
    
    for i in range(1, len(xyz)):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
    return True

def start1():
    xyz = []
    last = 0  
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')

        if chance == "F":
            while True:
                if last == 20:
                    lose()
                else:
                    print("\nYour Turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = int(input("> "))

                    
                    if inp > 0 and inp <= 3:
                        i = 1
                        while i <= inp:
                            xyz.append(last + i)
                            i += 1
                        print("Your inputs:", xyz[-inp:])
                        last = xyz[-1]
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose()

                    
                    if check(xyz):
                        if last == 21:
                            lose()
                        else:
                            
                            comp = 4 - inp
                            j = 1
                            while j <= comp:
                                xyz.append(last + j)
                                j += 1
                            print("Order of inputs after computer's turn is:", xyz)
                            last = xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose()

        elif chance == "S":
            comp = 1
            last = 0  
            while last < 20:
                j = 1
                while j <= comp:
                    xyz.append(last + j)
                    j += 1
                print("Order of inputs after computer's turn is:", xyz)

                if xyz[-1] == 20:
                    lose()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter?")
                    inp = int(input('> '))
                    i = 1
                    print("Enter your values")

                    while i <= inp:
                        xyz.append(int(input('> ')))
                        i += 1
                    last = xyz[-1]

                    
                    if check(xyz):
                        near = nearestMultiple(last)
                        comp = near - last

                        if comp == 4:
                            comp = 3
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose()

            print("\n\nCONGRATULATIONS!!!")
            print("YOU WON!")

        else:
            print("Wrong choice")

game = True
while game:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input('> ')

    if ans.lower() == "yes":
        start1()
    else:
        print("Do you want to quit the game? (yes / no)")
        nex = input('> ')

        if nex.lower() == 'yes':
            print("You are quitting the game...")
            exit(0)
        elif nex.lower() == "no":
            print("Continuing...")
        else:
            print("Wrong choice")

                           
                           
                    
                         
                        
                       
             



   


            