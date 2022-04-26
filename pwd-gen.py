# author: ononemli

from pyfiglet import Figlet
import string
import random
import secrets
from time import sleep
import pyperclip

title = Figlet(font='threepoint')
print(title.renderText('\n'+'Password Generator'))

ononemli = Figlet(font='doom')
print(ononemli.renderText('ononemli'))

uppercaseletters = string.ascii_uppercase
lowercaseletters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

uppercaseletters1 = ''.join(random.choice(uppercaseletters) for i in range(1))
lowercaseletters1 = ''.join(random.choice(lowercaseletters) for i in range(5))
numbers1 = ''.join(random.choice(numbers) for i in range(1))
symbols1 = ''.join(random.choice(symbols) for i in range(1))
select1 = (uppercaseletters1+lowercaseletters1+numbers1+symbols1)

uppercaseletters2 = ''.join(random.choice(uppercaseletters) for i in range (2))
lowercaseletters2 = ''.join(random.choice(lowercaseletters) for i in range(6))
numbers2 = ''.join(random.choice(numbers) for i in range(1))
symbols2 = ''.join(random.choice(symbols) for i in range(1))
select2 = (uppercaseletters2+lowercaseletters2+numbers2+symbols2)

uppercaseletters3 = ''.join(random.choice(uppercaseletters) for i in range (2))
lowercaseletters3 = ''.join(random.choice(lowercaseletters) for i in range(6))
numbers3 = ''.join(random.choice(numbers) for i in range(2))
symbols3 = ''.join(random.choice(symbols) for i in range(2))
select3 = (uppercaseletters3+lowercaseletters3+numbers2+symbols3)

uppercaseletters4 = ''.join(random.choice(uppercaseletters) for i in range (2))
lowercaseletters4 = ''.join(random.choice(lowercaseletters) for i in range(6))
numbers4 = ''.join(random.choice(numbers) for i in range(4))
symbols4 = ''.join(random.choice(symbols) for i in range(4))
select4 = (uppercaseletters4+lowercaseletters4+numbers4+symbols4)

print('1 > Quick 8-character password generation and Exit'+'\n'+'2 > Quick 10-character password generation and Exit'+'\n'+'3 > Quick 12-character password generation and Exit'+'\n'+'4 > Quick 16-character password generation and Exit'+'\n'+'5 > Generation by entering password length - Uses the Random module'+'\n'+'6 > Generation by entering password length - Uses the Secrets module'+'\n'+'7 > Rot13 Encrypt/Decrypt tool -Bonus content-'+'\n'+'8 > Exit')
command = (input('\n'+'What is your choice > '))

if command == '1':
    print('\n'+'Generated password is : '+select1)
    pyperclip.copy(select1)
    print('\n'+'Copied to clipboard')
    sleep(0.2)
    print('Exited')
    exit()

elif command == '2':
    print('\n'+'Generated password is : '+select2)
    pyperclip.copy(select2)
    print('\n'+'Copied to clipboard')
    sleep(0.2)
    print('Exited')
    exit()

elif command == '3':
    print('\n'+'Generated password is : '+select3)
    pyperclip.copy(select3)
    print('\n'+'Copied to clipboard')
    sleep(0.2)
    print('Exited')
    exit()

elif command == '4':
    print('\n'+'Generated password is : '+select4)
    pyperclip.copy(select4)
    print('\n'+'Copied to clipboard')
    sleep(0.2)
    print('Exited')
    exit()

elif command == '5':
    passwordlength = int(input('\n'+'Enter a password length : '))
    passwordlength = int(passwordlength)
    select5 = ''.join(random.choice(uppercaseletters+lowercaseletters+numbers+symbols) for i in range(passwordlength))
    print('\n'+'Generated password is : '+select5)
    pyperclip.copy(select5)
    print('\n'+'Copied to clipboard')
    sleep(0.2)
    print('Exited')
    exit()

elif command == '6':
    passwordlength = int(input('\n'+'Enter a password length : '))
    passwordlength = int(passwordlength)
    select6 = ''.join(secrets.choice(uppercaseletters+lowercaseletters+numbers+symbols) for i in range(passwordlength))
    print('\n'+'Generated password is : '+select6)
    pyperclip.copy(select6)
    print('\n'+'Copied to clipboard')
    sleep(0.2)
    print('Exited')
    exit()

elif command == '7':
    select7 = input('\n'+'Enter text to encrypt/decrypt -use lowercase letters and no spaces- : ')
    rot13encryptdecrypt = ''.join([lowercaseletters[(lowercaseletters.find(x)-13)%26] for x in select7])
    print('\n'+'Your encrypted/decrypted text is : '+rot13encryptdecrypt)
    pyperclip.copy(rot13encryptdecrypt)
    print('\n'+'Copied to clipboard')
    sleep(0.2)
    print('Exited')
    exit()

elif command == '8':
    sleep(0.2)
    print('\n'+'Exited')
    exit()

elif command == '':
    print('\n'+'Incorrect entry')
    input('\n'+'Press enter to exit')
    sleep(0.2)
    print('Exited')
    if input: exit()

else:
    print('\n'+'Incorrect entry')
    input('\n'+'Press enter to exit')
    sleep(0.2)
    print('Exited')
    if input: exit()