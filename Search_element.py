a = list(map(int,input().split()))
b = int(input())
ele_found=False
for i in range(len(a)):
    if a[i] == b:
        print("Element is found at index",i)
        ele_found = True
        break
else:
    print("Element is not found")