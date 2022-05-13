# ---part2
# index("sub string",start.end)



MyString="i love python and C"
print(MyString.index("l"))#--> number of letter
print(MyString.index("o"))#--> number of letter
print(MyString.index("l",2,5))
# print(MyString.index("K"))#--> error

#find("substring",start,end) --> solve error problem of inedex
print(MyString.find("k")) #--> -1
print(MyString.find("l",0,5)) 
print(MyString.find("i",0,8)) 

#rjust and ljust (width,"substring")-->nfs fkra i center

#spilitlines()-->not take any arqu and back them to class : list
a="""firts line
second line
third line """
print(a.splitlines())
print(type(a.splitlines()))

#expandtabs(no)-->for tabs
a="i \tlove\t python\t and \tc"
print(a.expandtabs(20))

#check for class--> istitle --> true or false
# isspace()
# isidefnfier()
# isalpha --> letters only
# isalnum  --> letter and numbers
a="I Love Programming And C"  #--> title
b="I Love Programming And c"  #--> not title becasue c is small 
print(a.istitle())
print(b.istitle())

# relpace("old sub","new sub",count)
a="my name is is mahmoud is ramdaan"
print(a.replace("is","one"))
print(a.replace("is","1",1))
print(a.replace("is","1",2))
print(a.replace("is","1",3))

#join(iterable) --> used for loops take list or tupple and back as string
a=["mahmoud","ramadan","1998"]
print("@".join(a))
print("-".join(a))
print(" ".join(a))
