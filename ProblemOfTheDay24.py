#Lexicographically Largest String After K Deletions
#Given a string s consisting of lowercase English letters and an integer k, your task is to remove exactly k characters from the string. The resulting string must be the largest possible in lexicographical  order, while maintain the relative order of the remaining characters.

class Solution:
    def maxSubseq(self, s, k):
        #code here
        stack=[]
        remove=k
         
        for ch in s:
            while remove>0 and stack and stack[-1]<ch:
                stack.pop()
                remove-=1
            stack.append(ch)
            
        return ''.join(stack[:len(s)-k])    
