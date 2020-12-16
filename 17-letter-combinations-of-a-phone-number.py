class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def possibilities(u, digit):

            if len(digit) == 0:
                output.append(u)
            else:
                for element in phone[digit[0]]:
                    possibilities(u+element, digit[1:])

        output = []
        if digits:
            possibilities("", digits)
        return output
