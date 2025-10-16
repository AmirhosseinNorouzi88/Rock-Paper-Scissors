from collections import Counter
import random
print("Welcome to Rock, Paper, Scissors game!")
choices_list = ["rock", "scissors", "paper"]
round = 0
situation_list = []
while True:
    round += 1
    print(f"Ok! \nCome on! \nRound {round}")
    player_choice = input(">>> ")
    computer_choice = random.choice(choices_list)
    if player_choice not in choices_list:
        print("Your choice is not correct! \nPlease write the correct choices. (Rock , Scissors , Paper)")
        situation = "Lost, Because you enter wrong input!"
    elif player_choice.lower() == computer_choice:
        print(
            f"Draw! \nYour choice is {player_choice} and computer choice is {computer_choice}.")
        situation = "Draw"
    elif player_choice.lower() == "rock" and computer_choice == "scissors":
        print(
            f"Awsome! \nYou won.\nYour choice is {player_choice} and computer choice is {computer_choice}.")
        situation = "Won"
    elif player_choice.lower() == "scissors" and computer_choice == "paper":
        print(
            f"Awsome! \nYou won.\nYour choice is {player_choice} and computer choice is {computer_choice}.")
        situation = "Won"
    elif player_choice.lower() == "paper" and computer_choice == "rock":
        print(
            f"Awsome! \nYou won.\nYour choice is {player_choice} and computer choice is {computer_choice}.")
        situation = "Won"
    else:
        print(
            f"Ohh sorry! \nYou lost.\nYour choice is {player_choice} and computer choice is {computer_choice}.")
        situation = "Lost"
    situation = situation.replace(
        "Lost, Because you enter wrong input!", "Lost")
    situation_list += [situation]
    if round == 6:
        break
    if round == 3:
        print(
            f"Ok, \nYou finished Round {round}! \nYou {situation}. \nDo you wanna play again?")
        yes_no = input(">>> ")
        if yes_no.lower() == "yes":
            print("Very well, so come on with me and let's play again! ''")
        elif yes_no.lower() == "no":
            print("Ok! \nNice to meet you! \nByeeee! ''")
            break
        else:
            print("What? \nI'm sorry but I couldn't understand what you said and I should continue \nSo let's play.")
counter = Counter(situation_list)
most_common_word, count = counter.most_common(1)[0]
print(
    f"The game finished and you {most_common_word}. Thank you for playing this game. \nGood Bye and Have a Nice Day My Friend!")
if most_common_word.lower() == "lost":
    print("And remember, It's not matter that you lost, Because you can come back and defeat me whenever you want but if you can! \nNow Good Bye My Friend.")
elif most_common_word.lower() == "won":
    print("OMG! you were very good competitor, I'll be happy whenever you come back and competit with me. \nGood Bye My Friend.")
else:
    print("Ohhh! I was near to lose but It didn't happen! I wish you come back to lose! \nGood Bye My friend.")
print(f"You : {round - count} , Computer : {count}")
