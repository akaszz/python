import random
import pyperclip
import qrcode

symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

length = input("Hey, Welcome. Just say me how many characters do you want in your password? (default 10)\n")
length = 10 if length is '' else int(length)

#randomly select ascii character classes and individual characters

while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,123))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,91)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,58)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,48)
            password.append(b)
        elif r == 1:
            b = random.randint (91,97)
            password.append(b)
        elif r == 2:
            b = random.randint (123,126)
            password.append(b)
    count += 1

#convert ascii code to characters
word = "".join([chr(c) for c in password])

#copy pass to clipboard
pyperclip.copy(word)

#print the result
print ("Random password of length %s is: \n" % length)

print('*' * length)
print(word)
print('*' * length)

print ("\nIt contains",lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol_characters")
print (length,"total length")
input('Password copied to clipboard.')


val = input("do you want save password in qrcode ??--->(y/n)")

if val == "y":
    qr=qrcode.QRCode(
    version=1,
    box_size=10,
    border=5)
    data=(word)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill="black",back_color="white")
    img.save("password.png")
    print(" push a button to exit..")

else:
    exit()








    
