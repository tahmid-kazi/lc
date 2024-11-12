class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # 11/12/24) Tue) 528-543pm) tk)
        stack1 = []
        for j in asteroids:
            #if its negative then its a collision
            while stack1 and j < 0 and stack1[-1] > 0: 
                if abs(j) > stack1[-1]:
                    stack1.pop()
                elif abs(j) == stack1[-1]:
                    stack1.pop()
                    break
                else:
                    break
            else:
                stack1.append(j)
        return stack1 
