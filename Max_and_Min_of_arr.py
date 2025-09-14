List = list(map(int, input().split()))
maxElement = -float("inf")
for i in range(len(List)):
    if List[i] > maxElement:
        maxElement = List[i]
print("max Element is : ", maxElement)
minElement = float("inf")
for i in range(len(List)):
    if List[i] < minElement:
        minElement = List[i]
print("min Element is : ", minElement)