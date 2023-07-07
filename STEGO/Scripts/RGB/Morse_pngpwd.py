import sys
import string
import re
from PIL import Image

morseAlphabet = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....",
"I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.",
"S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--.."," ": "/",
"1" : ".----","2" : "..---","3" : "...--","4" : "....-","5" : ".....","6" : "-....","7" : "--...","8" : "---..",
"9" : "----.","0" : "-----",".": ".-.-.-",",": "--..--",":": "---...","?": "..--..","'": ".----.","-": "-....-",
"/": "-..-.","@": ".--.-.","=": "-...-"}

inverseMorseAlphabet = dict((v, k) for (k, v) in morseAlphabet.items())
def decodedMorse(message):
    messageSeparated = message.split(' ')
    decodedMessage = ''
    for char in messageSeparated:
        if char in inverseMorseAlphabet:
            decodedMessage += inverseMorseAlphabet[char]
        else:
            # CNF = Character not found
            decodedMessage += '<CNF>'
    print (decodedMessage)
    #print ("decodedMessage= ", decodedMessage)
    return decodedMessage

image = Image.open((sys.argv[1]))
rgb = image.convert("RGB")
width, height = image.size
binString = ""

for y in range(0, height, 1):
    binString += "\n"
    for x in range(0, width, 1): #1 is the step size in pixels; each square is 1x1 pixels
        pixel = rgb.getpixel((x,y))
        if x == 0:
            color1 = pixel
        if x > 0 and pixel != color1:
            color2 = pixel
        if pixel == color1:
            binString += "1" 

        if pixel== color2:  
            binString += "0"
        #binString value of 0 represents color1 
        #binString value of 1 repreents color2; (255,255,255)
# Formating
binString = (binString.replace("0001", "-"))
binString = (binString.replace("01", "."))
binString = re.sub('1+', ' ', binString)
binString = re.sub('\s+', ' ', binString)
binString = binString.strip()

decodedMorse(binString)
