from Transition import Transition
from State import State
from MonitoredTransition import MonitoredTransition

class TrafficLightTransition(MonitoredTransition):

    def __init__(self, next_state: State):
        super().__init__(next_state)

