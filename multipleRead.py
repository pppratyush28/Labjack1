from labjack import ljm
import time
handle = ljm.openS("ANY", "ANY", "ANY")
info = ljm.getHandleInfo(handle)
print("Opened a LabJack with Device type: %i, Connection type: %i,\n"
      "Serial number: %i, IP address: %s, Port: %i,\nMax bytes per MB: %i" %
      (info[0], info[1], info[2], ljm.numberToIP(info[3]), info[4], info[5]))

#f = open ('sampleWr.csv','w+')
#t1=time.time()
#t2=0
#count=0
while True:#t2-t1<1 :# Setup and call eReadName to read from AIN0 on the LabJack.
      name = "AIN0"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN1"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN2"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN3"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "AIN5"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "MIO0"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "MIO1"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "MIO2"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "FIO6"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      name = "FIO7"
      result = ljm.eReadName(handle, name)
      print("\n%s reading : %f V" % (name, result))

      #t2=time.time()      
      #f.write("%f\n" %result)
      #count+=1

# Close handle
#f.close()
print(count)
ljm.close(handle)
