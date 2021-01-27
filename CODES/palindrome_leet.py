class Solution:
    def strrev(self, x):
        return x[::-1]

    def isPalindrome(self, x: int) -> bool:

        x = str(x)

        y = self.strrev(x)

        if x == y:
            return "true"
