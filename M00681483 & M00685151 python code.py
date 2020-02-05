# libraries
import opc
import time
import random
import sys
import pyfirmata
from random import randint
from pyfirmata import Arduino, util

# connecting with the Simulator
client = opc.Client('localhost:7890')

# linking Arduino Uno 
arduino = pyfirmata.Arduino('COM6')
it = util.Iterator(arduino)
it.start()

# declaring analog port from arduino
a0 = arduino.get_pin('a:0:i')
a1 = arduino.get_pin('a:1:i')
a2 = arduino.get_pin('a:2:i')
a3 = arduino.get_pin('a:3:i')
#declaring powerLed as 6 because it is connected to digital pin 6
powerLed = 6

#turning on powerLed when the program starts
arduino.digital[powerLed].write(1)

# set all LED's to black on simulator
led_colour=[(0,0,0)]*360

# display on simulator
client.put_pixels(led_colour)

# define clearScreen function
def clearScreen() :
 # reset all LED's to black   
 led_colour=[(0,0,0)]*360
 client.put_pixels(led_colour)

 # define inputNumber function with message as parameter
def inputNumber(message) :
 # infinite while loop
 while True:
  # ask user for input and convert to integer
  try:
   userInput = int(input(message))
   # Exception catch(Integer)
  except ValueError:
   print("\nNot an integer! Try again.")
   continue
  else:
  # return value and exit while loop
   return userInput 
   break 

