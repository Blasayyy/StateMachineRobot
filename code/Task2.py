from FSM import FiniteStateMachine
from Robot import Robot
from RobotState import RobotState
from StateValueCondition import StateValueCondition
from ConditionalTransition import ConditionalTransition
from SideBlinkers import SideBlinkers


class Task2(FiniteStateMachine):
    def __init__(self, robot: Robot, remote_control):
        self.robot = robot
        self.task2_layout = FiniteStateMachine.Layout()
        self.remote_control = remote_control

        self.stop_state = RobotState(self.robot)
        self.forward_state = RobotState(self.robot)

        self.forward_state.add_entering_action(self.forward_entering_state_action)

        self.stop_state.add_in_state_action(self.stop_in_state_action)
        self.forward_state.add_in_state_action(self.forward_in_state_action)

        self.stop_state.add_exiting_action(self.exiting_action)
        self.forward_state.add_exiting_action(self.exiting_action)

        self.stop_condition = StateValueCondition(300, self.stop_state)
        self.forward_condition = StateValueCondition(50, self.forward_state)

        self.stop_transition = ConditionalTransition(self.stop_condition)
        self.forward_transition = ConditionalTransition(self.forward_condition)

        self.stop_transition.next_state = self.forward_state
        self.forward_transition.next_state = self.stop_state

        self.stop_state.add_transition(self.stop_transition)
        self.forward_state.add_transition(self.forward_transition)

        self.forward_state.custom_value = 0
        self.stop_state.custom_value = 0

        self.task2_layout.add_states([self.forward_state,
                                      self.stop_state])

        self.task2_layout.initial_state = self.forward_state
        super().__init__(self.task2_layout)

    def stop_in_state_action(self):
        self.stop_state.custom_value = self.robot.sensor.read()
        if self.stop_state.custom_value > 60:  # car précision du sensor est pauvre
            self.stop_state.custom_value = 300
        print("stop")

    def forward_in_state_action(self):
        self.robot.ledBlinkers.track()
        self.robot.robot.forward()
        self.forward_state.custom_value = self.robot.sensor.read()

        if 60 > self.forward_state.custom_value:  # car précision du sensor est pauvre
            self.forward_state.custom_value = 50
        print("go")

    def forward_entering_state_action(self):
        self.robot.ledBlinkers.blink(SideBlinkers.Side.BOTH, percent_on=0.25, cycle_duration=1)

    def exiting_action(self):
        self.robot.ledBlinkers.turn_off(SideBlinkers.Side.BOTH)
        self.robot.robot.stop()
