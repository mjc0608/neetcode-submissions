class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key = lambda x: -x[0])

        res = 1
        min_time_to_target = (target - cars[0][0]) / cars[0][1]
        for i in range(1, len(cars)):
            p = cars[i][0]
            s = cars[i][1]

            time_to_target = (target - p) / s
            if time_to_target <= min_time_to_target:
                # this one will be blocked by previous fleet
                pass
            else:
                # this one will not be blocked
                min_time_to_target = time_to_target
                res += 1
        
        return res
