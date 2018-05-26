from picar import front_wheels, back_wheels
import picar
from time import sleep
import cv2
from pyzbar.pyzbar import decode

picar.setup()



class CarController:
    def __init__(self):
        self.fw = front_wheels.Front_Wheels()
        self.bw = back_wheels.Back_Wheels()
        self.speed = 30

    def moveForward(self, t=0):
        """
        move the car forward, then stop
        """
        self.turnStraight()
        time.sleep(0.5)
        self.bw.forward()
        self.bw.speed = self.speed
        # make the car run for t second
        if t>0:
            time.sleep(t)
        self.bw.stop()
     
    def moveBackward(self, t=0):
        """
        move the car backward, then stop
        """
        self.turnStraight()
        time.sleep(0.5)
        self.bw.backward()
        self.bw.speed = self.speed
        # make the car run for t seconds
        if t>0: 
            time.sleep(t)
        self.bw.stop()

    def turnLeft(self, angle=0):
        """
        turn front wheel to the left
        """
        self.fw.turn_left(angle)
        time.sleep(0.5)
    
    def turnRight(self, angle=0):
        """
        turn front wheel to the right
        """
        self.fw.turn_right(angle)
        time.sleep(0.5)

    def destroy():
        self.bw.stop()

if __name__ == '__main__':
    cc = CarController()
    try:
        main()
    except KeyboardInterrupt:
        destroy()