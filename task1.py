steps = input("Enter the number of steps taken each day in the month as numbers separated by spaces: \n")

stepList = [int(x) for x in steps.split()] # 1 4 3 .....  [1,2,3,....]

print(stepList)

maxSteps = max(stepList) # 3
print("The highest number of steps is: "+str(maxSteps))

minSteps = min(stepList) #1
print("The lowest number of steps is: "+str(minSteps))

avg = sum(stepList) / len(stepList)
print("The average of daily steps is: "+str(avg))

sortedSteps = sorted(stepList,reverse=True) #4 3 1
print("Step counts in descending order: "+str(sortedSteps))