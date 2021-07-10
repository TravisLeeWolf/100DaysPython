alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(plain_text, shift_amount, crypt_direction):
    text_to_crypt = ""
    for letter in plain_text:
        letter_index = alphabet.index(letter)
        if crypt_direction == "encode":
            shift_to = letter_index + shift
            if shift_to > 25:
                shift_to -= 26
        elif crypt_direction == "decode":
            shift_to = letter_index - shift
        else:
            print("An error occured.")
        text_to_crypt += alphabet[shift_to]
    print(f"The {crypt_direction}d text is {text_to_crypt}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text=text, shift_amount=shift, crypt_direction=direction)