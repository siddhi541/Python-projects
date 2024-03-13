import stages

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(stages.logo_caesar_cipher)

def encription(msg, key):
    print(msg)
    encoded = []
    
    for i in msg:
        if i in alphabet:
            encoded.append(alphabet[alphabet.index(i)+key])
        else:
            encoded.append(" ")
    
    print(''.join(encoded))
        


def decription(msg, key):
    print(msg)
    decoded = []
    
    for i in msg:
        if i in alphabet:
            decoded.append(alphabet[alphabet.index(i)-key])
        else:
            decoded.append(" ")
    
    print(''.join(decoded))
  

while True:

    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    
    msg = input("Type your message: ")
    key = int(input("Type shift number: "))

    if choice == "encode":
        encription(msg, key)
    elif choice == "decode":
        decription(msg, key)
    else:
        print("Invalid input!")
    ch = input("Press 'Y' to continue and 'N' to exit: ")
    if ch == 'n' or ch == 'N':
        break