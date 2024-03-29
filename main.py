from art import logo
from alphabets import alphabet


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:

        if char.isalpha():
            position = alphabet.index(char)

            if shift_amount > 26:
                print(len(alphabet))
                shift_amount = shift_amount % 26

            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

restart_cipher = True

while restart_cipher:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    if input("Do you want to restart the cipher program? yes/no: ").lower() == "no":
        print("Thank you for using caesar cipher program!")
        restart_cipher = False
