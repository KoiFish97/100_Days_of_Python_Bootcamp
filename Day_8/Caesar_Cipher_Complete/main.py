from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(starting_text, shift_amt, cipher_direction):
    if cipher_direction == "decode":
        shift_amt *= -1
    end_text = ""
    for char in starting_text:
        if char in alphabet:
            pos = alphabet.index(char)
            # if cipher_direction == "encode":
                # new_pos = (pos + shift_amt) % 26
            # elif cipher_direction == "decode":
                # new_pos = (pos - shift_amt) % 26
            new_pos = (pos + shift_amt) % 26
            end_text += alphabet[new_pos]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")


print(f"\033[35m{logo}\033[00m")

Start_Over = True
while Start_Over:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
        if direction == 'encode' or direction == 'decode':
            break
        else:
            print("Invalid selection. Please type 'encode' or 'decode'")
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Invalid Shift Input. Please type a number.")

    caesar(starting_text=text, shift_amt=shift, cipher_direction=direction)
    result = input("Would you like to use the cipher again? Type 'Yes' or 'No'\n").lower()
    if result == 'no':
        Start_Over = False
