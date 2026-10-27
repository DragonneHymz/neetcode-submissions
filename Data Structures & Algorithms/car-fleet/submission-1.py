class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p,s in zip(position, speed)]
        cars.sort(reverse=True)
        stack = [(target-cars[0][0])/cars[0][1]]
        for p,s in cars[1:]:
            ttf = (target-p)/s
            if ttf > stack[-1]:
                stack.append(ttf)
        return len(stack)

