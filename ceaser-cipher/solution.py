from logo import logo

print(logo)
isContinue = "yes"

while isContinue == "yes":
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % len(alphabet)

    def caser_cipher(direction, text, shift):
        manipulated_text = ""
        if direction == "decode":
            shift *= -1

        for char in text:
            if char in alphabet:
                original_index = alphabet.index(char)
                shifted_index = original_index + shift

                if shifted_index >= len(alphabet):
                    shifted_index -= len(alphabet)

                manipulated_text += alphabet[shifted_index]
            else:
                manipulated_text += char
        
        if manipulated_text != "":
            print(f"The {direction}ed text is: {manipulated_text}")

    caser_cipher(direction, text, shift)

    isContinue = input("Do you want to continue (yes or no)? ")
    print("")