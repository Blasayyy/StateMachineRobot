from Condition import Condition
from ConditionList import ConditionList


class ManyConditions(Condition):
    def __init__(self, inverse: bool = False):
        self.inverse = inverse
        self._conditions: ConditionList = [] 

    def add_condition(self, condition: Condition):
        self._conditions.append(condition)

    def add_conditions(self, conditions: ConditionList):
        for condition in conditions:
            self.add_condition(condition)
    
