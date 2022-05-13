# set method

#clear()-->remove all elment
a={1,2,3}
a.clear()
print(a)
print("+"*40) #separtor
#add()
a={1,5,6,10.5}
a.add(5)
print(a)
print("+"*40)
#discard()-->not give error
a={1,5,6}
print(a.discard(7))
print("+"*40) #separtor
#pop()-->random slect
print(a.pop())
print("+"*40) #separtor
#update()-
a={1,5,4,50,"mahmoud"}
b={100,200,300}
a.update(b)
print(a)
print("+"*40) #separtor
#union()
a={1,2,6,3,4}
b={1,2,3}
a.union(b)
print(a)
print("+"*40) #separtor
#difference() a-b
a={1,2,6,3}
b={1,2,3}
print(a.difference(b))
print("+"*40) #separtor
#differnece_update()-->btrg3 set
a={1,2,6,3,4}
b={1,2,3}
a.difference_update(b)
print(a)
print("+"*40) #separtor
#intersection()
a={1,2,6,3,4}
b={1,2,3}
print(a.intersection(b))
print("+"*40) #separtor
#intersection_update()-->give set
a={1,2,6,3,4}
b={1,2,3}
a.intersection_update(b)
print(a)
print("+"*40) #separtor
#symmetric_difference()
a={1,2,6,3,4}
b={1,2,3}
print(a.symmetric_difference(b))
print("+"*40) #separtor
#symmetric_difference_update()
a={1,2,6,3,4}
b={1,2,3}
a.symmetric_difference_update(b)
print(a)
print("+"*40) #separtor
#isuperset()-->true or false
a={1,2,6,3,4}
b={1,2,3}
print(a.issuperset(b))
print("+"*40) #separtor
#issubset
a={1,2,6,3,4}
b={1,2,3}
print(a.issubset(b))
print("+"*40) #separtor
#isdisjoint()-->moved or not
a={1,2,6,3,4}
b={100,20,10}
print(a.isdisjoint(b))
print("+"*40) #separtor
