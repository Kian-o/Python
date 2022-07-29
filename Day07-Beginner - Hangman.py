#######################Day 7 Project: Hangman######################
#Final thing#
import random
import hangman_words
import art

chosen_word = random.choice(hangman_words.word_list)
print(f'Pssst, the solution is {chosen_word}.')
word_length = len(chosen_word)
lives = 6
end_of_game = False

display = []
for _ in range(word_length):
    display += "_"
print(hangman_art.logo)
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
  if guess not in chosen_word:
    lives -= 1
    print(f"The letter: {guess}, is not in the word.")
    if lives == 0:
      end_of_game = True
      print("You Lose")
  print(f"{' '.join(display)}")
  print(hangman_art.stages[lives])
  if "_" not in display:
    end_of_game = True
    print("You Win!!")

#Hangman part I#
word_list = ["aardvark", "baboon", "camel"]
import random
choose_word = random.choice(word_list)

guess = input("Choose a letter: ").lower()

for letter in choose_word:
  if letter == guess:
    print("correct")
  else:
    print("wrong")

#Hangman part II#
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)

for _ in range(word_length):
  display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)

#Hangman part III#
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
word_length = len(chosen_word)
lives = 6
end_of_game = False


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose")
  print(f"{' '.join(display)}")
  print(stages[lives])
  if "_" not in display:
    end_of_game = True
    print("You Win!!")
