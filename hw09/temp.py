#!/usr/bin/env python3

path = "/sys/class/hwmon/hwmon"
tmp0 = path + "0/temp1_input"
tmp1 = path + "1/temp1_input"
tmp2 = path + "2/temp1_input"
temp0 = open(tmp0, 'r')
temp1 = open(tmp1, 'r')
temp2 = open(tmp2, 'r')
# read the MAX31820 temperature data


for i in range(100):
    temp0.seek(0)
    temp1.seek(0)
    temp2.seek(0)
    try:
        Temperature0 = float(temp0.read()[:-1])/1000.0
        Temperature1 = float(temp1.read()[:-1])/1000.0
        Temperature2 = float(temp2.read()[:-1])/1000.0
        
        print("Temperature0:",Temperature0,"Temperature1:",Temperature1,"Temperature2:",Temperature2)
    except KeyboardInterrupt:
        exit()
    except:
        print("error")
        continue
