#!/usr/bin/env python 



from time import sleep

import pifacedigitalio



# Time that the button is pressed for

BUTTON_PRESS_TIME = 0.5  # seconds



# Device pin numbers

DEVICE_1_ON = 4

DEVICE_1_OFF = 5

DEVICE_2_ON = 6

DEVICE_2_OFF = 7





def main():

    # Setup PiFace

    pifacedigitalio.init()

    piface = pifacedigitalio.PiFaceDigital()



    # switch device 1 off 

    print "Device 1 off"

    # Turns the relay on (switches device off)

    piface.output_pins[DEVICE_1_OFF].turn_on()

    sleep(BUTTON_PRESS_TIME)

    # Turns the relay off 

    piface.output_pins[DEVICE_1_OFF].turn_off()



    # Delay before we turn it on 

    sleep(1)



    # Turn device on

    print "Device 1 on"

    piface.output_pins[DEVICE_1_ON].turn_on()

    sleep(BUTTON_PRESS_TIME)

    piface.output_pins[DEVICE_1_ON].turn_off()



    # Leave device on for 5 secs 

    sleep(5)



    # Turn device back off

    print "Device 1 off" 

    piface.output_pins[DEVICE_1_OFF].turn_on()

    sleep(BUTTON_PRESS_TIME)

    piface.output_pins[DEVICE_1_OFF].turn_off()



if __name__ == "__main__":

    main()