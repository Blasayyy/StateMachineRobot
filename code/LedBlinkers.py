from FSM import FiniteStateMachine
from SideBlinkers import SideBlinkers
from MonitoredState import MonitoredState


class LedBlinkers(SideBlinkers):
    def __init__(self, robot):
        self.robot = robot
        super().__init__(self.off_state_generator_left_led, self.off_state_generator_right_led,
                         self.on_state_generator_left_led, self.on_state_generator_right_led)

    def off_state_generator_right_led(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_off_right)
        return state

    def on_state_generator_right_led(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_on_right)
        return state

    def off_state_generator_left_led(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_off_left)
        return state

    def on_state_generator_left_led(self):
        state = MonitoredState()
        state.add_in_state_action(self.blink_on_left)
        return state

    def blink_off_left(self):
        self.robot.blinker_off(0)

    def blink_off_right(self):
        self.robot.blinker_off(1)

    def blink_on_left(self):
        self.robot.blinker_on(0)

    def blink_on_right(self):
        self.robot.blinker_on(1)