class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        holder = ""
        strs.sort(key=len)
        for x, letter in enumerate(strs[0]):
            holder = letter
            for word in strs[1:]:
                if word[x] != holder:
                    return output
            output += holder 
        return output