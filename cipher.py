# this code to encript text 

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('a') if char.islower() else ord('A')
            result += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            result += char
    return result

def main():
    print("Hello")
    print("Caesar Cipher Program")
    text = input("Enter the text to be ciphered: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = caesar_cipher(text, shift)
    print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
