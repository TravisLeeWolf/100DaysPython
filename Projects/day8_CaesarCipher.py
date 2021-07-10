# Importing logo art
import day8_CaesarCipherArt

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(plain_text, shift_amount, crypt_direction):
    text_to_crypt = ""
    if crypt_direction == "decode":
        shift_amount = -(shift_amount)
    for letter in plain_text:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        try:
            letter_index = alphabet.index(letter)
            shift_to = letter_index + shift_amount

            #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
            #Try running the program and entering a shift number of 45.
            #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
            #Hint: Think about how you can use the modulus (%).
            if shift_to > 25 or shift_to < -25:
                shift_to = shift_to % 26

            text_to_crypt += alphabet[shift_to]
        except ValueError:
            text_to_crypt += letter



    print(f"The {crypt_direction}d text is {text_to_crypt}")

#TODO-1: Import and print the logo from art.py when the program starts.
print(day8_CaesarCipherArt.logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
def start_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_amount=shift, crypt_direction=direction)

start_cipher()
keep_going = True
while keep_going == True:
    choice = input("Type 'yes' if you want to go again, otherwise type 'no'.")
    if choice == "yes":
        start_cipher()
    else:
        keep_going = False
        print("Thanks for using Caesar Cipher.")