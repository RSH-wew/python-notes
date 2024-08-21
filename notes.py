# yeh niche vla jaadu h
# a = "weather is nice today."
# for nice in a:
#     print(nice)

# #str slicing
# a ="www.rishimodi.com"
# print(a[4:len(a)])
# print(a[-13:])
# print(a[:17])

# #str functions
# str = "I'll be a coder."
# print(str.endswith("er.")) #returns tru if substr ends with
# print(str.capitalize()) #capitalizes 1st character
# print(str.replace("I'll","Baburao will")) #replaces from old char to new
# print(str.lower()) #lowercase 1st character
# print(str.find("z")) #returns 1st index of 1st occurence
# print(str.count("e")) #counts the occurence of substr

# #nesting
# age = int(input("umar daale-> "))
# if age >= 18:
#     if age >=50:
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive")

##
# a = "today is great day.\n today is great." - next lyn
# b = "today is great day.\t today is great." - tab
# c = "my name is rishi modi.\r I am 18 years old." - only second sentence will print
# d = "my name is rishi modi.\b I am 18 years old." - backspace
# print(a)
# print(b)
# print(c)

# #format strings
# b = "my"
# name = "rishi modi"
# age = 34
# a = "{1} name is {2} nd i am {0}"
# print(a.format(age,b,name))

# #list functions - list is mutable whereas str nd tuple are immutable
# a = [31,31223,2132]
# b = [32,42,2,2,2]
# a.append(12) #adds element at the end
# a.extend(b) #add lists
# a.sort() #sorts in ascending order
# a.sort(reverse=True) #sorts in descending order
# a.reverse() #list in reverse order
# b.index(2) #returns index of elm of first occurence
# a.insert(1,2) #insert element at the designated index
# a.remove(31) #remove first occurence of the elm
# a.pop(2) #remove elm from the index entered
# print(a)

# #tuple functions
# a = (1,2, 3, 4, 5,3 ,4 ,5 )
# print(a.index(3)) #first occurence of the elm
# print(a.count(4)) #counts elm

# #dict functions
# dict = {"name":"rishi", "class":12, "subjects":{"chem":21,"phy":12,"maths":32}}
# print(dict.keys()) #returns only keys
# print(dict.values()) #returns only values
# print(dict.items()) #returns key & value as pair of tuple
# print(dict.get("name")) #reutns value of entered key
# print(dict["name"]) #returns value of entered key
# dict.update({"per kyu": "yuhi"}) #updates key nd value when input is dict
# print(dict)

# #set functions - sets are mutable but its elm aren't
# set1 = {1,2,3,4,5,6,7,8}
# set2 = {5,6,7,8,9,0}
# set1.add(311) #adds elm
# set1.remove(311) #removes elm
# set1.clear() #empties set or creates null_set
# set1.pop() #removes a random value
# print(set)
# print(set1.union(set2)) #union of sets
# print(set1.intersection(set2)) #intersection of sets

# #table of any number n
# n = int(input("enter a number -> "))
# i = 1
# while i <=10:
#     print(n*i , i)
#     i += 1

# #printing list using while loop
# list1 = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(list1):
#     print(list1[i])
#     i += 1

# #printing list using for loop
# list1 = [1,4,9,16,25,36,49,64,81,100]
# for x in list1:
#     print(x)

# #finding a num using while loop
# list1 = [1,4,9,16,25,36,49,64,81,100,81,81]
# i = 0
# x = 81
# while i < len(list1):
#     if list1[i] == x:
#         print("found'ya" , i )
#     else:
#         print("not found" , i)
#     i += 1

# #finding a num using for loop
# list1 = [1,4,9,16,25,36,49,64,81,100,81,81]
# y = 81
# i = 0
# for x in list1:
#     if x == y:
#         print("found'ya",i)
#     else:
#         print("not found")
#     i+=1

# #range(start?,stop,stepsize?)
# for i in range(1,11,2):
#     print(i)

# #sum of first n numbers using for loop
# n = int(input("enter a number : "))
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# #sum of first n numbers using while loop
# n = int(input("enter a number : "))
# sum1 = 0
# i = 1
# while i <= n:
#     sum1 += i
#     i+=1
# print(sum1)

# #factorial of first n numbers using for loop
# n = int(input("enter a number : "))
# factorial = 1
# i = 1
# for x in range(1,n+1):
#     factorial *= 1
# print(factorial)

# #factorial of first n numbers using while loop
# n = int(input("enter a number : "))
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i += 1
# print(factorial)

# return value is only useful when there is any parameter in function defined

# object attribute > class attribute {precedence

# a = int(input("enter num 1 -> "))
# b = int(input("enter num 2 -> "))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("division by zero")
# else: 
#     print("no exceptions raised")
# finally:
#     print("regardless of any exception, run this cmd")