alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caeser(plain_text, shift_amount,direction1):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction1=="encode":
      new_position=position+shift
    elif direction1=="decode":
      new_position=position-shift
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The {direction1} text is {cipher_text}")

caeser(plain_text=text,shift_amount=shift,direction1=direction)
#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.