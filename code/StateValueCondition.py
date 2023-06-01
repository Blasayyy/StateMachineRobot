from State import State
from MonitoredStateCondition import MonitoredStateCondition

class StateValueCondition(MonitoredStateCondition):

    def __init__(self, expected_value: any, monitored_state: State, inverse: bool = False):
        super().__init__(inverse)
        self.__expected_value = expected_value
        self.monitored_state = monitored_state
        

    @property
    def expected_value(self) -> any:
        return self.__expected_value

    @expected_value.setter
    def expected_value(self, expected_value: any):
        self.__expected_value = expected_value

    def _compare(self) -> bool:
        if self.monitored_state.custom_value is not None:
            if isinstance(self.__expected_value, type(self.monitored_state.custom_value)):
                return self.__expected_value == self.monitored_state.custom_value
            else:
                raise Exception("Not the same type")
        else:
            raise Exception("custom_value is None")