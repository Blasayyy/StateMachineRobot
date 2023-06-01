from State import State
from typing import Callable

class ActionState(State):

    def __init__(self, parameter: State.Parameters()):
        super().__init__(parameter)
        self.__in_state_actions = []
        self.__exiting_actions = []
        self.__entering_actions = []

    def _do_entering_action(self):
        if self.__entering_actions:
            for action in self.__entering_actions:
                action()

    def _do_in_state_action(self):
        if self.__in_state_actions:
            for action in self.__in_state_actions:
                action()


    def _do_exiting_action(self):
        if self.__exiting_actions:
            for action in self.__exiting_actions:
                action()

    def add_entering_action(self, action: Callable):
        self.__entering_actions.append(action)

    def add_in_state_action(self, action: Callable):
        self.__in_state_actions.append(action)

    def add_exiting_action(self, action: Callable):
        self.__exiting_actions.append(action)




