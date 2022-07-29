import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift > 26:
  shift = shift % 26
def caesar(text_input, shift_amount, c_direction):
  new_value =""
  if c_direction == "decode":
    shift_amount *= -1
  for char in text_input:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      new_value += alphabet[new_position]
    else:
      new_value += char
  print(f"The {c_direction}d text is {new_value}")
  restart = input("Would you like to restart the cipher? Yes or No ").lower()
  if restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text_input = text, shift_amount = shift, c_direction = direction)

caesar(text_input = text, shift_amount = shift, c_direction = direction)



################################################NOTES###########################
#Caesar Cipher Part 1#
Caesar Cipher encrpyts data by shifting a letter by a predetermined number
Encrypt data by using encode [enter] "message" [enter] shift number [enter]

"encode
hellocoders
9"

Decrypt data is just as simple
use decode [enter] "encrypted message" [enter] shift number [enter]

# Functions with Inputs #
def my_function(something)
    #do this with something
    #then do this
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
greet_with_name("Angela")

# Positional vs Keyword Arguments#
# function with multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Angela", "UK") <--- Positional Argument

#Keyword
my_function(a=1, b=2, c=3)

def greet_keyword(name="Angela", location ="location"):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_keyword() <--- Keyword Argument

# Caesar Cipher Part 2: Encryption#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text, shift_number):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    shift_position = position + shift_number
    new_letter = alphabet[shift_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")
encrypt(plain_text=text, shift_number=shift)

#Caesar Cipher Part 3: Decryption#
def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decrypted text is {plain_text}")
#Combined#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decrypted text is {plain_text}")


if direction == "encode"
  encrypt(plain_text=text, shift_amount=shift)
else:
  decrypt(cipher_text=text, shift_amount=shift)




##########################################CODE CHALLENGES#####################
# Paint Area Calculator#
import math
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height + width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#Prime Number Checker#
def prime_checker(number):
  prime = 0
  if number > 1:
    for num in range(2, number):
      if number % num == 0:
        prime += 1
  if prime >= 1:
    print(f"{number} is not a prime number")
  else:
    print(f"{number} is a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)

# further refinement
import art
import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_input, shift_amount, c_direction):
  new_value =""
  for letter in text_input:
    position = alphabet.index(letter)
    if c_direction == "encode":
      new_position = position + shift_amount
    else:
      new_position = position - shift_amount
    new_value += alphabet[new_position]
  print(f"The {c_direction}d text is {new_value}")
caesar(text_input = text, shift_amount = shift, c_direction = direction)
#or#
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text_input, shift_amount, c_direction):
  new_value =""
  if c_direction == "decode":
    shift_amount *= -1
  for letter in text_input:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_value += alphabet[new_position]
  print(f"The {c_direction}d text is {new_value}")

caesar(text_input = text, shift_amount = shift, c_direction = direction)