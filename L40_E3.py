import random
import string

def encryption(a):
    encrypted_string=""

    if len(a)<=3:
        for i in a:
            encrypted_string=i+encrypted_string
    else:
        encrypted_string = a[1:]
        encrypted_string = encrypted_string + a[0]
        for i in range(3):
            encrypted_string = random.choice(string.ascii_letters) + encrypted_string + random.choice(string.ascii_letters)
    return encrypted_string

def decryption(a):
    decrypted_string=""
    if len(a)<=3:
        for i in a:
            decrypted_string = i+decrypted_string
    else:
        decrypted_string = a[3:-3]
        decrypted_string = decrypted_string[-1] + decrypted_string[0:-1]
    return decrypted_string

a=input("Enter the String to be Encrypted: ")
b=encryption(a)
print(f"This is Encrypted string {b}")
print(f"This is Decrypted string {decryption(b)}")


#Decryption

# print(random.choice(string.ascii_letters))