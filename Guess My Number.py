import random

def repeat():
    size = random.randint(1,10)
    Chosen_num = int(input("Choose a number: "))
    while Chosen_num != size:
        if Chosen_num < 1 or Chosen_num > 10:
            print("Choose a different number this time within 1 to 10: ")
        elif Chosen_num > size:
            print("try a little smaller")
        elif Chosen_num < size:
            print("try alot bigger")
        Chosen_num = int(input("now another: "))
repeat()

again = input("You got it... play again? ")
if again == 'yes':
    repeat()
elif again == 'no':
    exit()
else:
    print('W##T TH# B#NA##S... *Error* Pl3ase R3set.....')
