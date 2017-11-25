# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip

#setup
mode = 'encrypt' #set to encrypt or decrypt
translated = ''
message = 'GUVF VF ZL FRPERG ZRFFNTR'
message = message.upper()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #you can expand this to be any char set, see https://inventwithpython.com/caesarCipher2.py

for key in range(len(LETTERS)):
    translated = ''
    #run the encryption/decryption on each symbol in the message string
    for symbol in message:
        if symbol in LETTERS:
            #get encrypted/decrypted number for this symbol
            num = LETTERS.find(symbol)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
    #handles the wrap around in num is larger than length of LETTERS
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
    #add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]
    #add the symbol without enc/dec
        else:
            translated = translated + symbol
#display current key and its description
    print('Key #%s: %s' % (key, translated))

###Add code to allow lowercase enc/dec
##https://github.com/a0xnirudh/Exploits-and-Scripts/blob/master/Mystery%20Twister%20Solutions/Caesar%20Brute%20Force.py
