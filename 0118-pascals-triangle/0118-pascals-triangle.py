class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        what= [[1], [1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        else:
            a = [1,1]
            for i in range(numRows-2):
                b = []
                for i in range(len(a)-1):
                    j = i +1
                    k = a[i]+a[j]
                    b.append(k)

                b.insert(0,1)
                b.insert(len(b),1)
                what.append(b)
                a = what[-1]
            return what