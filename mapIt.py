#mapIt - launches a map in the browser from commandline or clipboard
#https://automatetheboringstuff.com/chapter11/

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
  address = ' '.join(sys.argv[1:]) #gets all items on command line except the first one, which is our program name
else:
  address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
