#import serial library
import serial
port = serial.Serial("COM3",9600)

#creating On button class

class button_func:
    def __init__(self,value):
        self.value=bytes(value, 'ascii')
    def tx(self):
        return port.write(self.value)

button1=button_func('A')
button2=button_func('a')
button3=button_func('B')
button4=button_func('b')
button5=button_func('C')
button6=button_func('c')
button7=button_func('D')
button8=button_func('d')
button9=button_func('X')
button10=button_func('x')