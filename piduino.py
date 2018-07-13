#!/user/bin/env python

import serial
import os

port = "/dev/ttyUSB0"
y=0
s1= serial.Serial(port,9600,xonxoff=True)
s1.flushInput()
while True:
  if s1.inWaiting()>0:
   x = s1.read_until()
   print(x.decode('utf -8'))
   y = x
   print(y)
   if y == b'test\r\n':
     print('hello world')
     os.system('sh hello-world1.sh')
  
