class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        elif x == 2:
            return 1
        elif x == 0:
            return 0

        for i in range(1, x):
            if i * i == x:
                return i
            elif i * i >= x:
                return i-1
            elif i * i < x:
                continue
