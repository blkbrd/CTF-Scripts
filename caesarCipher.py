# Caesar cipher
# http://inventwithpython.com/hacking (BSD Licensed)
import pyperclip

#setup
message = 'This is a SECRET'
key = 13
mode = 'encrypt' #set to encrypt or decrypt
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #you can expand this to be any char set, see https://inventwithpython.com/caesarCipher2.py
translated = ''
message = message.upper()

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

print(translated)
pyperclip.copy(translated) #copies the enc/dec string to the clipboard
