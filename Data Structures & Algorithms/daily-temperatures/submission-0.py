class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                # no longer a decreasing seq
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    j = stack.pop()
                    res[j] = i - j
                stack.append(i)

        return res