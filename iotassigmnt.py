Import RPi.GPIO  as GPIO
from firebase import firebase
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
firebase = firebase.FirebaseApplication('https://raspiberrypi-18mca8142.firebaseio.com/', None)
result = firebase.get('/dh11', None)
while(True):
if(result[‘rl1’]==1):
GPIO.output(32,GPIO.HIGH)
else:
GPIO.output(32,GPIO.LOW)
#RL2
if(result[‘rl2’]==1):
GPIO.output(36,GPIO.HIGH)
else:
GPIO.output(36,GPIO.LOW)
#RL3
if(result[‘rl3’]==1):
GPIO.output(38,GPIO.HIGH)
else:
GPIO.output(38,GPIO.LOW)
#RL4
if(result[‘rl4’]==1):
GPIO.output(40,GPIO.HIGH)
else:
GPIO.output(40,GPIO.LOW)

