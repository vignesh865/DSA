class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st_s = dict()
        st_t = {}

        for si in s:
            st_s[si] = st_s.get(si, 0) + 1

        for ti in t:
            st_t[ti] = st_t.get(ti, 0) + 1

        for ti in st_t:
            if st_t.get(ti) != st_s.get(ti):
                return False

        for si in st_s:
            if st_t.get(si) != st_s.get(si):
                return False
        return True
