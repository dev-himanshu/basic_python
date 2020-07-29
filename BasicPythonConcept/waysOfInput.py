# 6
# 45 85 61 33 44 74
n = int(input())
arr = [int(x) for x in input().strip().split()]
print(n)
print(arr)
del arr
print("".center(55, "-"))


# 3
# 5
# 10 20 30 40 50
# 6
# 21 22 33 44 65 49
# 4
# 44 74 26 101
n = int(input())
for _ in range(0, n):
    size = int(input())
    arr = [int(x) for x in input().strip().split()]
    print(size)
    print(arr)


# 7
# a b c d e f g
n = int(input())
arr = [x for x in input().strip().split()]
print(n)
print(arr)
print(len(arr))
print("".center(55, "-"))


# 6
# a b c d e f g h i j k l m n o p q r s t u
size = int(input())
ar = [x for x in input().strip().split()][:size]
print(size)
print(ar)
print(len(ar))
print("".center(55, "-"))


# 6
# 45 85 61 33 44 74
n = int(input())
a = list(map(int, input().strip().split()))[:n]
print(n)
print(a)


# For ---> [[10, 20, 30],  [40, 50, 60],  [70, 80, 90]]
# 3 -> size of 2-d array
# Input format :
# 1
# 2
# 3
# 4
# 5
# and so on...
listLen = int(input())
finalList = [[int(input()) for _ in range(listLen)] for _ in range(listLen)]
print(finalList)


# For ---> [[10, 20, 30],  [40, 50, 60],  [70, 80, 90]]
# 3 -> size of 2-d array
# Input format : 1 2 3 4 5 6 7 8 9
# USE numpy for this


# Take user-input in dictionary.
# Input:
# 3
# A1023 CRT
# A1029 Regulator
# A1030 Therm
n = int(input())
d = dict(input().split() for _ in range(n))
print(d)

