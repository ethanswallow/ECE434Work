# Homework 4
## Memory Map
![mmap](mmap.JPG)

This is a memory map for the BeagleBone Black. It specifically marks the four GPIO ports and 
the starting and ending address of EMIF0 SDRAM.

## mmap
1. `switchesAndLEDs.py` reads two switches by using mmap from two different ports GPIO0 and GPIO1.
The buttons are assigned to pins P9_13 and P9_15. The LEDS are USR1 and USR3.
To run this, `chmod +x switchesAndLEDS.py` then `sudo ./switchesAndLEDs.py`.

2. To toggle the GPIO port there is a toggle program, which is `toggle.py`. It toggles pin P9_14. 
To run this, `chmod +x toggle.py` then `sudo ./toggle.py.

An oscilliscope was used to measure the frequency, which was found to be 91.1KHz.
![Oscilliscope](osci.jpg)


## Kernel Driver
`kernelDriver.sh` is a kernel driver that reads the temperature sensors. 
To run this, `chmod +x kernelDriver.sh`

## Flask and Etch-A-Sketch
This program is an Etch-A-Sketch on the LED Matrix and it is controlled by a Flask webpage.
To run this, `chmod +x hw04.py` then `./hw04.py`. The webpage will then be at `192.168.7.2:8081`



  
