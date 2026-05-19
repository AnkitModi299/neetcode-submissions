class Solution:

    def encode(self, strs: List[str]) -> str:
        cat = ""
        for val in strs:
            if val != None:
                val +="/"
                cat+= val
        return cat

    def decode(self, s: str) -> List[str]:
        list1 = s.split("/")
        list1.pop()
        return list1
