import lcd
import twstock
import time
import keyboard as kb
import RPi.GPIO as GPIO
import threading

stopper = 0

def mov_print(str):
  counter = 0
  str_len = len(str)
  while stopper == 1:
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(str[counter:str_len]+str[0:counter], 2)
    counter += 1
    if counter == str_len:
      counter = 0
    time.sleep(0.2)

def main():
  global stopper
    
  lcd.lcd_init()
  kb.keyboard_init()
  try:
    while True:

      num = ''
      lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
      lcd.lcd_string('Enter Stock Num:', 2)
      while True:
        print("get:")
        key = kb.get_key()
        time.sleep(0.3)
        if key == 'A':
          print('A')
        elif key == 'B':
          num = num[:len(num) - 1]
          print('Back, Cur num : ' + num)
          lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
          lcd.lcd_string(num, 2)
        elif key == 'C':
          num = ''
          print('Clear, Cur num : ' + num)
          lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
          lcd.lcd_string(num, 2)
        elif key == 'D':
          print('D')
        elif key == 'E' or key == 'F':
          print('Searching : ' + num)
          lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
          lcd.lcd_string(num, 2)
          lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
          lcd.lcd_string('Searching...', 2)
          break
        else:
          num += key
          print('Cur num : ' + num)
          lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
          lcd.lcd_string(num, 2)
          
      stock = twstock.realtime.get(num)
      
      if not stock['success']:
        lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
        lcd.lcd_string('Stock Not Found', 2)
        continue
    
      stock_his = twstock.Stock(num)
      print(stock)
      yes = stock_his.price[-2:][0]

      op = stock['realtime']['open']
      now = stock['realtime']["latest_trade_price"]
      high = stock['realtime']['high']
      low = stock['realtime']['low']

      a_s = float(now) - float(yes)
    
      output = now + '  '
      if a_s > 0:
        output += '+'
    
      output += "%.2f"%a_s

      lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
      lcd.lcd_string(num, 2)
      lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
      lcd.lcd_string(output, 2)
      
      while True:
        print("get:")
        key = kb.get_key()
        time.sleep(0.3)
        if key == 'E' or key == 'F':
          stopper = 0
          lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
          lcd.lcd_string('', 2)
          break
        elif key == 'A':
          stopper = 0
          lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
          lcd.lcd_string(output, 2)
        elif key == 'B':
          if stopper == 1:
            stopper = 0
            t.join()
          stopper = 1
          s = ' open: ' + op + ' high: ' + high + ' low: ' + low
          t = threading.Thread(target = mov_print, args = [s])
          t.start()
        elif key == 'C':
          if stopper == 1:
            stopper = 0
            t.join()
          stopper = 1
          s = ' '.join(str(x) for x in stock_his.price[-5:]) + '     '
          t = threading.Thread(target = mov_print, args = [s])
          t.start()
    
  except KeyboardInterrupt:
    GPIO.cleanup()



if __name__ == '__main__':
  main()
