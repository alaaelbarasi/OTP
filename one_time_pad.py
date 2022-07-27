import string

alphpet = string.ascii_lowercase
one_time_pad = list(alphpet)

def encrypt(plainText, key):
    ciphertext = ''
    for idx, char in enumerate(plainText):
        charIdx = alphpet.index(char)
        keyIdx = one_time_pad.index(key[idx])
        cipher = (keyIdx + charIdx) % len(one_time_pad)
        ciphertext += alphpet[cipher]

    return ciphertext

def decrypt(ciphertext, key):
    if ciphertext == '' or key == '':
        return ''
    charIdx = alphpet.index(ciphertext[0])
    keyIdx = one_time_pad.index(key[0])
    cipher = (charIdx - keyIdx) % len(one_time_pad)
    char = alphpet[cipher]
    return char + decrypt(ciphertext[1:], key[1:])

def main():
    key = input("Key: ")
    plainText = input("Message: ")
    cipherText=encrypt(plainText,key)
    print("Cipher text is .. ")
    print(cipherText)
    decryptedText=decrypt(cipherText,key)
    print("Plain text is .. ")
    print(decryptedText)
    

if __name__ == '__main__':
    main()
  