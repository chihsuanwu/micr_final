import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

MATRIX = [
  ["1","4","7","A"],
  ["2","5","8","0"],
  ["3","6","9","B"],
  ["C","D","E","F"]
]

ROW = [4, 17, 27, 22]
COL = [18, 23, 24, 25]

def keyboard_init():
  for item in range(4):
    GPIO.setup(COL[item], GPIO.OUT)

  for item in range(4):
    GPIO.setup(ROW[item], GPIO.IN, pull_up_down = GPIO.PUD_UP)

def get_key():
  try:
    while True:
      for item in range(4):
        GPIO.output(COL[item],0)
        for i in range(4):
          if GPIO.input(ROW[i]) == 0:

            #MATRIX[i][item] returns the value in string that has been pressed. this value can be changed by editing the strings in the matrix
            
            while GPIO.input(ROW[i]) == 0:
              pass
            print(MATRIX[i][item])
            return MATRIX[i][item]

        GPIO.output(COL[item],1)
  except KeyboardInterrupt:
    GPIO.cleanup()
 
def main():
  keyboard_init()
  try:
    while True:
      print("get:")
      print(get_key())
      time.sleep(0.2)
  except KeyboardInterrupt:
    GPIO.cleanup()
 
if __name__ == '__main__':
  main()
