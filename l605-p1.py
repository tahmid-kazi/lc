class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 11/21/24) thurs) 427-429pm, 440-443pm) tk)
        counter = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1 #place a flower
                counter += 1
                if counter >= n:
                    return True
        return counter >= n
        