# define welcomeHelloMessage function
def welcomeHelloMessage () :
 # reset all LED's to black
 led_colour=[(0,0,0)]*360
 client.put_pixels(led_colour)

 #set individual[ 0 & 1] LED to white
 led_colour[0]= (255,255,255)
 led_colour[1]= (255,255,255)

 # display on simulator
 client.put_pixels(led_colour)

 # paused 0.05 seconds
 time.sleep(0.05)

  # set LED [60 & 61] in the array to White 
 led_colour[60]= (255,255,255)
 led_colour[61]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[120]= (255,255,255)
 led_colour[121]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[180]= (255,255,255)
 led_colour[181]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[240]= (255,255,255)
 led_colour[241]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[300]= (255,255,255)
 led_colour[301]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[122]= (255,255,255)
 led_colour[182]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[123]= (255,255,255)
 led_colour[183]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[124]= (255,255,255)
 led_colour[184]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[5]= (255,255,255)
 led_colour[6]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[65]= (255,255,255)
 led_colour[66]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[125]= (255,255,255)
 led_colour[126]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[185]= (255,255,255)
 led_colour[186]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[245]= (255,255,255)
 led_colour[246]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[305]= (255,255,255)
 led_colour[306]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[8]= (255,255,255)
 led_colour[9]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[68]= (255,255,255)
 led_colour[69]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[128]= (255,255,255)
 led_colour[129]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[188]= (255,255,255)
 led_colour[189]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[248]= (255,255,255)
 led_colour[249]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[308]= (255,255,255)
 led_colour[309]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[10]= (255,255,255)
 led_colour[11]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[12]= (255,255,255)
 led_colour[13]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[14]= (255,255,255)
 led_colour[15]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[130]= (255,255,255)
 led_colour[190]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[131]= (255,255,255)
 led_colour[191]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[132]= (255,255,255)
 led_colour[192]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[310]= (255,255,255)
 led_colour[311]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[312]= (255,255,255)
 led_colour[313]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[314]= (255,255,255)
 led_colour[315]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[17]= (255,255,255)
 led_colour[18]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[77]= (255,255,255)
 led_colour[78]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[137]= (255,255,255)
 led_colour[138]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[197]= (255,255,255)
 led_colour[198]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[257]= (255,255,255)
 led_colour[258]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[317]= (255,255,255)
 led_colour[318]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[259]= (255,255,255)
 led_colour[319]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[260]= (255,255,255)
 led_colour[320]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[261]= (255,255,255)
 led_colour[321]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[262]= (255,255,255)
 led_colour[322]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[263]= (255,255,255)
 led_colour[323]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[25]= (255,255,255)
 led_colour[26]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[85]= (255,255,255)
 led_colour[86]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[145]= (255,255,255)
 led_colour[146]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[205]= (255,255,255)
 led_colour[206]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[265]= (255,255,255)
 led_colour[266]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[325]= (255,255,255)
 led_colour[326]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[267]= (255,255,255)
 led_colour[327]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[268]= (255,255,255)
 led_colour[328]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[269]= (255,255,255)
 led_colour[329]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[270]= (255,255,255)
 led_colour[330]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[271]= (255,255,255)
 led_colour[331]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[33]= (255,255,255)
 led_colour[34]= (255,255,255)
 led_colour[35]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[93]= (255,255,255)
 led_colour[94]= (255,255,255)
 led_colour[95]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[153]= (255,255,255)
 led_colour[154]= (255,255,255)
 led_colour[155]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[213]= (255,255,255)
 led_colour[214]= (255,255,255)
 led_colour[215]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[273]= (255,255,255)
 led_colour[274]= (255,255,255)
 led_colour[275]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[333]= (255,255,255)
 led_colour[334]= (255,255,255)
 led_colour[335]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[276]= (255,255,255)
 led_colour[336]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[277]= (255,255,255)
 led_colour[337]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[278]= (255,255,255)
 led_colour[338]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[279]= (255,255,255)
 led_colour[339]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[280]= (255,255,255)
 led_colour[340]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[281]= (255,255,255)
 led_colour[341]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[219]= (255,255,255)
 led_colour[220]= (255,255,255)
 led_colour[221]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[159]= (255,255,255)
 led_colour[160]= (255,255,255)
 led_colour[161]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[99]= (255,255,255)
 led_colour[100]= (255,255,255)
 led_colour[101]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[39]= (255,255,255)
 led_colour[40]= (255,255,255)
 led_colour[41]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[38]= (255,255,255)
 led_colour[98]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[37]= (255,255,255)
 led_colour[97]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[36]= (255,255,255)
 led_colour[96]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[44]= (255,255,255)
 led_colour[45]= (255,255,255)
 led_colour[46]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05) 

 led_colour[104]= (255,255,255)
 led_colour[105]= (255,255,255)
 led_colour[106]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[284]= (255,255,255)
 led_colour[285]= (255,255,255)
 led_colour[286]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[344]= (255,255,255)
 led_colour[345]= (255,255,255)
 led_colour[346]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[48]= (255,255,255)
 led_colour[49]= (255,255,255)
 led_colour[50]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[109]= (255,255,255)
 led_colour[110]= (255,255,255)
 led_colour[111]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[170]= (255,255,255)
 led_colour[171]= (255,255,255)
 led_colour[172]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[230]= (255,255,255)
 led_colour[231]= (255,255,255)
 led_colour[232]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[289]= (255,255,255)
 led_colour[290]= (255,255,255)
 led_colour[291]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)
 
 led_colour[348]= (255,255,255)
 led_colour[349]= (255,255,255)
 led_colour[350]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[57]= (255,255,255)
 led_colour[58]= (255,255,255)
 led_colour[59]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[117]= (255,255,255)
 led_colour[118]= (255,255,255)
 led_colour[119]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[177]= (255,255,255)
 led_colour[178]= (255,255,255)
 led_colour[179]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[237]= (255,255,255)
 led_colour[238]= (255,255,255)
 led_colour[239]= (255,255,255)
 client.put_pixels(led_colour)
 time.sleep(0.05)

 led_colour[357]= (255,255,255)
 led_colour[358]= (255,255,255)
 led_colour[359]= (255,255,255)
 client.put_pixels(led_colour)

