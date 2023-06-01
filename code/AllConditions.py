from ManyConditions import ManyConditions


class AllConditions(ManyConditions):

    def __init__(self, inverse: bool = False):
        self.inverse = inverse


    def _compare(self) -> bool:
        pass
