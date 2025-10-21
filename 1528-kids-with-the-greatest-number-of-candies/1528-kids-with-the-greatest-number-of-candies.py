class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        fList = [False] * len(candies)
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_candies:
                fList[i] = True

        return fList
        