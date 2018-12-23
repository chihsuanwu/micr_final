import lcd
import twstock

def main():
  lcd.lcd_init()
  while True:
    num = input('Enter stock number: ')
    stock = twstock.realtime.get(num)

    op = stock['realtime']['open']
    now = stock['realtime']["latest_trade_price"]

    a_s = float(now) - float(op)
    
    output = now + '  '
    if a_s > 0:
      output += '+'
    
    output += "%.2f"%a_s

    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string(num, 2)
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string(output, 2)



if __name__ == '__main__':
  main()
