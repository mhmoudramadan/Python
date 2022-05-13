#----- tupples format 
# -- Imutable
#not support assign 
tupleone=(1,2,3,4)
print(tupleone)

a=("one", "two",1,5,90,5.23)
print(a)

#repeat --- *
print(a*5) # repaet 5 times

#index(item il bshof mkano )
a=(1,2,6,10,4,11,26,9,6)
print("the position is {:d}".format(a.index(26)))

#tupple desturct
b=(1,2,3,4)
x,y,_,z=b  # --(_)--> ignore item
print(x) #1
print(y) #2
print(z) #4