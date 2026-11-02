
# brute force
# we compare number to all other numbers in the array
# if we found equal number we can return true otherwise we return false
# Space O(1) for Time O(n)

# Sorting
# if we sort an array then duplicate nums will be next to each other
# and we can compare them here if we use i and j as indexes
# than j should be one index ahead of i
# Time to O(nlogn) bc of sorting algorithm
# Space O(1) 

# Hash Set
# We can use hash set to keep track of values we already seen
# hash set will give us constant time lookup
# as we iterate we will check if have seen the number already if yes
# then we found a duplicate
# Time O(n)
# Space O(n)


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

        