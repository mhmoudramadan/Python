# ------- string format
# --- old way 
# 1-concatenation
          #like C language  -->place holder
# 2-%s-->string
# 2-%d-->integer
# 2-%f-->float
              #------------
#new way {:s} 
#new way {:d}
#new way {:f}
#.format(name,age,rank)

name="mahmoud"
age=24
rank=12

# 1-concatenation
print("my name is " + name)
print("my name is " +"mahmoud")

#like C language 
print("my name is %s and my age is %d and my rank is %d" %(name,age,rank))

#new way
print("my name is {} and my age is {} and my rank is {}".format(name,age,rank))
print("my name is {:s} and my age is {:d} and my rank is {:d}".format(name,age,rank))
print("my name is {:.5s} and my age is {:d} and my rank is {:.5f}".format(name,age,rank))

#Rearrange Items of string

a,b,c="one","two","three"

print("hello {:s} {:s} {:s}".format(a,b,c))  #hello one two three
print("hello {0:s} {1:s} {2:s}".format(a,b,c)) #hello one two three
print("hello {1:s} {2:s} {0:s}".format(a,b,c)) #hello two three one
print("hello {2:s} {1:s} {0:s}".format(a,b,c)) #hello three two one