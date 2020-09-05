# List

List = ['hey', 'how', 'are', 'you', 25]
List.remove('are')
List.insert(2, 'hey')
print(List)

List = [12, 23, 4, 21, 12, 21, 12]
print(sum(List))
print(List.count(12))
print(len(List))
print(List.index(4))

# Dictionary

dict= {"A": "Python", "B": "Python1", "C": "Python2", "D": "Python3"}
print(dict)
print(dict.keys())
dict.pop("D")
print(dict)
print(dict.items())


# Sets

set = {"apple", "banana", "cherry"}
set2= {"1", "2"}
set.add("orange")
print(set)
print(len(set))
set.remove("banana")
print(set)
x= set.pop()
print(x)
set3= set.union(set2)
print(set3)
print(type(set))

# Tuples

tuple= ("apple", "banana", "cherry")
print(tuple)
print(type(tuple))
print(tuple[2])
print(tuple[1:])
print(len(tuple))
del tuple

# String

name= "abc"
name1= "pqr"
print(name)
name3 = name+name1
print(name3)
print(type(name))
print(name.capitalize())
print(name.index('a'))
print(name1.casefold())
print(name.isnumeric())
a= 3
b= 4
print(a+b)
print(type(a))
print(float(a))

