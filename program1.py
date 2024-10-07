class Solution(object):
    def isValid(self, s):
        for i in range(len(s)):
        if s[i]=='(' and s[i+1]==')': return True
        if s[i]=='[' and s[i+1]==']': return True
        if s[i]=='{' and s[i+1]=='}': return True
        else: return False







    



  

