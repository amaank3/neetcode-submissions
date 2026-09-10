class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        num_days = len(temperatures)
        result = [0]*num_days
        stack = []

        for i in range(num_days):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result