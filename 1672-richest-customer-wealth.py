class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = float("-inf")
        for welth in accounts:
            maximum = max(sum(welth), maximum)
        return maximum
