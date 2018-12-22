import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

MATRIX = [
  ["1","2","3","A"],
  ["4","5","6","B"],
  ["7","8","9","C"],
  ["*","0","#","D"]
]

ROW = [7,11,13,15]
COL = [12,16,18,22]

for item in range(4):
  GPIO.setup(COL[item], GPIO.OUT)

for item in range(4):
  GPIO.setup(ROW[item], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
  while True:
    for item in range(4):
      GPIO.output(COL[item],0)
      for i in range(4):
        if GPIO.input(ROW[i]):

          #MATRIX[i][item] returns the value in string that has been pressed. this value can be changed by editing the strings in the matrix
          print(MATRIX[i][item])

      GPIO.output(COL[item],1)
except KeyboardInterrupt:
  GPIO.cleanup()
 
