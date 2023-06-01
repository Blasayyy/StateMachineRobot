import imp
from Condition import Condition


class AlwaysTrueCondition(Condition):
    
    def __init__(self, inverse: bool = False):
        super().__init__(inverse)
        
        
    def compare(self) -> bool:
        return True