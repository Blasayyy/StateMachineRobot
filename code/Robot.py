from LedBlinkers import LedBlinkers
from EyeBlinkers import EyeBlinkers
from MonitoredState import MonitoredState
from GoPiGo import GoPiGo
import easygopigo3 as gpg

class Robot():
    def __init__(self):
        self.robot = gpg.EasyGoPiGo3()
        self.ledBlinkers = LedBlinkers(self.robot)
        self.eyesBlinkers = EyeBlinkers(self.robot)
        sensor_port = 'I2C'
        self.sensor = self.robot.init_distance_sensor(sensor_port)


    def track_all(self):
        self.ledBlinkers.left_blinker.track()
        self.ledBlinkers.right_blinker.track()
        self.eyesBlinkers.left_blinker.track()
        self.eyesBlinkers.right_blinker.track()

    def is_instantiated(self):
        if not self.robot:
            return False
        else:
            return True

    def is_integral(self):
        return True

    def initialize_all_components(self):
        self.led = self.robot.init_led(port='AD2')








