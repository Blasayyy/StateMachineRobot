from FSM import FiniteStateMachine
from StateValueCondition import StateValueCondition
from ConditionalTransition import ConditionalTransition

class Manual_control(FiniteStateMachine):
    def __init__(self, robot: any, forward_state_generator, stop_state_generator, rotate_right_state_generator, backward_state_generator, rotate_left_state_generator):
        self.robot = robot

        self.state_forward = forward_state_generator()
        self.state_stop = stop_state_generator()
        self.state_rotate_right = rotate_right_state_generator()
        self.state_backwards = backward_state_generator()
        self.state_rotate_left = rotate_left_state_generator()

        self.state_forward.add_in_state_action(lambda: print("forward"))
        self.state_stop.add_in_state_action(lambda: print("stop"))
        self.state_rotate_right.add_in_state_action(lambda: print("rotate right"))
        self.state_backwards.add_in_state_action(lambda: print("backward"))
        self.state_rotate_left.add_in_state_action(lambda: print("rotate_left"))

        self.state_forward_condition = StateValueCondition("up", self.stop)
        self.state_stop_condition = StateValueCondition("ok", self.state_stop)
        self.state_rotate_right_condition = StateValueCondition("right", self.state_rotate_right)
        self.state_backwards_condition = StateValueCondition("down", self.state_backwards)
        self.state_rotate_left_condition = StateValueCondition("left", self.state_rotate_left)

        self.state_forward_transition = ConditionalTransition(self.state_forward_condition)
        self.state_stop_transition = ConditionalTransition(self.state_stop_condition)
        self.state_rotate_right_transition = ConditionalTransition(self.state_rotate_right_condition)
        self.state_backwards_transition = ConditionalTransition(self.state_backwards_condition)
        self.state_rotate_left_transition = ConditionalTransition(self.state_rotate_left_condition)

