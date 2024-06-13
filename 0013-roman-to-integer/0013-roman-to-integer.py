class Solution:
    def romanToInt(self, s: str) -> int:
        encounter = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        num_total = 0
        last_number = 9999

        for i in s:
            amount = encounter[i]
            if amount > last_number:
                num_total = num_total+ amount - 2 * last_number
            else:
                num_total += amount 

            last_number = encounter[i]

        return num_total