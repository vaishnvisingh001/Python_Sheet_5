A = list(map(int,input().split()))

print("Even elements:")
for i in A:
    if i % 2 == 0:
        print(i, end=" ")
print()

print("Odd elements:")
for i in A:
    if i % 2 != 0:
        print(i, end=" ")