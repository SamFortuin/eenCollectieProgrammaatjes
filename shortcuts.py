#print slow from sabastion on stackoverflow, good lad
from string import ascii_lowercase
from serial import Serial, SerialException
from time import sleep
from sys import stdout
from os import system

class color:
   PURPLE= '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

coloredText = lambda uncoloredIn, colorSelect, coloredIn: uncoloredIn+colorSelect+coloredIn+color.END

def comScan(checkRange,bluetooth=False,debugMode=False): #checks all open ports, returns the first one found
    bluetoothPorts = [3,4] #*change if your bluetooth ports are different
    debug,output = [],[] #empty lists
    for i in range(checkRange):
        if i+1 in bluetoothPorts and bluetooth:
            pass
        else:
            port = f'COM{i+1}'
            try:
                serial_port = Serial(port=port, baudrate=115200, timeout=1)
            except SerialException as e:
                debug.append("could not open serial port '{}': {}".format(port, e))
            else:
                output.append(port)
                debug.append("serial port {port} is open and not busy.")
                serial_port.close()

    if debugMode:
        print(*debug,sep='\n') #use if debug is True
    if len(output) > 0:
        return output[0] #returns first available port
    else:
        print("Could not find any COM ports")
        exit() #exits because code falls apart if there is no COM port.
        #scorched earth type beat. kinda. not really.


def slowPrint(str):
    for letter in str:
        stdout.write(letter)
        stdout.flush()
        sleep(0.04)
   
#clears screen after given time
# def clearScreen(sleepTime):
#     sleep(sleepTime)
#     system("cls")

clearScreen = lambda sleeptime: sleep(sleeptime); system('cls')

def intConvert(num):
    Check1 = False
    Check2 = True
    for i in range(10):
        if str(i) in num:
            Check1 = True
    for x in ascii_lowercase:
        if x in num.lower():
            Check2 = False
    if Check1 and Check2:
        return int(num)
    else:
        return num