import random
from replit import clear
import art

# Functions
def dealing_cards():
  """
  A function for dealing the cards.
  """
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  chosen_card = random.choice(cards)
  return chosen_card


def calculate_score(input_list):
  """
  A function for calculating the score.
  """
  total_score = 0
  for num in input_list:
    total_score = sum(input_list)

    # check if there is a blackjack.
    if sum(input_list) == 21 and len(input_list) == 2:
      return 0

    if total_score > 21:
      if 11 in input_list:
        input_list.remove(11)
        input_list.append(1)

  return total_score


def compare_scores(user_score, computer_score):
  if computer_score == 0:
    return 'The computer has a blackjack, you lose.'
    
  elif computer_score == user_score:
    return 'You both have the same score. It\'s a draw.'

  elif user_score == 0:
    return 'You have a blackjack. You win!'

  elif user_score > 21:
    return 'Your score is above 21. You lose.'

  elif computer_score > 21:
    return 'The computer has a score above 21. You win!'

  elif user_score > computer_score:
    return 'Your score is higher than the computer score. You win!'

  else:
    return 'Your score is below the computer score. You lose.'
    
  

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False

  print(art.logo)
  
  # Adding two cards to the user
  user_cards.append(dealing_cards())
  user_cards.append(dealing_cards())
  
  # Adding one card to the computer_cards
  computer_cards.append(dealing_cards())
  computer_cards.append(dealing_cards())

  # Calculating the computer score and the user score.
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  # Print the statements to the terminal
  print(f'Your cards: {user_cards}. Current score: {user_score}.')
  print(f'Computers first card: {computer_cards[0]}')
  
  while not is_game_over and user_score <= 21:
    # Ask for another card
    get_more_cards_input = input("Type 'y' to get another card, type 'n' to pass\n") 

    if get_more_cards_input == 'n':
      is_game_over = True
    else:
      user_cards.append(dealing_cards())
      user_score = calculate_score(user_cards)
      print(f'Your cards: {user_cards}. Current score: {user_score}.')
  
  # Computer plays
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(dealing_cards())
    computer_score = calculate_score(computer_cards)
    
  print(f'The final computer score is: {computer_score} with the deck {computer_cards}')

  print(compare_scores(user_score, computer_score))

# Checks if the user would like to keep playing.
while input("\nWould you like to play a game of blackjack? Type 'y' or 'n'.\n") == 'y':
  # Remove this function if the code is not run on Replit.
  clear()
  play_game()