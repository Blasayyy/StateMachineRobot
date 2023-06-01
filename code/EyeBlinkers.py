from SideBlinkers import SideBlinkers
from MonitoredState import MonitoredState


class EyeBlinkers(SideBlinkers):
    def __init__(self, robot):
        self.robot = robot
        #         self.robot.set_eye_color((255,255,255))
        super().__init__(self.off_state_generator_left, self.off_state_generator_right, self.on_state_generator_left,
                         self.on_state_generator_right)

    def off_state_generator_right(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_off_right)
        return state

    def on_state_generator_right(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_on_right)
        return state

    def off_state_generator_left(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_off_left)
        return state

    def on_state_generator_left(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_on_left)
        return state

    def blink_off_left(self):
        self.robot.close_left_eye()

    def blink_off_right(self):
        self.robot.close_right_eye()

    def blink_on_left(self):
        self.robot.open_left_eye()

    def blink_on_right(self):
        self.robot.open_right_eye()