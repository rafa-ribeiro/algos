import math


class GuessGame:
    """
    # The guess API is already defined for you.
    # @param num, your guess
    # @return -1 if num is higher than the picked number
    #          1 if num is lower than the picked number
    #          otherwise return 0
    # def guess(num: int) -> int:
    """

    def __init__(self, picked):
        self.picked = picked

    def guess(self, n: int):
        if n > self.picked:
            return -1
        elif n < self.picked:
            return 1

        return 0

    def guessNumber(self, n: int) -> int:
        def execute_guess(start: int, end: int):
            new_start, new_end = start, end
            target = math.ceil((start + end) / 2)
            result = self.guess(target)
            if result == 0:
                return target

            if result == -1:
                new_end = target - 1
            else:
                new_start = target + 1

            return execute_guess(new_start, new_end)

        return execute_guess(start=1, end=n)