# define writeHorizontal function	
def writeHorizontal():
# reset all LED's to black and display
 led_colour=[(0,0,0)]*360
 client.put_pixels(led_colour)
 print("\n\nPrinting horizontal line ...")
 print("Choose length of line (per led)")

 # call inputNumber function and return a valid  integer length
 length = inputNumber("Length : ")
 print("Now choose starting point !")
 print("Choose horizontal ordinate (1 to 60)")

 # call inputNumber function and return a valid integer hOffset 
 hOffset = inputNumber("Horizontal ordinate : ")
 print("Choose vertical ordinate (1 to 6)")

 # call inputNumber function and return a valid integer vOffset 
 vOffset = inputNumber("Vertical ordinate : ")

 # condition in case of invalid values for length, vOffset, hOffset and array bounds
 if (((hOffset*vOffset) + length) <= 361 ) and (vOffset < 7) and (hOffset >0) and (vOffset>0):

     # for loop to add random colours to the LED's which have to be switched on
  for i in range(hOffset - 1, length + (hOffset - 1)):
   led_colour[((vOffset - 1)*60) + i] = (randint(0,256),randint(0,256),randint(0,256))
  client.put_pixels(led_colour)
 else :
  print("\nLed amount out of bounds... returning to main menu !")
  # delay 1 second
  time.sleep(1)

# define writeVertical function 
def writeVertical():
 # reset all LED's to black
 led_colour=[(0,0,0)]*360
 client.put_pixels(led_colour)
 print("\n\nPrinting vertical line ...")
 print("Choose length of line (per led)")
 length = inputNumber("Length : ")
 print("Now choose starting point !")
 print("Choose horizontal ordinate (1 to 60)")
 hOffset = inputNumber("Horizontal ordinate : ")
 print("Choose vertical ordinate (1 to 6)")
 vOffset = inputNumber("Vertical ordinate : ")
 
 # condition in case of invalid values for length, vOffset, hOffset and array bounds
 if ((vOffset + length) < 8 ) and (hOffset < 61) and (hOffset >0) and (vOffset>0):

     # for loop to add random colours to the LED's which have to be switched on
  for i in range(vOffset - 1, length + (vOffset - 1)):
   led_colour[hOffset - 1 + (i*60)] = (randint(0,256),randint(0,256),randint(0,256))
  client.put_pixels(led_colour)
 else :
  print("\nLed amount out of bounds... returning to main menu !")
  time.sleep(1)

# define potentiometerRGB function
def potentiometerRGB():

 while True :
  try :
   time.sleep(1)
   print("\nUse the potentiometers to control the colour !")
   print("Press CTRL+C to exit animation !")
 
 # call clearScreen function
   clearScreen()
   time.sleep(1)

 # for loop
   for x in range (0, 1000) :
    time.sleep(0.02)
  
  # read input ( 0-1) from analog pin 0
    red = a0.read()

  # try statement, map 0-1 into 0-255
    try:
     red = red * 255.9

   # catch statement in case of errors
    except TypeError:
     red = 0

   # round into nearest integer value
    red = int(red)

  # read input ( 0-1) from analog pin 1
    green = a1.read()

   # try statement, map 0-1 into 0-255
    try:  
     green = green * 255.9

   # catch statement in case of errors
    except TypeError:
     green = 0

   # round into nearest integer value
    green = int(green)

  # read input ( 0-1) from analog pin 2
    blue = a2.read()

  # try statement, map 0-1 into 0-255
    try:
     blue = blue * 255.9

  # catch statement in case of errors 
    except TypeError:
     blue = 0

   # round into nearest integer value
    blue = int(blue)

  #set and display on screen
    led_colour=[(red,green,blue)]*360
    client.put_pixels(led_colour)

  except KeyboardInterrupt:
   print("\nClosed !")
   break

# define soundSensorStrobe function 
def soundSensorStrobe():
 
 while True :
  try :
   print("\nRandom colour strobes will appear when a sound is detected !")  
   print("Press CTRL+C to exit animation !")
   clearScreen()

  # for loop
   for x in range (0,850) :
    time.sleep(0.02)

  # read input ( 0-1) from analog pin 3
    x = a3.read()

  # try statement, map 0-1 into 0-255
    try:
     answer = x * 255.9

   # catch statement in case of errors 
    except TypeError:
     answer = 0

  # round into nearest integer value 
    answer = int(answer)

  # display random colours to all 360 LED's if value > 30
    if answer > 30 :
     led_colour=[(randint(0,256),randint(0,256),randint(0,256))]*360
     client.put_pixels(led_colour)

   # else statement if value < 30
    elif answer < 30 :
     led_colour=[(0,0,0)]*360
     client.put_pixels(led_colour)
  except KeyboardInterrupt:
   print("\nClosed !")
   break


