class Solution:
    def longestPalindrome(self, s: str) -> str:
        _, substring = self.testPalindrome(s, 0)
        if substring:
            return substring
        return ''

    def testPalindrome(self, s, position):
        """test if string 's' is a palindromic string or not

        :s       : the string to be tested
        :position: instruction of whether left substring and right substring
                   needed to be checked
                   0: both
                   1: no right
                   2: no left
        :returns : return whether it is a palindromic substring of the original
                   and the palindromic substring of 's'
                   0: not found
                   1: 's' is a palindromic substring
                   2: 's' contains palindromic substring but 's' is not

        """
        if len(s) == 0:
            return 0, ''
        if len(s) == 1:
            return 1, s
        if len(s) == 2:
            if s[0] == s[1]:
                return 1, s
            else:
                return 2, s[0]
        stringType = 0
        result = ''
        checkedMiddle = 0
        if s[0] == s[-1]:
            checkedMiddle == 1
            found, substring = self.testPalindrome(s[1:-1], 0)
            if found & 0b01:
                return 1, s
            elif found:
                result = substring
                stringType = found

        if position & 0b10 == 0:
            found, substring = self.testPalindrome(s[0:-1], checkedMiddle)
            if found and len(substring) > len(result):
                result = substring
                stringType = 2
        if position & 0b01 == 0:
            found, substring = self.testPalindrome(s[1:], 2)
            if found and len(substring) > len(result):
                result = substring
                stringType = 2

        return stringType, result


if __name__ == "__main__":
    # s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedica
    # tedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpa
    # teaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthat
    # thatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalarg
    # ersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravel
    # menlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoad
    # dordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcan
    # neverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheul
    # nfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherfor
    # ustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoredde
    # adwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofd
    # evotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisn
    # ationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythe
    # peopleforthepeopleshallnotperishfromtheearth"
    s = 'abaca'
    test = Solution()
    print(test.longestPalindrome(s))
