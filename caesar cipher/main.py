alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text1,shift1):
  cipher=""
  for i in text1:
    position=alphabet.index(i)
    new_position=position+shift
    new_letter=alphabet[new_position]
    cipher+=new_letter
  print(f"encoded text is:{cipher}")
def decrypt(text2,shift2):
  decipher=""
  for i in text2:
    position=alphabet.index(i)
    new_position=position-shift
    new_letter=alphabet[new_position]
    decipher+=new_letter
  print(f"decoded information is {decipher}")
  
if direction=="encode":
  encrypt(text1=text,shift1=shift)
else:
  decrypt(text2=text,shift2=shift)
