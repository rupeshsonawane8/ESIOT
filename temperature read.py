#Program to read the values of Temp
  
import time #import time for creating delay 
import Adafruit_CharLCD as LCD #Import LCD library 
import os #Import for file handling 
import glob #Import for global
 
 
lcd_rs        = 7  #RS of LCD is connected to GPIO 7 on PI
lcd_en        = 8  #EN of LCD is connected to GPIO 8 on PI 
lcd_d4        = 25 #D4 of LCD is connected to GPIO 25 on PI
lcd_d5        = 24 #D5 of LCD is connected to GPIO 24 on PI
lcd_d6        = 23 #D6 of LCD is connected to GPIO 23 on PI
lcd_d7        = 18 #D7 of LCD is connected to GPIO 18 on PI
lcd_backlight =  0  #LED is not connected so we assign to 0
 
lcd_columns = 16 #for 16*2 LCD
lcd_rows    = 2 #for 16*2 LCD
 
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, 
                           lcd_columns, lcd_rows, lcd_backlight)   #Send all the pin details to library 
 
lcd.message('DS18B20 with Pi \n -CircuitDigest') #Give a intro message
 
time.sleep(2) #wait for 2 secs
 
 
os.system('modprobe w1-gpio') 
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
 
def get_temp(): #Fundtion to read the value of Temperature
    file = open(device_file, 'r') #opent the file
    lines = file.readlines() #read the lines in the file 
    file.close() #close the file 
 
    trimmed_data = lines[1].find('t=') #find the "t=" in the line
 
    if trimmed_data != -1:
        temp_string = lines[1][trimmed_data+2:] #trim the strig only to the temoerature value
        temp_c = float(temp_string) / 1000.0 #divide the value of 1000 to get actual value
        return temp_c #return the value to prnt on LCD
 
    
 
while 1: #Infinite Loop
 
    lcd.clear() #Clear the LCD screen
    lcd.message ('Temp = %.1f C' % get_temp()) # Display the value of temperature
 
    time.sleep(1) #Wait for 1 sec then update the values
 