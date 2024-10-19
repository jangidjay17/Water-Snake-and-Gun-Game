import random

game_dict = {1:"SNAKE", -1:"WATER", 0:"GUN"}

computer = random.choice([1,-1,0])

print("Please Enter your input \n 1 for snake \n -1 for water \n 0 for gun")
you = int(input())

print(f"you chose:{game_dict[you]}")
print(f'computer chose: {game_dict[computer]}')

if(computer==1 and you == -1):
    print("you lose")
elif(computer==1 and you==0):
    print("you win")
elif(computer == 1 and you==1):
    print("It's a tie")
elif(computer == -1 and you==1):
    print("you win")
elif(computer == -1 and you== 0):
    print("you lose")
elif(computer == -1 and you == -1):
    print("It's a tie")
elif(computer == 0 and you== 0):
    print("It's a tie")
elif(computer ==0 and you == 1):
    print("you lose")
elif(computer == 0 and you == -1):
    print("you win")
else:
    print("there is an error")

