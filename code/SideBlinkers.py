from FSM import FiniteStateMachine
from Blinker import Blinker
from enum import Enum, auto


class SideBlinkers:
    def __init__(self, left_off_state_generator, right_off_state_generator, left_on_state_generator, right_on_state_generator):
        super().__init__()
        self.__left_off_state_generator = left_off_state_generator
        self.__left_on_state_generator = left_on_state_generator
        self.__right_off_state_generator = right_off_state_generator
        self.__right_on_state_generator = right_on_state_generator
        self.left_blinker = Blinker(self.__left_off_state_generator, self.__left_on_state_generator)
        self.right_blinker = Blinker(self.__right_off_state_generator, self.__right_on_state_generator)

    class Side(Enum):
        LEFT = auto()
        RIGHT = auto()
        BOTH = auto()
        LEFT_RECIPROCAL = auto()
        RIGHT_RECIPROCAL = auto()

    @property
    def is_off(self, side: Side) -> bool:
        if side == SideBlinkers.Side.LEFT:
            return self.left_blinker.is_off
        elif side == SideBlinkers.Side.RIGHT:
            return self.right_blinker.is_off
        elif side == SideBlinkers.Side.BOTH:
            return self.right_blinker.is_off and self.left_blinker.is_off
        elif side == SideBlinkers.Side.LEFT_RECIPROCAL:
            return self.left_blinker.is_off and self.right_blinker.is_on
        elif side == SideBlinkers.Side.RIGHT_RECIPROCAL:
            return self.right_blinker.is_off and self.left_blinker.is_on
        else:
            raise Exception('input is not valid')

    @property
    def is_on(self, side: Side) -> bool:
        if side == SideBlinkers.Side.LEFT:
            return self.left_blinker.is_on
        elif side == SideBlinkers.Side.RIGHT:
            return self.right_blinker.is_on
        elif side == SideBlinkers.Side.BOTH:
            return self.right_blinker.is_on and self.left_blinker.is_on
        elif side == SideBlinkers.Side.LEFT_RECIPROCAL:
            return self.left_blinker.is_on and self.right_blinker.is_off
        elif side == SideBlinkers.Side.RIGHT_RECIPROCAL:
            return self.right_blinker.is_on and self.left_blinker.is_off
        else:
            raise Exception('input is not valid')

    def turn_off(self, side: Side, **kwargs):
        if side == SideBlinkers.Side.LEFT:
            self.left_blinker.turn_off(**kwargs)
        elif side == SideBlinkers.Side.RIGHT:
            self.right_blinker.turn_off(**kwargs)
        elif side == SideBlinkers.Side.BOTH:
            self.left_blinker.turn_off(**kwargs)
            self.right_blinker.turn_off(**kwargs)
        elif side == SideBlinkers.Side.LEFT_RECIPROCAL:
            self.left_blinker.turn_off(**kwargs)
            self.right_blinker.turn_on(**kwargs)
        elif side == SideBlinkers.Side.RIGHT_RECIPROCAL:
            self.left_blinker.turn_on(**kwargs)
            self.right_blinker.turn_off(**kwargs)
        else:
            raise Exception('input is not valid')

    def turn_on(self, side: Side, **kwargs):
        if side == SideBlinkers.Side.LEFT:
            self.left_blinker.turn_on(**kwargs)
        elif side == SideBlinkers.Side.RIGHT:
            self.right_blinker.turn_on(**kwargs)
        elif side == SideBlinkers.Side.BOTH:
            self.left_blinker.turn_on(**kwargs)
            self.right_blinker.turn_on(**kwargs)
        elif side == SideBlinkers.Side.LEFT_RECIPROCAL:
            self.left_blinker.turn_on(**kwargs)
            self.right_blinker.turn_off(**kwargs)
        elif side == SideBlinkers.Side.RIGHT_RECIPROCAL:
            self.left_blinker.turn_off(**kwargs)
            self.right_blinker.turn_on(**kwargs)
        else:
            raise Exception('input is not valid')

    def blink(self, side: Side, begin_on: bool = True, percent_on: float = 0.5, **kwargs):
        if side == SideBlinkers.Side.LEFT:
            self.left_blinker.blink(begin_on, percent_on, **kwargs)
        elif side == SideBlinkers.Side.RIGHT:
            self.right_blinker.blink(begin_on, percent_on, **kwargs)
        elif side == SideBlinkers.Side.BOTH:
            self.left_blinker.blink(begin_on, percent_on, **kwargs)
            self.right_blinker.blink(begin_on, percent_on, **kwargs)
        elif side == SideBlinkers.Side.LEFT_RECIPROCAL:
            self.left_blinker.blink(begin_on, percent_on, **kwargs)
            self.right_blinker.blink(not begin_on, percent_on, **kwargs)
        elif side == SideBlinkers.Side.RIGHT_RECIPROCAL:
            self.left_blinker.blink(not begin_on, percent_on, **kwargs)
            self.right_blinker.blink(begin_on, percent_on, **kwargs)
        else:
            raise Exception('input is not valid')

    def track(self):
        self.left_blinker.track()
        self.right_blinker.track()