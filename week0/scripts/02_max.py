#question: max of a list without using max
def maximum(a):
    large = a[0]
    for i in range(len(a)):
        if a[i] > large:
            large = a[i]
    return large

# i have no idea how split and map works im used to array in c java 
arr = list(map(int, input("Enter nums:").split()))
# passed a instead of arr before
print(maximum(arr))
