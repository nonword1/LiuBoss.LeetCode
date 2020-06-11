class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        num = len(T)
        result = [0]*num
        stack = []
        for i in range(num):
            while stack:
                if T[stack[-1]] < T[i]:
                    result[stack[-1]]=i-stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(i)
        return result
