from MonitoredStateCondition import MonitoredStateCondition
from MonitoredState import MonitoredState
from time import perf_counter

class StateEntryDurationCondition(MonitoredStateCondition):

    def __init__(self, duration: float, monitored_state: MonitoredState, inverse: bool = False):
        super().__init__(monitored_state, inverse)
        self.__duration = duration

    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

    def _compare(self) -> bool:
        return self.__duration <= (perf_counter() - self._monitored_state.last_entry_time)