# define runningLights function  
def runningLights() :

 print("\nPress CTRL+C to exit animation !")
 
 while True :
  try :
    # set random values from 0 to 255
   red = randint(0,256)
   green = randint(0,256)
   blue = randint(0,256)

   # nested for loop
   for i in range (0,60) :

      # set RGB colour(randomly) to each row
    led_colour[i] = (red,green,blue)
    led_colour[i+60] = (red,green,blue)
    led_colour[i+120] = (red,green,blue)
    led_colour[i+180] = (red,green,blue)
    led_colour[i+240] = (red,green,blue)
    led_colour[i+300] = (red,green,blue)
    client.put_pixels(led_colour)

    # delay time
    time.sleep(0.01)

    # set new random values		
   red = randint(0,256)
   green = randint(0,256)
   blue = randint(0,256)

  # for loop for reversing
   for i in reversed(range(0,60)) :
       # set RGB colour(randomly) to each row
    led_colour[i] = (red,green,blue)
    led_colour[i+60] = (red,green,blue)
    led_colour[i+120] = (red,green,blue)
    led_colour[i+180] = (red,green,blue)
    led_colour[i+240] = (red,green,blue)
    led_colour[i+300] = (red,green,blue)
    client.put_pixels(led_colour)
    time.sleep(0.01)
  except KeyboardInterrupt:
   print("\nClosed !")
   break
   
#define runningLightRandom function
def runningLightsRandom() :

 print("\nPress CTRL+C to exit animation !")

 while True :
  try :
  
    # inner for loop
   for i in range (0,60) :

    # display random colours to each LED
    led_colour[i] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+60] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+120] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+180] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+240] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+300] = (randint(0,256), randint(0,256), randint(0,256))
    client.put_pixels(led_colour)
    time.sleep(0.01)

    # reverse the animation with random colours again	
   for i in reversed(range(0,60)) :
    led_colour[i] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+60] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+120] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+180] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+240] = (randint(0,256), randint(0,256), randint(0,256))
    led_colour[i+300] = (randint(0,256), randint(0,256), randint(0,256))
    client.put_pixels(led_colour)
    time.sleep(0.01)
  except KeyboardInterrupt:
   print("\nClosed !")
   break

# starting point of the program
# call welcomeHelloMessage
welcomeHelloMessage()

# while loop - main user interface
while True :
 print("\nChoose what you want to run :")
 print("1. Run HELLO again")
 print("2. A horizontal line with random colours")
 print("3. A vertical line with random colours")
 print("4. Turn off all leds")
 print("5. Change colours with potentiometers")
 print("6. Sound Reactive RGB strobes")
 print("7. Running lights")
 print("8. Running lights random colours")
 print("10. Exit the program")

 # prompt user for choice
 choice = inputNumber("Choice : ")

 # if statement depending on user choice
 if choice == 1 :
  welcomeHelloMessage()
 elif choice == 2 :
  writeHorizontal()
 elif choice == 3 :
  writeVertical()
 elif choice == 4 :
  clearScreen()
 elif choice == 5 :
  potentiometerRGB()
 elif choice == 6 :
  soundSensorStrobe()
 elif choice == 7 :
  runningLights()
 elif choice == 8 :
  runningLightsRandom()
 elif choice == 10 :
 # turn power led off when the program exits
  led_colour=[(0,0,0)]*360
  client.put_pixels(led_colour)
  arduino.digital[powerLed].write(0)
  sys.exit()
 elif (choice > 10) or (choice == 9) or (choice < 1) :
  print("\nNo option available")
