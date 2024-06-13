class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        what= [[1], [1,1]]
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            a = [1,1]
            for i in range(rowIndex-1):
                b = []
                for i in range(len(a)-1):
                    j = i +1
                    k = a[i]+a[j]
                    b.append(k)

                b.insert(0,1)
                b.insert(len(b),1)
                what.append(b)
                a = what[-1]
            return a