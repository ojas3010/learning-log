# question - odd / even
def oddEven(n):
    return "Even" if n % 2 == 0 else "Odd"

#func to keep code more readable 
print("Enter num")
n = int(input())
print(oddEven(n))
