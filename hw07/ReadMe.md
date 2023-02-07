# Homework 7

## 1-wire temperature sensors
Wired up teh Max31820 1-wire temperature sensors to P9.14 with BB-W1-P9.14-00A0.dts and can read the temperatures in /sys/class/hwmon and go into hwmon0, hwmon1, and hwmon2 and cat temp1_input to read each sensors temperature.

## systemd
Have the systemd automatically start the flask client and can run the app5.py file automatically and can access at 192.168.7.2:8081. Used flask1.service to run automatically.


# hw07 grading

| Points      | Description | | |
| ----------- | ----------- |-|-|
|  2/2  | Project Template | | https://elinux.org/ECE434_Project_-_SnakeGame
|  0/2  | | Names | *missing*
|  0/2  | | Executive Summary | *missing*
| 10/10 | Blynk - TMP101
|  4/4  | systemd auto start |
|  0    | Blynk - Etch-a-sketch - extra
| 14/20 | **Total**
Late: -2
*My comments are in italics. --may*

