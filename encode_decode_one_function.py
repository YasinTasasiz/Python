alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(start_text, direction1, shift_amount):
  output_text = ""
  for letter in start_text:
    if direction1 == "encode":
      position = alphabet.index(letter)
      new_position = position + shift_amount
      output_text += alphabet[new_position]
    if direction1 == "decode":
      position = alphabet.index(letter)
      new_position = position - shift_amount
      output_text += alphabet[new_position]
  print(f"The {direction1}d text is {output_text}")
ceasar(start_text=text, direction1=direction, shift_amount=shift)