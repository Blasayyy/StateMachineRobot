from abc import ABC, abstractmethod
import State


class Transition:
    def __init__(self, next_state: State = None):
        self.__next_state = next_state

    @property
    def is_valid(self):
        '''
        Détermine la validité de la transition.
        '''
        return self.__next_state and type(self.__next_state) == State

    # STATE
    @property
    def next_state(self):
        '''Retourne le prochain state'''
        return self.__next_state

    @next_state.setter
    def next_state(self, state):
        """Defini un nouveau state pour la transition"""
        if state.is_valid:
            self.__next_state = state

    # TRANSITION
    @abstractmethod
    def is_transiting(self) -> bool:
        pass

    def _exec_transiting_action(self):
        self._do_transiting_action()

    def _do_transiting_action(self):
        pass
