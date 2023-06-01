from FSM import FiniteStateMachine
from State import State
from Transition import Transition
from TrafficLightState import TrafficLightState
from TrafficLightTransition import TrafficLightTransition
from MonitoredState import MonitoredState
from StateEntryDurationCondition import StateEntryDurationCondition
from ConditionalTransition import ConditionalTransition


class TrafficLightFSM(FiniteStateMachine):

    def __init__(self):
        monitored_red_state = MonitoredState()
        monitored_yellow_state = MonitoredState()
        monitored_green_state = MonitoredState()

        monitored_red_state.add_entering_action(lambda: print('red'))
        monitored_yellow_state.add_entering_action(lambda: print('yellow'))
        monitored_green_state.add_entering_action(lambda: print('green'))

        red_state_condition = StateEntryDurationCondition(3.0, monitored_red_state)
        yellow_state_condition = StateEntryDurationCondition(3.0, monitored_yellow_state)
        green_state_condition = StateEntryDurationCondition(3.0, monitored_green_state)

        red_transition = ConditionalTransition(red_state_condition)
        yellow_transition = ConditionalTransition(yellow_state_condition)
        green_transition = ConditionalTransition(green_state_condition)

        red_transition.next_state = monitored_green_state
        yellow_transition.next_state = monitored_red_state
        green_transition.next_state = monitored_yellow_state

        monitored_red_state.add_transition(red_transition)
        monitored_yellow_state.add_transition(yellow_transition)
        monitored_green_state.add_transition(green_transition)

        traffic_layout = FiniteStateMachine.Layout()
        traffic_layout.initial_state = monitored_red_state
        traffic_layout.add_states([monitored_yellow_state, monitored_green_state])

        super().__init__(traffic_layout)
