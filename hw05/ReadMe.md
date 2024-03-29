# Homework 5
## Project
I added the TicTakToe project to the Projects document. It would be a scoreboard displayed by a website through the BeagleBone and played on LED Matrix.
## Make
I completed the exercise. `cd makefile` to get to the make files. Use `make` to create the executable.
The answers to the questions are as follows:
* 1.) Target = app.o
* 2.) Dependency = app.c
* 3.) Command = gcc
* 4.) -c says not to run the linker
* 
## Kernel Modules
### gpio_test
The first part of gpio_test can be found in the gpio_test folder. This uses a button connected to P9_15 to turn an LED connected to 
P9_16 on and off. To use it, first make it using `make` then insert the module into the kernel using `sudo insmod gpio_test.ko`. 
Once you are done, you can remove the module from the kernel using `sudo rmmod gpio_test`.

The second part of gpio_test can be found in the gpio_test2 folder. This uses two buttons, one connected to P9_15 and one connected
to P9_18, to control two LEDs, one connected to P9_12 and one connected to P9_16. To use it, first make it using `make` then insert 
the module into the kernel using `sudo insmod gpio_test.ko`. Once you are done, you can remove the module from the kernel using 
`sudo rmmod gpio_test`.

### led
This part of the assignment can be found in the led folder. This blinks two LEDs, one connected to P9_23 and one connected to P9_25
at different rates. To use it, first make it using `make` then insert the module into the kernel using `sudo insmod led.ko`. 
Once you are done, you can remove the module from the kernel using `sudo rmmod led`.

# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  0/0 | Project 
|  2/2 | Makefile
|  6/6 | Kernel Source
|  0/4 | Etch-a-Sketch
|  8/8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  0/4 | Extras - Blink at different rates
| 12/20 | **Total**
Late: -4
*My comments are in italics. --may*

