from curses import flash
import imp
import re
from Condition import Condition

class TimedCondition(Condition):
    
    def __init__(self, duration: float = 1., time_reference: float = None, inverse: bool = False):
        super().__init__(inverse)
        self.duration = duration
        self.time_reference = time_reference
        self.__counter_duration: float = 0.
        self.__counter_reference: float = 0.
        
    def _compare(self) -> bool:
        pass

        
    @property
    def duration(self) -> float:
        return self.duration
        
    @duration.setter
    def duration(self, duration: float):
        self.duration = duration
        
    def reset(self):
        self.duration = 0
        self.__counter_duration = 0
        self.time_reference = 0
        self.__counter_duration = 0