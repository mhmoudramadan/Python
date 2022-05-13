# ----- list like Array 
#-format--> take any data -- int - float - string - boolean

listone=["one" , "two ", 1 , 2 , 1.45 , True]
print(listone)

#change elments
listone[3]=10
print(listone)

#list method 
#Append() -- add elment
Var1=["one" , "two ", 1 , 2 , 1.45 , True]
Var2=["one" , "two ", 1 , 2 , 100, True]
Var1.append(Var2)
print(Var1)
print(Var1[6][2]) #-- 1

#entend() -->farz il lements
Var1=["one" , "two ", 1 , 2 , 1.45 , True]
Var1.extend(Var2)
print(Var1)

#remove()
a=["one", "one" ,1,1,2,2 ]
a.remove("one")
a.remove(1)
a.remove(2)
print(a)

#sort(reverse=False)
a=[1,2,5,10,-8,6]
a.sort(reverse=False)
print(a)
a.sort(reverse=True)
print(a)

#clear()
a.clear()
print(a)

#var1.copy(var2)
b=[1,2,3,4,5]
c=b.copy()
print(b)
print(c)

#pop(index)
print(b.pop(2)) #--[3]

#insert(index,"object") -->insert before index 
c=["one", "two",50,90,80,6]
c.insert(3,True)
c.insert(5,1)
c.insert(4,"three")
print(c)

