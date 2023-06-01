from abc import abstractmethod

class Condition:
    def __init__(self, inverse: bool = False):
        self._inverse = inverse

    @abstractmethod
    def _compare(self) -> bool:
        pass

    def __bool__(self) -> bool:
        if self._inverse:
            return not self._compare()
        else:
            return self._compare()
