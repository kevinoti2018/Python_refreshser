import random

def get_choice():
    person_choice = input("enter choice ,(rock, paper,scissors): ")
    print(person_choice)
    options = ['rock','paper','scissors']
    computer_choice = random.choice(options)
    choice_dict= {"player":person_choice, "computer": computer_choice}
    return choice_dict



def check_win(player,computer):
    print(f"player choise is {player} computer choice is {computer}")
    if(player==computer):
        return "its a draw"
    elif player == "rock":
        if computer == "scissors":
            return "rock crushes scissors, you win!!"
        else:
            return "paper wraps rock, you loose"
    elif player == "paper":
        if computer == "rock":
            return "paper wraps rock, you win!!"
        else:
            return "scissors cut paper, you loose"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper, you win!!"
        else:
            return " rock crushes scissors, you loose"

choices = get_choice()
winner = check_win(choices["player"], choices["computer"])
print(winner)