from Transition import Transition
from Condition import Condition

class ConditionalTransition(Transition):

    def __init__(self, condition: Condition = None):
        self.__condition = condition

    @property
    def is_valid(self) -> bool:
        return self.__condition

    @property
    def condition(self) -> Condition:
        return self.__condition

    @condition.setter
    def condition(self, condition: Condition):
        self.__condition = condition

    def is_transiting(self) -> bool:
        temp = self.__condition._compare()
        return temp
