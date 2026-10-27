class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maximum = 0
        stack = []
        for index, value in enumerate(heights):
            if stack:
                if stack[-1][1] < value: 
                    stack.append([index, value])
                elif stack[-1][1] > value:
                    lastIndex = stack[-1][0]
                    while stack and stack[-1][1] > value:
                        previousIndex, previousValue = stack.pop()
                        a = (index - previousIndex) * previousValue
                        if a > maximum:
                            maximum = a
                        lastIndex = previousIndex
                    stack.append([lastIndex, value])    
                else:
                    stack.append([stack[-1][0], value])
            else:
                stack.append([index, value])

        while stack:
            previousIndex, previousValue = stack.pop()
            a = (len(heights) - previousIndex) * previousValue
            if a > maximum:
                maximum = a
        return maximum
                
        

        
      

        