class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if length==len(set(s[j:length+j])):
                    return length
            length-=1
        return 0