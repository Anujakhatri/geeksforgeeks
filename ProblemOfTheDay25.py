#Check if frequencies can be equal
#Given a string s consisting only lowercase alphabetic characters, check whether it is possible to remove at most one character
# such that the  frequency of each distinct character in the string becomes same. Return true if it is possible; otherwise, return false.

from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        #code here
        
        freq=Counter(s)
        freq_values=list(freq.values())
        
        freq_count=Counter(freq_values)
        
        if len(freq_count)==1:
            return True
            
        elif len(freq_count)==2:
            f1,f2=freq_count.keys()
            c1,c2=freq_count[f1], freq_count[f2]
            
            if(f1==1 and c1==1) or (f2==1 and c2==1):
                return True
                
            if (abs(f1-f2) ==1):
                if(f1>f2 and freq_count[f1]==1) or (f2>f1 and freq_count[f2]==1):
                    return True
                    
        return False            
