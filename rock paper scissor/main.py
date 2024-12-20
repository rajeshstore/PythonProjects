from random import choice

values=["rock","paper","scissor"]

c=choice(values)

run=True

while run:
    print("\tOption \n1.rock\n\n2.paper\n\n3.scissor")
    try:
        n=input("\nEnter a Choice : ").lower()
    except ValueError:
        print("nInvaild Choice")

    print("\nYour Gues     : "+n)
    print("\nComputer Gues : "+c)

    if(n=="paper" and c=="rock") or (n=="scissor" and c=="paper") or (n=="rock" and c=="scissor"):
        print("\nYou Won")
    elif(c=="paper" and n=="rock") or (c=="scissor" and n=="paper") or (c=="rock" and n=="scissor"):
        print("\nComputer Won")
    elif n==c:
        print("\nDraw Match")
    else:
        print("\nInvaild Choice")
        break
    
    option=0
    try:
        option=int(input("\nDo You Want To Play Click 1 To Play Otherwise 0 : "))
    except ValueError:
        print("\nInvaild Choice")

    if option !=1:
        if option!=0:
            print("\nYour Click ",option,"Button So Game Exit")
        print("\nThanks For Coming")
        run=False




    