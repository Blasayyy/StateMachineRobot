import Transition


class State():
    '''
    State est une classe qui contient un état.

    Chaque état possede ses propres paramètres qui indique s'il est dans un état
    terminal ou non, et qui détermine si une action doit être fait au début et
    à la fin de l'état.
    Chaque état possède également sa propre liste de transition. Un état est
    valide s'il possède au moins une transition et si chacune d'elle
    est valide.

    Les paramètres sont définient à l'initialisation de l'état, tandis que
    les transitions sont ajoutées par la suite.
    '''

    class Parameters:
        def __init__(self):
            self.terminal = False
            self.do_in_state_action_when_entering = False
            self.do_in_state_action_when_exiting = False

    def __init__(self, parameter: Parameters()):
        self.__parameters = parameter
        self.__transition_list = []

    def add_transition(self, transition):
        self.__transition_list.append(transition)

    def _exec_entering_action(self):
        self._do_entering_action()

    def _exec_in_state_action(self):
        self._do_in_state_action()

    def _exec_exiting_action(self):
        self._do_exiting_action()

    def _do_entering_action(self):
        pass

    def _do_in_state_action(self):
        pass

    def _do_exiting_action(self):
        pass

    @property
    def is_valid(self) -> bool:
        '''Valide si il s'agit bien d'un State'''
        return isinstance(self, State)

    @property
    def is_terminal(self) -> bool:
        '''blabla'''
        terminal = True
        return terminal

    @property
    def is_transiting(self) -> Transition:
        '''blabla'''
        for transition in self.__transition_list:
            if transition.is_transiting():
                return transition

        return None

