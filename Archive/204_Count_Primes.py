class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        primeCount = 0
        primeList = []
        for i in range(2, n):
            isPrime = True
            middle = int(math.sqrt(i))
            if primeList:
                for prime in primeList:
                    if i % prime == 0:
                        isPrime = False
                        break
                    if prime > middle:
                        break
            else:
                for j in range(2, int(math.sqrt(i)) + 1):
                    if i % j == 0:
                        isPrime = False
                        break
            if isPrime:
                primeCount += 1
                primeList.append(i)
        return primeCount


if __name__ == "__main__":
    test = Solution()
    print(test.countPrimes(10))
