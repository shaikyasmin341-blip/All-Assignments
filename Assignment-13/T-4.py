#Task Description #4 – Inefficient Loop Refactoring
#Task: Refactor this inefficient loop with AI help

#Python Code
nums = [1,2,3,4,5,6,7,8,9,10]
squares = []
for i in nums:
    squares.append(i * i)
#Expected Output: AI suggested a list comprehension
squares = [i * i for i in nums]