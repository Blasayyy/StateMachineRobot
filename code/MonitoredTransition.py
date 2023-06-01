from ActionTransition import ActionTransition
from State import State

class MonitoredTransition(ActionTransition):

    def __init__(self, next_state: State = None):
        self.__transit_count: int = 0
        self.__last_transit_time: float = 0
        self.custom_value: any

    @property
    def transit_count(self) -> int:
        return self.__transit_count

    @property
    def last_transit_time(self) -> float:
        return self.__last_transit_time

    def reset_transit_count(self):
        self.__transit_count = 0

    def reset_last_transit_time(self):
        self.__last_transit_time = 0

    def _exec_transiting_action(self):
        pass