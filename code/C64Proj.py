from Robot import Robot
from FSM import FiniteStateMachine
from MonitoredState import MonitoredState
from MonitoredState import MonitoredState
from ConditionalTransition import ConditionalTransition
from StateValueCondition import StateValueCondition
from StateEntryDurationCondition import StateEntryDurationCondition
from AlwaysTrueCondition import AlwaysTrueCondition
from RobotState import RobotState
from SideBlinkers import SideBlinkers
from Task1 import Task1
from Task2 import Task2


class C64Proj(FiniteStateMachine):

    def __init__(self):
        self.robot = Robot()
        self.c64_layout = FiniteStateMachine.Layout()

        self.remote_control_port = "AD1"
        self.remote_control = self.robot.robot.init_remote(port=self.remote_control_port)

        self.robot_instantiation_state = RobotState(self.robot)
        self.instantiation_failed_state = RobotState(self.robot)
        self.end_state = RobotState(self.robot)
        self.robot_integrity_state = RobotState(self.robot)
        self.integrity_failed_state = RobotState(self.robot)
        self.shut_down_robot_state = RobotState(self.robot)
        self.integrity_succeeded_state = RobotState(self.robot)
        self.home_state = RobotState(self.robot)

        self.task1_state = RobotState(self.robot)
        self.task2_state = RobotState(self.robot)

        self.home_state.add_entering_action(self.blink_home)
        self.home_state.add_in_state_action(self.acceuil)

        self.robot_instantiation_state.add_entering_action(lambda: print("doing entering instatiation"))
        self.instantiation_failed_state.add_in_state_action(lambda: print("Instantiation failed"))
        self.end_state.add_in_state_action(lambda: print("Bye-bye"))

        self.robot_integrity_state.add_entering_action(self.set_custom_value_integrity_state)
        self.robot_integrity_state.add_in_state_action(lambda: print("in integrity"))

        #         self.integrity_failed_state.add_in_state_action(lambda: print("robot is not an integer"))
        #         self.integrity_succeeded_state.add_in_state_action(lambda: print("robot is a go"))
        #         self.integrity_succeeded_state.add_entering_action(lambda: print("robot is soon a go"))
        self.integrity_succeeded_state.add_entering_action(self.blink_int_suc)
        self.integrity_succeeded_state.add_in_state_action(self.track_int_suc)
        self.integrity_succeeded_state.add_exiting_action(self.stop_blink_int_suc)
        self.task1_state.add_entering_action(self.task1_entering_action)
        self.task1_state.add_in_state_action(self.task1_in_state_action)
        self.task2_state.add_entering_action(self.task2_entering_action)
        self.task2_state.add_exiting_action(self.task2_exiting_action)
        self.task2_state.add_in_state_action(self.task2_in_state_action)
        self.shut_down_robot_state.add_in_state_action(lambda: print("Shutting down robot..."))

        self.robot_instantiation_succeed_condition = StateValueCondition(True, self.robot_instantiation_state)
        self.robot_instantiation_failed_condition = StateValueCondition(False, self.robot_instantiation_state)
        self.instantiation_failed_state.condition = AlwaysTrueCondition()
        self.robot_integrity_failed_condition = StateValueCondition(False, self.robot_integrity_state)
        self.robot_integrity_succeed_condition = StateValueCondition(True, self.robot_integrity_state)
        self.integrity_failed_condition = StateEntryDurationCondition(5, self.integrity_failed_state)
        self.integrity_succeed_condition = StateEntryDurationCondition(3, self.integrity_succeeded_state)
        self.shut_down_robot_condition = StateEntryDurationCondition(3, self.shut_down_robot_state)
        self.home_condition_ok = StateValueCondition("ok", self.home_state)
        self.home_condition_task1 = StateValueCondition("1", self.home_state)
        self.home_condition_task2 = StateValueCondition("2", self.home_state)
        self.task1_condition_ok = StateValueCondition("ok", self.task1_state)
        self.task2_condition_ok = StateValueCondition("ok", self.task2_state)

        self.robot_instantiation_failed_transition = ConditionalTransition(self.robot_instantiation_failed_condition)
        self.robot_instantiation_succeed_transition = ConditionalTransition(self.robot_instantiation_succeed_condition)
        self.instantiation_failed_transition = ConditionalTransition(self.integrity_failed_condition)
        self.robot_integrity_failed_transition = ConditionalTransition(self.robot_integrity_failed_condition)
        self.robot_integrity_succeed_transition = ConditionalTransition(self.robot_integrity_succeed_condition)
        self.integrity_failed_transition = ConditionalTransition(self.integrity_failed_condition)
        self.integrity_succeed_transition = ConditionalTransition(self.integrity_succeed_condition)
        self.shut_down_robot_transition = ConditionalTransition(self.shut_down_robot_condition)
        self.home_state_ok_transition = ConditionalTransition(self.home_condition_ok)
        self.home_state_task1_transition = ConditionalTransition(self.home_condition_task1)
        self.home_state_task2_transition = ConditionalTransition(self.home_condition_task2)
        self.task1_transition_ok = ConditionalTransition(self.task1_condition_ok)
        self.task2_transition_ok = ConditionalTransition(self.task2_condition_ok)

        self.robot_instantiation_failed_transition.next_state = self.instantiation_failed_state
        self.robot_instantiation_succeed_transition.next_state = self.robot_integrity_state
        self.instantiation_failed_transition.next_state = self.end_state
        self.robot_integrity_failed_transition.next_state = self.integrity_failed_state
        self.robot_integrity_succeed_transition.next_state = self.integrity_succeeded_state
        self.integrity_failed_transition.next_state = self.shut_down_robot_state
        self.integrity_succeed_transition.next_state = self.home_state
        self.shut_down_robot_transition.next_state = self.end_state
        self.home_state_ok_transition.next_state = self.shut_down_robot_state
        self.home_state_task1_transition.next_state = self.task1_state
        self.home_state_task2_transition.next_state = self.task2_state
        self.task1_transition_ok.next_state = self.home_state
        self.task2_transition_ok.next_state = self.home_state

        self.shut_down_robot_state.custom_value = "0"
        self.home_state.custom_value = "-1"
        self.task1_state.custom_value = "-1"
        self.task2_state.custom_value = "-1"

        self.robot_instantiation_state.custom_value = True
        self.robot_instantiation_state.add_transition(self.robot_instantiation_failed_transition)
        self.robot_instantiation_state.add_transition(self.robot_instantiation_succeed_transition)
        self.instantiation_failed_state.add_transition(self.instantiation_failed_transition)
        self.robot_integrity_state.add_transition(self.robot_integrity_failed_transition)
        self.robot_integrity_state.add_transition(self.robot_integrity_succeed_transition)
        self.integrity_failed_state.add_transition(self.integrity_failed_transition)
        self.shut_down_robot_state.add_transition(self.shut_down_robot_transition)
        self.integrity_succeeded_state.add_transition(self.integrity_succeed_transition)
        self.home_state.add_transition(self.home_state_ok_transition)
        self.home_state.add_transition(self.home_state_task1_transition)
        self.home_state.add_transition(self.home_state_task2_transition)
        self.task1_state.add_transition(self.task1_transition_ok)
        self.task2_state.add_transition(self.task2_transition_ok)

        self.c64_layout.add_states([self.robot_instantiation_state,
                                    self.instantiation_failed_state,
                                    self.end_state,
                                    self.robot_integrity_state,
                                    self.integrity_failed_state,
                                    self.shut_down_robot_state,
                                    self.integrity_succeeded_state,
                                    self.home_state,
                                    self.task1_state,
                                    self.task2_state])

        self.c64_layout.initial_state = self.robot_instantiation_state
        super().__init__(self.c64_layout)

    def acceuil(self):
        if self.cooldown > 0:
            self.cooldown = self.cooldown - 1
        self.robot.eyesBlinkers.track()
        key = self.remote_control.get_remote_code() if self.cooldown <= 0 else ""
        self.home_state.custom_value = key

    def set_custom_value_instatiation_state(self):
        self.robot_instantiation_state.custom_value = self.robot.is_instantiated()

    def set_custom_value_integrity_state(self):
        self.robot_integrity_state.custom_value = self.robot.is_integral()

    def blink_home(self):
        print("acceuil")
        self.robot.eyesBlinkers.blink(SideBlinkers.Side.BOTH, cycle_duration=1.5)
        self.cooldown = 2000

    def stop_blink_home(self):
        self.robot.ledBlinkers.turn_off(SideBlinkers.Side.BOTH)

    def blink_int_suc(self):
        self.robot.ledBlinkers.blink(SideBlinkers.Side.BOTH, cycle_duration=1)

    def stop_blink_int_suc(self):
        self.robot.ledBlinkers.turn_off(SideBlinkers.Side.BOTH)

    def track_int_suc(self):
        self.robot.ledBlinkers.track()

    def task1_in_state_action(self):
        self.task1.track()
        key = self.remote_control.get_remote_code()
        self.task1_state.custom_value = key

    def task1_entering_action(self):
        print("entering task 1")
        self.task1 = Task1(self.robot, self.remote_control)

    def task2_in_state_action(self):
        self.task2.track()
        key = self.remote_control.get_remote_code()
        self.task2_state.custom_value = key

    def task2_entering_action(self):
        print("entering task 2")
        self.task2 = Task2(self.robot, self.remote_control)

    def task2_exiting_action(self):
        self.robot.robot.stop()