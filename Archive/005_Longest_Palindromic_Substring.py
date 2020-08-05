class Solution:
    def longestPalindrome(self, s: str) -> str:
        """

        """
        if not s:
            return s
        result = s[0]
        tempResult = ''
        for i in range(len(s)):
            if i == len(s) - 1:
                if len(tempResult) > len(result):
                    result = tempResult
                break
            if s[i] == s[i+1]:
                tempResult = self.findPalindrome(s, i, i+1)
                if len(tempResult) > len(result):
                    result = tempResult

            if i == len(s) - 2:
                if len(tempResult) > len(result):
                    result = tempResult
                continue
            if s[i] == s[i+2]:
                tempResult = self.findPalindrome(s, i, i+2)
                if len(tempResult) > len(result):
                    result = tempResult

        return result

    def findPalindrome(self, s, i, j):

        length = 0
        while i-length > 0:
            length += 1
            try:
                if s[i-length] == s[j+length]:
                    continue
                else:
                    length -= 1
                    break
            except IndexError:
                length -= 1
                break
        return s[i-length:j+1+length]


if __name__ == "__main__":
    s = "abadd"
    test = Solution()
    print(test.longestPalindrome(s))
