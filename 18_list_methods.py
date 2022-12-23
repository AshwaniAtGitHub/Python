l1 = [33, 56, 7, 8, 2, 1, 6]
print(l1)
l1.sort() # no need store the values of l1 in another variable.
print(l1)
l1.reverse() # reverse the list
print(l1)
l1.append(35) # adds 35 at the end of the list
print(l1)
l1.insert(5,455) # inserts 455 at index 5.
print(l1)
l1.pop(3) # removes element at the index 3.
print(l1)
l1.remove(56) # removes (56) from the list.
print(l1)


l = [11, 45, 1, 2, 4, 6, 1, 1]
print(l)
l.append(7)
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
# m = l # here list m is a reference of list l, which is not a new list unlike following
m = l.copy() # here list m is a copy of list l.
m[0] = 0
l.insert(1, 899)
m = [900, 1000, 1100]
l.extend(m)
# k = l + m
# print(k)
print(l)