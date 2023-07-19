a = list(map(int, input().split()))
b = int(input("Enter a: "))
def goodPair(lst, b):
 for i in range(0, len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == b:
            return 1
 return 0
print(goodPair([1,2,3,4], 7))
print(goodPair([1,2,4], 4))
print(goodPair([1,2,2], 4))
print(goodPair(a, b))
