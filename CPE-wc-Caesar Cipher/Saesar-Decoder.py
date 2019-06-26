#KEY for decode is 5
fileRead = open("cipher.txt","r")
key = 'abcdefghijklmnopqrstuvwxyz'
def decrypt(n, ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result

KEY = int(input("Enter KEY for decrypt: "))
decrypted = decrypt(KEY, fileRead.read())
print('Decrypted:', decrypted)
