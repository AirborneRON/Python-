from microbit import *

uart.write("Ready\n")
while(True):
    if(uart.any()):
        input = uart.read(1)
        next_character = chr(input[0])
        print("You just sent: " + next_character)
        
        if (next_character == "N"):
            display.show(Image.HAPPY)
            display.show(Image.RABBIT)
        #else: display.clear()              #what its suppose to do
        
        #if (next_character == "F"):
            #display.show(Image.RABBIT)
        #else: display.clear()
        