from State import State
from MonitoredStateCondition import MonitoredStateCondition

class StateEntryCountCondition(MonitoredStateCondition):

    def __init__(self, expected_count: int, monitored_State: State, auto_reset: bool = True, inverse: bool = False):
        super().__init__(inverse)
        self.auto_reset = auto_reset
        self.ref_count: int
        self.expected_count = expected_count
        self.monitored_state = monitored_State

    @property
    def expected_count(self) -> int:
        return self.expected_count

    @expected_count.setter
    def expected_count(self, expected_count: int):
        self.expected_count = expected_count

    def reset_count(self):
        self.ref_count = 0
            
    def _compare(self) -> bool:
        return self.ref_count >= self.expected_count