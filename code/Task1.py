from FSM import FiniteStateMachine
from Robot import Robot
from RobotState import RobotState
from StateValueCondition import StateValueCondition
from ConditionalTransition import ConditionalTransition
from SideBlinkers import SideBlinkers


class Task1(FiniteStateMachine):
    def __init__(self, robot: Robot, remote_control):
        self.robot = robot
        self.task1_layout = FiniteStateMachine.Layout()
        self.remote_control = remote_control

        self.stop_state = RobotState(self.robot)
        self.forward_state = RobotState(self.robot)
        self.rotate_left_state = RobotState(self.robot)
        self.rotate_right_state = RobotState(self.robot)
        self.backwards_state = RobotState(self.robot)

        self.forward_state.add_entering_action(self.forward_entering_state_action)
        self.rotate_right_state.add_entering_action(self.right_entering_state_action)
        self.rotate_left_state.add_entering_action(self.left_entering_state_action)
        self.backwards_state.add_entering_action(self.backward_entering_state_action)

        self.stop_state.add_in_state_action(self.stop_in_state_action)
        self.forward_state.add_in_state_action(self.forward_in_state_action)
        self.rotate_left_state.add_in_state_action(self.rotate_left_in_state_action)
        self.rotate_right_state.add_in_state_action(self.rotate_right_in_state_action)
        self.backwards_state.add_in_state_action(self.backwards_in_state_action)

        self.stop_state.add_exiting_action(self.exiting_action)
        self.forward_state.add_exiting_action(self.exiting_action)
        self.rotate_left_state.add_exiting_action(self.exiting_action)
        self.rotate_right_state.add_exiting_action(self.exiting_action)
        self.backwards_state.add_exiting_action(self.exiting_action)

        self.stop_condition = StateValueCondition("", self.stop_state)
        self.stop_condition_from_forward = StateValueCondition("", self.forward_state)
        self.stop_condition_from_backwards = StateValueCondition("", self.backwards_state)
        self.stop_condition_from_right = StateValueCondition("", self.rotate_right_state)
        self.stop_condition_from_left = StateValueCondition("", self.rotate_left_state)
        self.forward_condition = StateValueCondition("up", self.stop_state)
        self.rotate_left_condition = StateValueCondition("left", self.stop_state)
        self.rotate_right_condition = StateValueCondition("right", self.stop_state)
        self.backwards_condition = StateValueCondition("down", self.stop_state)

        self.stop_transition = ConditionalTransition(self.stop_condition)
        self.stop_transition_from_forward = ConditionalTransition(self.stop_condition_from_forward)
        self.stop_transition_from_backwards = ConditionalTransition(self.stop_condition_from_backwards)
        self.stop_transition_from_right = ConditionalTransition(self.stop_condition_from_right)
        self.stop_transition_from_left = ConditionalTransition(self.stop_condition_from_left)
        self.forward_transition = ConditionalTransition(self.forward_condition)
        self.rotate_left_transition = ConditionalTransition(self.rotate_left_condition)
        self.rotate_right_transition = ConditionalTransition(self.rotate_right_condition)
        self.backwards_transition = ConditionalTransition(self.backwards_condition)

        self.stop_transition.next_state = self.stop_state
        self.stop_transition_from_forward.next_state = self.stop_state
        self.stop_transition_from_backwards.next_state = self.stop_state
        self.stop_transition_from_right.next_state = self.stop_state
        self.stop_transition_from_left.next_state = self.stop_state
        self.forward_transition.next_state = self.forward_state
        self.rotate_left_transition.next_state = self.rotate_left_state
        self.rotate_right_transition.next_state = self.rotate_right_state
        self.backwards_transition.next_state = self.backwards_state

        self.stop_state.add_transition(self.forward_transition)
        self.stop_state.add_transition(self.rotate_left_transition)
        self.stop_state.add_transition(self.rotate_right_transition)
        self.stop_state.add_transition(self.backwards_transition)

        self.forward_state.add_transition(self.stop_transition_from_forward)
        self.rotate_right_state.add_transition(self.stop_transition_from_right)
        self.rotate_left_state.add_transition(self.stop_transition_from_left)
        self.backwards_state.add_transition(self.stop_transition_from_backwards)

        self.forward_state.custom_value = ""
        self.backwards_state.custom_value = ""
        self.rotate_right_state.custom_value = ""
        self.rotate_left_state.custom_value = ""
        self.stop_state.custom_value = ""

        self.task1_layout.add_states([self.forward_state,
                                      self.rotate_right_state,
                                      self.rotate_left_state,
                                      self.backwards_state,
                                      self.stop_state])

        self.task1_layout.initial_state = self.stop_state
        super().__init__(self.task1_layout)

    def stop_in_state_action(self):
        key = self.remote_control.get_remote_code()
        self.stop_state.custom_value = key

    def forward_in_state_action(self):
        key = self.remote_control.get_remote_code()
        self.robot.ledBlinkers.track()
        self.forward_state.custom_value = key

        if key == "up":
            self.robot.robot.forward()

    def rotate_right_in_state_action(self):
        key = self.remote_control.get_remote_code()
        self.robot.ledBlinkers.track()
        self.rotate_right_state.custom_value = key

        if key == "right":
            self.robot.robot.right()

    def rotate_left_in_state_action(self):
        key = self.remote_control.get_remote_code()
        self.robot.ledBlinkers.track()
        self.rotate_left_state.custom_value = key

        if key == "left":
            self.robot.robot.left()

    def backwards_in_state_action(self):
        key = self.remote_control.get_remote_code()
        self.robot.ledBlinkers.track()
        self.backwards_state.custom_value = key
        if key == "down":
            self.robot.robot.backward()

    def forward_entering_state_action(self):
        self.robot.ledBlinkers.blink(SideBlinkers.Side.BOTH, percent_on=0.25, cycle_duration=1)

    def backward_entering_state_action(self):
        self.robot.ledBlinkers.blink(SideBlinkers.Side.BOTH, percent_on=0.75, cycle_duration=1)

    def left_entering_state_action(self):
        self.robot.ledBlinkers.blink(SideBlinkers.Side.LEFT, percent_on=0.5, cycle_duration=1)

    def right_entering_state_action(self):
        self.robot.ledBlinkers.blink(SideBlinkers.Side.RIGHT, percent_on=0.5, cycle_duration=1)

    def exiting_action(self):
        self.robot.ledBlinkers.turn_off(SideBlinkers.Side.BOTH)
        self.robot.robot.stop()

