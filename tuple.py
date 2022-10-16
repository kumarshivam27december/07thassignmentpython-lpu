# it is used to  stores multiple items in a single variable 
# tuples is ordered 
# tuples are unchangeble 
# they are written with rounded brackets 
# tuples are unchangeable ,meaning we can't add,change,remove the items after it is created 
import numbers


my_tuple=(10,20,30,40,50)
print(my_tuple[1])
# my_tuple[1]=100 it won't return 
print(len(my_tuple))

# create a tuple with one item  
mytuple=(10,)
print(mytuple) 
# NOTE : it won't work if mytuple=(10)


# you can store items of any data type 
mytuple1=(10,'apple',True,100)
print(mytuple1)

# tuple constructor
mytuple2=tuple((10,20,30,40,40))
print(mytuple2) 

# access the elements of tuple 

print(mytuple2[3]) 
print(mytuple2[2:4]) #you can also use range of indexes 

# change tuple elements (tuples are immutable or unchangeble)

mytuple3=[10,20,30,40,50,60,70,80,90,100]
mylist=list(mytuple3)
print(mylist)


mylist[2]=200
print(mylist)

mytuple3=tuple(mylist)
print(mytuple3)

# append tuple with another tuple
mytuple4=(10,20,30,40,50,60)
k=(70,)
mytuple5=k + mytuple4
print(mytuple5)

# always remember in above code we have to name it other than mytuple4 otherwise it will give the same output
# NOTE IF TUPLE1=(10,20,30)
# del TUPLE1 
# PRINT(TUPLE1)
# SYNTAX WILL BE SHOWN ERROR WE U HAVE DELETED EVERYTHING PERMANENTLY 



# unpack a tuple 
# in python ,we can extract the value into diff vaariables .this is unpackaging
number=(10,20,30)  #this is packing
(num1,num2,num3) = number
# num oof variables should match numbers of item in the tuple
print(num1)
print(num2)
print(num3)

numberone=(10,20,30,40,50,60,70,80)
(num1,num2,*num3)=numberone
print(num1)
print(num2)
print(num3) # rest of the values are stored in a list
# we can add streak if not then syntax error
# if *is with num2 then it will give 
# 10
# [20,30,40,50,60,70]
# 80 
# respectively







# loop through tuples for loops 
mytuple10=('apple','banana','orange')
for x in mytuple10 :
    print(x)

# looping through the index numbers
print(len(mytuple10))
print(range(len(mytuple10)))

for i in range(len(mytuple10)):
    print(mytuple10[i])
    



# joining tuple 
tuple10=(10,20,30,40,)
tuple20=(50,60,70,80,90)
tuple30=tuple10+tuple20
print(tuple30)



# MULTIPLICATION OF TUPLES
mynewtuple=("apple","oranges","banana","mangoes",)
multipliedtuple=mynewtuple*3
print(multipliedtuple)



















