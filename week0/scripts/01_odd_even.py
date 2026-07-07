# question - odd / even
def odd_even(n):
    return "Even" if n % 2 == 0 else "Odd"
#func to keep code more readable
print("Enter num")
n = int(input())
print(odd_even(n))
