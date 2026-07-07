# question: max of a list without using max()
def find_max(a):
    large = a[0]
    for i in range(1, len(a)):   # start at 1 — a[0] is already the seed
        if a[i] > large:
            large = a[i]
    return large
# split() breaks the input string on spaces → list of str; map(int, ...) converts each to int
arr = list(map(int, input("Enter nums: ").split()))
# passed a instead of arr before
print(find_max(arr))