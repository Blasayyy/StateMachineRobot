from MonitoredState import MonitoredState


class RobotState(MonitoredState):
    def __init__(self, robot: any):
        self.robot = robot
        super().__init__()

    def _do_in_state_action(self):
        super()._do_in_state_action()
