from ActionState import ActionState
from time import perf_counter

class MonitoredState(ActionState):
    '''yoyo'''

    def __init__(self, parameter: ActionState.Parameters = ActionState.Parameters()):
        super().__init__(parameter)
        self.__counter_last_entry: float = 0
        self.__counter_last_exit: float = 0
        self.__entry_count: int = 0
        self.custom_value: any = 0


    @property
    def entry_count(self) -> int:
        return self.__entry_count

    @property
    def last_entry_time(self) -> float:
        return self.__counter_last_entry

    @property
    def last_exit_time(self) -> float:
        return self.__counter_last_exit

    def reset_entry_count(self):
        self.entry_count = 0

    def reset_last_times(self):
        self.last_entry_time = 0
        self.last_exit_time = 0

    def _exec_entering_action(self):
        self.__counter_last_entry = perf_counter()
        super()._do_entering_action()

    def _exec_exiting_action(self):
        self.__counter_last_exit = perf_counter()
        super()._do_exiting_action()


