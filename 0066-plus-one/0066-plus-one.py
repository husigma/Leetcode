class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''

        for i in range(len(digits)):
            j = str(digits[i])
            num += j

        k = str(int(num)+1)

        return [x for x in k]