class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        for i in t:
            if i in s_list:
                s_list.remove(i)
            else:
                return False
        return len(s_list) == 0