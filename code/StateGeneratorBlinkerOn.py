from MonitoredState import MonitoredState
from Robot import Robot

class StateGeneratorBlinkerOn:
    def __init__(self, robot : Robot):
        self.robot = robot

    def __call__(self):
        parameters = MonitoredState.Parameters()

        monitored_state = MonitoredState(parameters)


        monitored_state.add_in_state_action(lambda: self.robot.ledBlinkers.turn_on)
        # monitored_state.add_entering_action(lambda: print("on"))


        return monitored_state

