import RPi.GPIO as GPIO   # Import the GPIO library.
import time               # Import time library


GPIO.setmode(GPIO.BOARD)  # Set Pi to use pin number when referencing GPIO pins.
                          # Can use GPIO.setmode(GPIO.BCM) instead to use 
                          # Broadcom SOC channel names.


GPIO.setup(32, GPIO.OUT)  # Set GPIO pin 12 to output mode.
pwm = GPIO.PWM(32, 800)   # Initialize PWM on pwmPin 100Hz frequency

GPIO.setup(29, GPIO.OUT)  ## Setup GPIO Pin 11(motor a enable) to OUT
GPIO.setup(31, GPIO.OUT)  ## Setup GPIO Pin 11(motor a enable) to OUT

GPIO.output(29, True)
GPIO.output(31, True)

# main loop of program
print("\nPress Ctl C to quit \n")  # Print blank line before and after message.
dc=0                               # set dc variable to 0 for 0%
pwm.start(dc)                      # Start PWM with 0% duty cycle
while True:                        # Loop until Ctl C is pressed to stop.
  for dc in range(20, 100, 1):      # Loop from 0 to 100 stepping dc up by 5 each loop
    pwm.ChangeDutyCycle(dc)
    #GPIO.output(32, True);
    
    time.sleep(.5)               # wait for .05 seconds at current LED brightness level
    print(dc)
  time.sleep(2)
  for dc in range(95, 0, -1):      # Loop from 95 to 5 stepping dc down by 5 each loop
    pwm.ChangeDutyCycle(dc)
    #GPIO.output(32, True)
    time.sleep(.5)               # wait for .05 seconds at current LED brightness level
    print(dc)
 
pwm.stop()
GPIO.cleanup()                     # resets GPIO ports used back to input mode

# if __name__ == '__main__':
    
