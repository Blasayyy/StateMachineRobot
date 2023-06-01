from State import State
from ConditionalTransition import ConditionalTransition

class ActionTransition(ConditionalTransition):
    '''supsup'''

    def __init__(self, next_state: State = None):
        self.next_state = next_state
        self.__transiting_actions = []


    def _do_transiting_action(self):
        if self.__transiting_actions:
            for action in self.__in_state_actions:
                action()

    def add_transiting_action(self, action: any):
        self.__transiting_actions.append(action)