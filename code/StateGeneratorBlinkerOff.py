from MonitoredState import MonitoredState
from Robot import Robot

class StateGeneratorBlinkerOff:
    def __init__(self, robot : Robot):
        self.robot = robot

    def __call__(self):
        parameters = MonitoredState.Parameters()

        monitored_state = MonitoredState(parameters)

        # monitored_state.add_entering_action(lambda: self.robot.ledBlinkers.turn_off)
        monitored_state.add_entering_action(lambda: print("off"))

        return monitored_state

