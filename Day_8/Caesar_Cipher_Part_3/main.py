alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amt):
    # cipher = ""
    # for letter in plain_text:
        # pos = alphabet.index(letter)
        # new_pos = (pos + shift_amt) % 26
        # print(new_pos)
        # cipher_letter = alphabet[new_pos]
        # cipher += cipher_letter
    # print(f"The encoded text is {cipher}")


# def decrypt(cypher_text, shift_amt):
    # message = ""
    # for letter in cypher_text:
        # pos = alphabet.index(letter)
        # new_pos = (pos - shift_amt) % 26
        # norm_letter = alphabet[new_pos]
        # message += norm_letter
#     print(message)


# if direction == "encode":
    # encrypt(plain_text=text, shift_amt=shift)
# elif direction == "decode":
    # decrypt(cypher_text=text, shift_amt=shift)
# elif direction != "encode" or direction != "decode":
    # print("Invalid Selection. Please type 'encode' or 'decode'")

# TODO: Combine both functions and get rid of if elif


def caesar(starting_text, shift_amt, cipher_direction):
    if cipher_direction != "encode" and cipher_direction != "decode":
        print("Invalid selection. Please type 'encode' or 'decode'")
        exit(1)
    elif cipher_direction == "decode":
        shift_amt *= -1
    end_text = ""
    for letter in starting_text:
        pos = alphabet.index(letter)
        # if cipher_direction == "encode":
            # new_pos = (pos + shift_amt) % 26
        # elif cipher_direction == "decode":
            # new_pos = (pos - shift_amt) % 26
        new_pos = (pos + shift_amt) % 26
        end_text += alphabet[new_pos]
    print(f"The {direction}d text is {end_text}")


caesar(starting_text=text, shift_amt=shift, cipher_direction=direction)
