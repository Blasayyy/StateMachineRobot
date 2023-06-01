from Condition import Condition

class ValueCondition(Condition):
    
    def __init__(self, initial_value: any, expected_value: any ,inverse: bool = False):
        super().__init__(inverse)
        self.initial_value: any = initial_value
        self.expected_value: any = expected_value
        self.value: any 
        
    def _compare(self) -> bool:
        if self.expected_value:
            if isinstance(self.expected_value, type(self.initial_value)):
                return self.expected_value == self.initial_value
        raise Exception("Pas le même type")