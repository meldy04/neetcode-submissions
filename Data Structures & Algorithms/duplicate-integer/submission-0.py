class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        dup = []

        for x in nums:
            if x not in hashset:
                hashset.add(x)
            else:
                dup.append(x)
        if dup != []:
            return True
        else:
            return False