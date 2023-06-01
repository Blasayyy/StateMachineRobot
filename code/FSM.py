from abc import ABC, abstractmethod
from enum import Enum, auto
from lib2to3.pgen2.token import OP
import State
import Transition


class FiniteStateMachine:
    class Layout:
        def __init__(self):
            self.__initial_state = None
            self.__state_list = []

        @property
        def is_valid(self) -> bool:
            if not self.__state_list:
                return False
            for state in self.__state_list:
                if not state.is_valid:
                    return False
            return True

        @property
        def initial_state(self) -> State:
            return self.__initial_state

        @initial_state.setter
        def initial_state(self, state: State):
            self.__initial_state = state

        def add_state(self, state: State):
            self.__state_list.append(state)

        def add_states(self, state_list: list):
            for state in state_list:
                self.__state_list.append(state)

    class OperationalState(Enum):
        UNINITIALIZED = auto()
        IDLE = auto()
        RUNNING = auto()
        TERMINAL_REACHED = auto()

    def __init__(self, layout: Layout, initialized: bool = False):
        if not layout.is_valid:
            raise Exception("Au moins un des layout n'est pas valide")
        self.__layout = layout
        # self.__uninitialized = uninitialized
        self.__current_operational_state = None
        self.__current_applicative_state = self.__layout.initial_state

    @property
    def current_operational_state(self) -> OperationalState:
        '''blabla'''
        return self.__current_operational_state

    @property
    def current_applicative_state(self) -> State:
        '''blabla'''
        return self.__current_applicative_state

    @current_applicative_state.setter
    def current_applicative_state(self, state):
        '''blabla'''
        self.__current_applicative_state = state

    def _transit_by(self, transition: Transition):
        self.__current_applicative_state._exec_exiting_action()
        transition._exec_transiting_action()
        self.transit_to(transition.next_state)
        self.__current_applicative_state._exec_entering_action()

    def transit_to(self, state: State):
        self.current_applicative_state = state

    def track(self) -> bool:
        transition = self.current_applicative_state.is_transiting
        self.current_applicative_state._exec_in_state_action()

        if transition:
            self._transit_by(transition)


    def reset(self):
        self.__current_operational_state(FiniteStateMachine.OperationalState.IDLE)
        self.__current_applicative_state = self.__layout.initial_state

    # def run(self, reset: bool = True, time_budget: float = None):
    #     while self.__current_operational_state != FiniteStateMachine.OperationalState.TERMINAL_REACHED:
    #         self.track()

    def stop(self):
        self.__current_operational_state(self.OperationalState.IDLE)

    def start(self):
        self.__current_operational_state(self.OperationalState.RUNNING)
        while self.__current_operational_state != FiniteStateMachine.OperationalState.TERMINAL_REACHED:
            self.track()
