# ------
# string method 
# len()--->length with spacess

myString="i love python"
myStringone="     i love python   "
print(len(myString))
print(len(myStringone))

#strip()-->remove sapce right and left
myStringtwo="     i love python   "
two="####i love python####"
mytwo="#@#@i love python#@#@"
print(myStringtwo.strip())
print(two.strip("#"))
print(mytwo.strip("#@"))

#lstrip()--> from right
myStringtree="     i love python   "
print(myStringtree.lstrip()) 

#rstrip()--> from left
myStringtree="     i love python   "
print(myStringtree.rstrip())


#title()--> captaile first letter of every word and letter after number
a=" i love python and 2d array"
print(a.title())

#upper() --> captaile all letters
b="i love python"
print(b.upper()) 
# lower()--> small all letters
c="I LOVE PYTHON"
print(c.lower()) 

# zfill()-->pattern for numbers
# 001
# 002
# 010
# 111
a,b,c="1","10","100"
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

#split()--> b2sm il items by dafult by space

a="i love python and c programming"
b="i_love_python_and_c_programming"
print(a.split())
print(b.split())
print(b.split("_"))
print(b.split("_",3)) #3--> max split
print(b.split("_",4)) #4--> max split
print(b.rsplit("_",3)) # from rigth
print(type(a.split())) #type--> list


#count("char",start,end)-->how time it repeated
a="i love C and C and C"
print(a.count("C"))
print(a.count("i"))
print(a.count("love"))
print(a.count("and"))

#center(width,char)--> take one arru at least
a="mahmoud"
print(a.center(10,"@"))

#startwith("char",start,end)--> true or fasle
a="i love python and C programming"
print(a.startswith("i"))
print(a.startswith("l"))
print(a.startswith("l",2,6))
print(a.startswith("o",2,6))
print(a.endswith("p",2,8))


#swapcase()-->cap to small and vise vers
a="i love python"
b="I LOVE PYTHON"
print(a.swapcase())
print(b.swapcase())