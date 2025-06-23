#Minimum sum
#Given an array arr[ ] consisting of digits, your task is to form two numbers using all the digits such that their sum is minimized. Return the minimum possible sum as a string with no leading zeroes

class Solution:
    def minSum(self, arr):
        # code here
        arr.sort()
        
        num1=[]
        num2=[]
        
        for i, digit in enumerate(arr):
            if i%2==0:
                num1.append(str(digit))
            else:
                num2.append(str(digit))
                
        n1=''.join(num1)
        n2=''.join(num2)
        
        return self.addStrings(n1,n2)
        
    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            
            total = x + y + carry
            carry = total // 10
            result.append(str(total % 10))
            
            i -= 1
            j -= 1
        
        # Reverse the result because we added from least significant digit
        res_str= ''.join(result[::-1])
        # Remove Leading zeros but return '0' if all zeros
        return res_str.lstrip('0') or '0'
        
