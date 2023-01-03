import lib.dog as dog

# print("hello")



# name ="beau"
# print( isinstance(name,str))

# age = int("20")
# print(isinstance(age,int))

# # booleans

# print('hi' or 'hey')
# print([] or False)

# print(0 and 1)
# print(1 and 0)
# print(False and 'hey')
# print('hi' and 'hey')


# is operator compares two objects returns ture if both are the same
# in membership operator tells when a value is contained in a list


# ternary operator
# age = 20
# def is_adult(age):
#     return True if age>28 else False

# # accessing non local variables
# def count():
#     count=0

#     def increment():
#         nonlocal count
#         count= count +1
#         print (count)

#     increment()
# count()



# closures
# def counter():
#     count=0

#     def increment():
#         nonlocal count
#         count= count +1
#         return count

#     return increment

# increment= counter()
# print(increment())
# print(increment())
# print(increment())




# objects

# everything is an object

# loop

# count = 0
# while count<10:
#     print(f"hello {count}")
#     count+=1


# for item in range(15):
#     print(item)

# class

# class Animal:
#     def walk(self):
#         print("walking")

# class Dog(Animal):

#     def __init__(self,name,age) :
#         self.name =name
#         self.age = age
#     def bark (self):
#         print("woof")
# roger = Dog("brian",8)
# print(roger.name)
# print(roger.age)
# roger.bark()
# roger.walk()




# modules

# dog.bark()
from lib.dog import bark

bark()
