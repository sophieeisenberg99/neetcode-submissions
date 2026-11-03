class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s): return False
        s1 = defaultdict(int)
        t1 = defaultdict(int)

        for i in range(len(s)):
            s1[s[i]] += 1
            t1[t[i]] += 1

        return s1 == t1
