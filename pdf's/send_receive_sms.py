-------------------------------code to send sms to particular number----------------

#!/usr/bin/python
import serial
<span class="pl-k">from</span> curses <span class="pl-k">import</span> <span class="pl-c1">ascii
</span>import time
 
modem <span class="pl-k">=</span> serial.Serial(<span class="pl-s"><span class="pl-pds">'</span>/dev/ttyUSB1<span class="pl-pds">'</span></span>, <span class="pl-c1">460800</span>, <span class="pl-smi">timeout</span><span class="pl-k">=</span><span class="pl-c1">1</span>)
 
modem.write("AT+CMGF=1")
print modem.readline()
print modem.readline()
 
modem.write('AT+CMGS="%s"r' % "012345679")
modem.write("message text")
modem.write(<span class="pl-c1">ascii</span>.ctrl(<span class="pl-s"><span class="pl-pds">'</span>z<span class="pl-pds">'</span></span>))
time.sleep(2)
 
print modem.readlines()
