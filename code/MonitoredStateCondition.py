from Condition import Condition
from MonitoredState import MonitoredState

class MonitoredStateCondition(Condition):

    def __init__(self, monitored_state: MonitoredState, inverse: bool = False):
        super().__init__(inverse)
        self._monitored_state = monitored_state
        

    @property
    def monitored_state(self) -> MonitoredState:
        return self._monitored_state

    @monitored_state.setter
    def monitored_state(self, monitored_state: MonitoredState):
        self._monitored_state = monitored_state
