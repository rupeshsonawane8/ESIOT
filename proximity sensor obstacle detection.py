import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,True)

# Get data from the sensor
proximity = vcnl.read_proximity()

# If the threshold is crossed, start the alarm
if (proximity > 3000):
   GPIO.output(gpio_pin,True)
   os.system("aplay alarm_sound.wav")
   GPIO.output(gpio_pin,False)
time.sleep(0.1)