from FSM import FiniteStateMachine
from MonitoredState import MonitoredState
from StateEntryDurationCondition import StateEntryDurationCondition
from ConditionalTransition import ConditionalTransition
from Transition import Transition
from StateValueCondition import StateValueCondition


class Blinker(FiniteStateMachine):
    def __init__(self, off_state_generator, on_state_generator):

        self.state_off = off_state_generator()
        self.state_on = on_state_generator()
        self.state_off_duration = off_state_generator()
        self.state_on_duration = on_state_generator()
        self.state_blink_on = on_state_generator()
        self.state_blink_off = off_state_generator()
        self.state_blink_stop_off = off_state_generator()
        self.state_blink_stop_on = on_state_generator()
        self.state_blink_begin = MonitoredState()
        self.state_blink_stop_begin = MonitoredState()
        self.state_blink_stop_end = MonitoredState()

        self.state_blink_stop_on.add_entering_action(lambda: print('on' + str(self.is_on)))
        self.state_blink_stop_off.add_entering_action(lambda: print('off' + str(self.is_off)))
        self.state_blink_begin.add_entering_action(lambda: print('blink_begin'))
        self.state_blink_stop_begin.add_entering_action(lambda: print('blink_stop_begin'))
        self.state_blink_stop_end.add_entering_action(lambda: print('stop end reached'))


        self.off_duration_condition = StateEntryDurationCondition(0, self.state_off_duration)
        self.on_duration_condition = StateEntryDurationCondition(0, self.state_on_duration)
        self.blink_off_duration_condition = StateEntryDurationCondition(0, self.state_blink_off)
        self.blink_on_duration_condition = StateEntryDurationCondition(0, self.state_blink_on)
        self.blink_begin_condition_true = StateValueCondition(True, self.state_blink_begin)
        self.blink_begin_condition_false = StateValueCondition(False, self.state_blink_begin)
        self.blink_stop_begin_condition_true = StateValueCondition(True, self.state_blink_stop_begin)
        self.blink_stop_begin_condition_false = StateValueCondition(False, self.state_blink_stop_begin)
        self.blink_stop_off_condition = StateEntryDurationCondition(0, self.state_blink_stop_off)
        self.blink_stop_on_condition = StateEntryDurationCondition(0, self.state_blink_stop_on)
        self.blink_stop_end_condition = StateEntryDurationCondition(0, self.state_blink_stop_begin)

        self.blink_stop_end_condition_false = StateValueCondition(False, self.state_blink_stop_end)
        self.blink_stop_end_condition_true = StateValueCondition(True, self.state_blink_stop_end)


        self.blink_off_duration_transition = ConditionalTransition(self.blink_off_duration_condition)
        self.blink_on_duration_transition = ConditionalTransition(self.blink_on_duration_condition)
        self.off_duration_transition = ConditionalTransition(self.off_duration_condition)
        self.on_duration_transition = ConditionalTransition(self.on_duration_condition)
        self.off_transition = Transition(self.state_off)
        self.on_transition = Transition(self.state_on)
        self.blink_begin_transition_true = ConditionalTransition(self.blink_begin_condition_true)
        self.blink_begin_transition_false = ConditionalTransition(self.blink_begin_condition_false)
        self.blink_stop_begin_transition_true = ConditionalTransition(self.blink_stop_begin_condition_true)
        self.blink_stop_begin_transition_false = ConditionalTransition(self.blink_stop_begin_condition_false)
        self.blink_stop_off_transition = ConditionalTransition(self.blink_stop_off_condition)
        self.blink_stop_on_transition = ConditionalTransition(self.blink_stop_on_condition)
        self.blink_stop_end_transition = ConditionalTransition(self.blink_stop_end_condition)

        self.blink_stop_end_transition_true = ConditionalTransition(self.blink_stop_end_condition_true)
        self.blink_stop_end_transition_false = ConditionalTransition(self.blink_stop_end_condition_false)


        self.off_duration_transition.next_state = self.state_on
        self.on_duration_transition.next_state = self.state_off
        self.blink_off_duration_transition.next_state = self.state_blink_on
        self.blink_on_duration_transition.next_state = self.state_blink_off
        self.blink_begin_transition_true.next_state = self.state_blink_on
        self.blink_begin_transition_false.next_state = self.state_blink_off
        self.blink_stop_begin_transition_true.next_state = self.state_blink_stop_on
        self.blink_stop_begin_transition_false.next_state = self.state_blink_stop_off
        self.blink_stop_off_transition.next_state = self.state_blink_stop_on
        self.blink_stop_on_transition.next_state = self.state_blink_stop_off
        self.blink_stop_end_transition.next_state = self.state_blink_stop_end

        self.blink_stop_end_transition_true.next_state = self.state_on
        self.blink_stop_end_transition_false.next_state = self.state_off


        self.state_off_duration.add_transition(self.off_duration_transition)
        self.state_on_duration.add_transition(self.on_duration_transition)
        self.state_off.add_transition(self.off_transition)
        self.state_on.add_transition(self.on_transition)
        self.state_blink_off.add_transition(self.blink_off_duration_transition)
        self.state_blink_on.add_transition(self.blink_on_duration_transition)
        self.state_blink_begin.add_transition(self.blink_begin_transition_true)
        self.state_blink_begin.add_transition(self.blink_begin_transition_false)
        self.state_blink_stop_off.add_transition(self.blink_stop_off_transition)
        self.state_blink_stop_on.add_transition(self.blink_stop_on_transition)
        self.state_blink_stop_begin.add_transition(self.blink_stop_begin_transition_true)
        self.state_blink_stop_begin.add_transition(self.blink_stop_begin_transition_false)
        self.state_blink_stop_begin.add_transition(self.blink_stop_end_transition)
        self.state_blink_stop_off.add_transition(self.blink_stop_end_transition)
        self.state_blink_stop_on.add_transition(self.blink_stop_end_transition)

        self.state_blink_stop_end.add_transition(self.blink_stop_end_transition_true)
        self.state_blink_stop_end.add_transition(self.blink_stop_end_transition_false)

        self.blinker_layout = FiniteStateMachine.Layout()
        self.blinker_layout.initial_state = self.state_off
        self.blinker_layout.add_states([self.state_off,
                                        self.state_on,
                                        self.state_off_duration,
                                        self.state_on_duration,
                                        self.state_blink_on,
                                        self.state_blink_off,
                                        self.state_blink_stop_off,
                                        self.state_blink_stop_on,
                                        self.state_blink_begin,
                                        self.state_blink_stop_begin,
                                        self.state_blink_stop_end])

        super().__init__(self.blinker_layout)


    @property
    def is_off(self) -> bool:
        if self.current_applicative_state == self.state_blink_stop_off:
            return True
        elif self.current_applicative_state == self.state_off:
            return True
        elif self.current_applicative_state == self.state_off_duration:
            return True
        elif self.current_applicative_state == self.state_blink_off:
            return True
        return False


    @property
    def is_on(self) -> bool:
        if self.current_applicative_state == self.state_on:
            return True
        elif self.current_applicative_state == self.state_on_duration:
            return True
        elif self.current_applicative_state == self.state_blink_on:
            return True
        elif self.current_applicative_state == self.state_blink_stop_on:
            return True
        return False

    def turn_off(self, **kwargs):
        if len(kwargs.keys()) == 0:
            self._transit_to(self.state_off)

        elif 'duration' in kwargs:
            if not isinstance(kwargs['duration'], float):
                raise Exception('doit etre un float')
            else:
                self.off_duration_transition.condition.duration = kwargs['duration']
                self.transit_to(self.state_off_duration)

    def turn_on(self, **kwargs):
        if len(kwargs.keys()) == 0:
            self.transit_to(self.state_on)

        elif 'duration' in kwargs:
            if not isinstance(kwargs['duration'], float):
                raise Exception('doit etre un float')
            else:
                self.on_duration_transition.condition.duration = kwargs['duration']
                self.transit_to(self.state_on_duration)

    def blink(self, begin_on: bool = True, percent_on: float = 0.5, **kwargs):
        if 'cycle_duration' in kwargs and len(kwargs.keys()) == 1:
            self.blink_on_duration_transition.condition.duration = kwargs['cycle_duration'] * percent_on
            self.blink_off_duration_transition.condition.duration = kwargs['cycle_duration'] * (1 - percent_on)
            if begin_on:
                self.state_blink_begin.custom_value = True
            else:
                self.state_blink_begin.custom_value = False
            self.transit_to(self.state_blink_begin)

        elif 'cycle_duration' in kwargs and 'total_duration' in kwargs:
            self.blink_stop_on_transition.condition.duration = kwargs['cycle_duration'] * percent_on
            self.blink_stop_off_transition.condition.duration = kwargs['cycle_duration'] * (1 - percent_on)
            self.blink_stop_end_transition.condition.duration = kwargs['total_duration']
            self.state_blink_stop_end.custom_value = not kwargs['end_off']
            if begin_on:
                self.state_blink_stop_begin.custom_value = True
            else:
                self.state_blink_stop_begin.custom_value = False
            self.transit_to(self.state_blink_stop_begin)

        elif 'total_duration' in kwargs and 'n_cycles' in kwargs:
            duration = kwargs['total_duration'] / kwargs['n_cycles']
            self.blink_stop_on_transition.condition.duration = duration * percent_on
            self.blink_stop_off_transition.condition.duration = duration * (1 - percent_on)
            self.blink_stop_end_transition.condition.duration = kwargs['total_duration']
            self.state_blink_stop_end.custom_value = not kwargs['end_off']
            if begin_on:
                self.state_blink_stop_begin.custom_value = True
            else:
                self.state_blink_stop_begin.custom_value = False
            self.transit_to(self.state_blink_stop_begin)

        elif 'cycle_duration' in kwargs and 'n_cycles' in kwargs:
            self.blink_stop_end_transition.condition.duration = kwargs['n_cycles'] * kwargs['cycle_duration']
            self.blink_stop_on_transition.condition.duration = kwargs['cycle_duration'] * percent_on
            self.blink_stop_off_transition.condition.duration = kwargs['cycle_duration'] * (1 - percent_on)
            self.state_blink_stop_end.custom_value = not kwargs['end_off']
            if begin_on:
                self.state_blink_stop_begin.custom_value = True
            else:
                self.state_blink_stop_begin.custom_value = False
            self.transit_to(self.state_blink_stop_begin)

