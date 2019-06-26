fileRead = open("Message.txt","r")
fileWrite = open("cipher.txt","w+")
key = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(n, plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

KEY = int(input("Enter KEY for encrypt: "))
encrypted = encrypt(KEY,fileRead.read())
print('Message is Encrypted:', encrypted)
fileWrite.write(encrypted) 
fileWrite.close() 
fileRead.close()
