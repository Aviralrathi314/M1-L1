l1 = [12,14,10,20,64]
print("List:," ,l1)
s = 0
for i in l1:
    s = s+i
print("sum:", s)
a = s/len (l1)
print("Average:", a)

l1.sort()
print("Sorted list:", l1)
print("Smallest number is", l1[0])
print("Biggest number is", l1[-1])

