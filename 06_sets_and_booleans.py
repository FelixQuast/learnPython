# Sets and Booleans
# Elemente können nur einmal in einem Set vorkommen

import random


a = {1,2,3,4}
print(type(a))

s = set()
print(type(s))

s.add(1)
print(s)
s.add(2)
print(s)
s.add(2)
print(s)

l = [10,2,3,2,4,5,2,3,4,5,3,3,3,2,1,1,1,3,4,5,6,True,"string", 7,8,9,7,6,54,4,3]
print(l)
s1 = set(l)
print(s1)


s1.remove(54)
print(s1)

