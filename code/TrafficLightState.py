from State import State
from MonitoredState import MonitoredState

class TrafficLightState(MonitoredState):

    def __init__(self, couleur: str):
        super().__init__(State.Parameters())
        self.couleur = couleur

    def _do_in_state_action(self):
        pass
        # print(self.couleur)

    def _do_entering_action(self):
        pass
        # print(self.couleur)

