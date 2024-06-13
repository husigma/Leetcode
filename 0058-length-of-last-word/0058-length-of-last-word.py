class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        last = ''
        split_string = s.split()
        for i in split_string:
            last = i

        return len(last)