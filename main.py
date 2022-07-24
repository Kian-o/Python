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