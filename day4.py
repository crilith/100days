import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
bot_pick = random.randint(0,2)
player_choice = int(input("Choose your option: Type 0 for Rock, 1 for Paper, 2 for Scissors."))

print(options[player_choice])
print(options[bot_pick])

if player_choice > 2 or player_choice < 0:
    print("Invalid choice. You lose!")
elif player_choice == bot_pick:
    print("It's a tie!")
elif bot_pick > player_choice and not (player_choice == 0 and bot_pick == 2):
    print("Bot Wins!")
else:
    print("Player Wins!")