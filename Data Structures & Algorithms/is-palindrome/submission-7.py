class Solution:
    def isPalindrome(self, s: str) -> bool:

        forwardPointer = 0
        backwardPointer = len(s) - 1

        while forwardPointer < backwardPointer:

            if not s[forwardPointer].isalnum():
                forwardPointer += 1
                continue

            if not s[backwardPointer].isalnum():
                backwardPointer -= 1
                continue

            if s[forwardPointer].lower() == s[backwardPointer].lower():
                forwardPointer += 1
                backwardPointer -= 1
            else:
                return False

        return True