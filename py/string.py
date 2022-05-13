#------
# 1- create string with single or double quote
# 2- using of """
# --------
# 1-index and slicing
# a- zero based index
# b-acess single elment
# c-acess multi elment
# --------------

myStringone="i love python"

myStringtwo='i love python'

myStringthree="""first 
second 
third"""

myString="i love python"

print(myStringone)
print(myStringtwo)
print(myStringthree)
print(myString)
#single acess
print(myString[0])  #--- I
print(myString[5])  #--- e
print(myString[-1]) #first char from end
# multi acess  slicing
# [start:end] Or [start:end:steps] --> lazem azwd 3la end 1 3ashn a3ml include ll char
print(myString[0:6]) #--> i love
print(myString[0:5]) #--> i lov
print(myString[:6]) #start from zero
print(myString[:])  #Full data
print(myString[8:11])  #yth
  #with steps
print(myString[0:6:1]) #i love
print(myString[0:6:2]) # ilv