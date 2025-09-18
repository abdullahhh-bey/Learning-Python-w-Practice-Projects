# import mymodule as m

# x = m.sum(2,3,2,43,45324,1,42345,23)
# print(x)

# print(f"{m.randomNumber()}")
# print(f"{int(m.divide(4,2))}")
# print(f"{int(m.sqrt(45))}")


#Print Only Even Numbers
# num_list = [1,2,3,4,5,6,7,8,9,10]

# for n in num_list:
#     if n%2==0:
#         print(n)




# #Remove all list items that contain 'a' in them
# fruits = ["apple" , "banana", "kiwi", "grapes" , "imli"]

# #List Comprehension
# fruits = [val for val in fruits if "a" not in val]
# print(fruits)




# #Reverse sorting a list
# nums = [5,2,1,9]
# nums.sort(reverse=True)
# print(nums)



# #Copy a list, update it and original should not change
# original = ["Biology" , "Computer" , "Maths"]
# copy = original.copy()
# copy[0] = "English"

# print(copy)
# print(original)




# #Make Tuple and Unpack it into separate variable for each item
# t = (10,20,30,40,50)
# a,b,c,d,e = t
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)




#Join two tuples into One Tuple
# t1 = (1,2,3)
# t2 = (4,5,6)
# mixed = t1 + t2
# print(mixed)





#Remove any element in set so safely that If it dont exists, 
#program should be fine (no error)
# s = {"Apple" , 3 , True , "Hello", 29.3}
# s.discard(2)
# print(s)



#Give union and Intersection of sets
# set1 = {10,20,30,40}
# set2 = {20,70,50,40}

# unionSet = set1.union(set2)
# intersectionSet = set1.intersection(set2)

# print(unionSet)
# print(intersectionSet)




#convert htis duplicate list to set and back to list
# nums = [1,2,2,3,4,4,5,6,6]
# num_set = set(nums)
# nums = list(num_set)
# print(nums)





# #make a dict of 3 countries and their capitls
# dict_list = [
#     {
#         "country" : "Pakistan",
#         "capital" : "Islamabad"
#     }, 
#     {
#         "country" : "England",
#         "capital" : "London"
#     },
#     {
#         "country" : "Turkey",
#         "capital" : "Istanbul"
#     }
# ]

# #example access
# print(dict_list[0]["country"])




#FIND THE CAPITAL OF THE COUNTRY BY TAKING INPUT FROM USER
# dict_list = [
#     {
#         "country" : "pakistan",
#         "capital" : "Islamabad"
#     }, 
#     {
#         "country" : "england",
#         "capital" : "London"
#     },
#     {
#         "country" : "turkey",
#         "capital" : "Istanbul"
#     }
# ]

# input = input("Enter country: ")

# for i in range(0, len(dict_list)):
#     if input in dict_list[i]["country"]:
#         cap = dict_list[i]["capital"]
#     else:
#         continue
    
# print(cap)





#Store 5 student and their grades in a dict and print who has grade "A"
# dict_list = [
#     {
#         "student" : "Alex",
#         "grade" : "A"
#     },
#     {
#         "student" : "Pingu",
#         "grade" : "B"
#     },
#     {
#         "student" : "Hopi",
#         "grade" : "A"
#     },
#     {
#         "student" : "Dembel",
#         "grade" : "D"
#     },
#     {
#         "student" : "Panda",
#         "grade" : "E"
#     },
# ]

# grade_list = []

# for i in range(0 , len(dict_list)):
#     if "A" in dict_list[i]["grade"]:
#         grade_list.append(dict_list[i])
        
# print(grade_list)






# #Merge two dict into one Dictionary
# dict_1 = {
#     "game1" : "Pubg"
# }

# dict_2 = {
#     "game2" : "Clash of Clans"
# }

# merged_dict = {**dict_1 , **dict_2}
# print(merged_dict)





# #Check if key exists in a dict or not
# dict_list = {
#     "name" : "Alex",
#     "skill" : "coding",
#     "age" : 21,
#     "isIntelligent" : False,
#     "isCrazy" : True
# }

# key = input("Enter key you wanna find: ")
# found = False
# for k in dict_list:
#     if key == k:
#         found = True
#     else:
#         continue

# print("Key found" if found==True else "Key not found")

