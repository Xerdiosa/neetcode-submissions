class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivor = []
        for i in asteroids:
            if i<0 and not (len(survivor)>0 and survivor[-1]>0):
                survivor.append(i)
            elif i>0:
                survivor.append(i)
            elif i<0 and (len(survivor)>0 and survivor[-1]>0):
                iIsDestroyed = False
                while len(survivor)>0 and i*-1>=survivor[-1] and survivor[-1]>0:
                    if i*-1 == survivor[-1]:
                        survivor.pop()
                        iIsDestroyed = True
                        break
                    survivor.pop()
                if iIsDestroyed or (len(survivor)>0 and survivor[-1]>i*-1):
                    continue
                else:
                    survivor.append(i)
                    continue
        return survivor