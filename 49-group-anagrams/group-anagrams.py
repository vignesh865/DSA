class Solution:
    # Complexity = n*klogk
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     anag = {}

    #     for str in strs:

    #         s_str = "".join(sorted(str))

    #         ls = anag.get(s_str, [])
    #         ls.append(str)
    #         anag[s_str] = ls

    #     return anag.values()

    # Complexity - n*k
    def hash_function(self, strr: str):

        hashe = [0] * 32

        for s in strr:
            ind = ord(s) - ord('a')
            hashe[ind] +=1

        return tuple(hashe)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = {}

        for str in strs:

            s_str = self.hash_function(str)

            ls = anag.get(s_str, [])
            ls.append(str)
            anag[s_str] = ls

        return anag.values()



