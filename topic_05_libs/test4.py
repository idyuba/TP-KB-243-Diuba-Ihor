
import statistics

markList = [80, 90, 100, 60, 74]

print(statistics.mean(markList))

allMark = 0
for elem in markList:
    allMark = allMark + elem

print(allMark/len(markList))
