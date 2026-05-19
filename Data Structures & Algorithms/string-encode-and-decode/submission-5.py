class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs ==[]:
            return ""
        cat = "/".join(strs) + "/"
        return cat

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        list1 = s.split("/")
        return list1[:-1]
