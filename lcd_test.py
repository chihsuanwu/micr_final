
import lcd
import RPi.GPIO as GPIO
import time
#lcd.main()
lcd.lcd_init()
# Turn off backlight
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
lcd.lcd_string("Raspberry Pi", 2)
lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
lcd.lcd_string("Model B+", 2)
lcd.GPIO.cleanup()
