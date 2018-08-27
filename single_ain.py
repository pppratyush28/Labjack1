"""
Demonstrates reading a single analog input (AIN) from a LabJack.

"""
from labjack import ljm
import time

# Open first found LabJack
handle = ljm.openS("ANY", "ANY", "ANY")  # Any device, Any connection, Any identifier
#handle = ljm.openS("T7", "ANY", "ANY")  # T7 device, Any connection, Any identifier
#handle = ljm.openS("T4", "ANY", "ANY")  # T4 device, Any connection, Any identifier
#handle = ljm.open(ljm.constants.dtANY, ljm.constants.ctANY, "ANY")  # Any device, Any connection, Any identifier

info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

#f = open ('sampleWr3.csv','w+')
t1=time.time()
t2=0
count=0
while t2-t1<1:# Setup and call eReadName to read from AIN0 on the LabJack.
      name = "AIN0"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))
      t2=time.time()
     # f.write("%f\n" %result)
      count+=1

# Close handle
#f.close()
print(count)
ljm.close(handle)
