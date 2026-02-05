# Palindrome Number (LeetCode 9)
# Approach: Math-based reversal
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        deep=x
        rev=0
        #sign = -1 if x<0 else 1 #if u have - negative sign that time we use this
        #x=x*sign
        while x>0:
            lastdigit=x%10
            x=x//10
            rev=(rev*10)+lastdigit
           
        #return 0 if -2** 31 or else 2**31-1 else sign * rev    
        if rev == deep:
            return True
        else:
            return False
              
