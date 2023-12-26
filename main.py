from art import logo
from os import system, name
from letters import alphabet

if name == 'nt':
    system("cls")
else:
    system("clear")

print(logo)
process_active = True

def crypt(message, shift_number, process_type):
    # if shift_number >= 26:
    #     shift_number %= 26

    if process_type == 'decode':
        shift_number = -shift_number
    
    new_message = []
    for letter in message:
        if letter not in alphabet:
            new_message.append(letter)
        else:
            new_message.append(alphabet[(alphabet.index(letter) + shift_number) % 26]) 
    
    return ''.join(new_message)


while process_active:
    process_type = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message = input("Type your message: ").lower()
    shift_number = int(input("Type the shift number: "))
    
    result = crypt(message, shift_number, process_type)
    print(f"Here's the {process_type}d result: {result}")
    process_active = False if input("\nType 'yes' if you want to go again, otherwise type 'no': ").lower() == 'no' else True
