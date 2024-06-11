#to remove an empty tuple from a list of tuples format [(),(1,2,3)] to [(1,2,3)]
d=[(),('',),(1,2,3),(5,)]
d=[i for i in d if i and all(i)]
print(d)
