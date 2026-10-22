class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import math
        def arrival(position, speed):
            return (target-position)/speed
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)
        ans = []
        ans.append(arrival(cars[0][0], cars[0][1]))
        # print(arrival(cars[0][0], cars[0][1]))
        for i in range(1, len(cars)):
            arrivalnoobstacle = arrival(cars[i][0], cars[i][1])
            # print(arrivalnoobstacle)
            if arrivalnoobstacle > ans[-1]:
                ans.append(arrivalnoobstacle)
        return len(ans)
        

        