import random
import hangman_words
import hangman_art

word_list = ["aardvark", "baboon", "camel"]
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
    if lives == 0:
      end_of_game = True
      print("You Lose")
  print(f"{' '.join(display)}")
  print(hangman_art.stages[lives])
  if "_" not in display:
    end_of_game = True
    print("You Win!!")