

# First of all we should always check if length og
# both strings are the same, if not return false

# Sorting
# By intuition my first solution will be sorting
# If we sord both strings than letters will appear in same order
# From this point we can iterate simalteniously both strings
# and comapre them if all match we get an anagram
# Time O(nlogn)
# Space O(1) or O(n) depends on sorting algorithm

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

# Hash maps using dict
# We can create two empty dict
# Iterate both strings as key have letter and as value have number
# of time we are seeing this letter
# In the end if dicts are equal means we get an anagram

# class Solution:
#     def isAnagra,(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return Fasle
        
#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT
        






