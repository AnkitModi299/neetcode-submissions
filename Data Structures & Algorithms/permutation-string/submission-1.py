class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        list1 = [0]*26
        list2 = [0]*26
        for i in range(len(s1)):
            list1[ord(s1[i]) - ord('a')]+=1
            list2[ord(s2[i]) - ord('a')]+=1
        matches = 0
        for i in range(26):
            matches+= (1 if list1[i] == list2[i] else 0) 

        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index =  ord(s2[r]) - ord('a')
            list2[index] += 1
            if list1[index] == list2[index]:
                matches += 1
            elif list1[index] + 1 == list2[index]:
                matches -= 1

            index =  ord(s2[r-len(s1)]) - ord('a')
            
            if list1[index] == list2[index]:
                matches -= 1
            list2[index] -= 1    
            if list1[index]  == list2[index]:
                matches += 1
        return matches == 26        


        