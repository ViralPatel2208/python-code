import statistics

print("Input set of data : ")

t = input()
a = tuple(int(x) for x in t.split())
print(a)

print(f"The mean of list value is : {statistics.mean(a)}")
print(f"The mode of list value is : {statistics.mode(a)}")
print(f"The mode of list value is : {statistics.mode(a)}")
