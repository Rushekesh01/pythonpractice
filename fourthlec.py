#Dictionary stores key:valuwe pairs
info = { 
    "name": "rush",
    "Gender": "Male",
     "Age": 21, 
     "ListOfSubjects": ["Maths","Science","Geography"],
     "Tuplesofmarks" : (97.2,25.54,65),  
    "is_adult": True,
    "marks" : 98.35,
     21.54 : "Mech" }
print(info)
info["name"] ="Raja"   #Updating value of key 'name'
info["Age"] = 50   #Updating value of key 'Age'
# info["Surname"] :  "Dusane"  this will not add new key value pair in dict
info["Surname"] = "Dusane"  #This will add new key value pair in dict

print(info)
print(type(info))
print(info["name"])  #Accessing value using key
print(info["ListOfSubjects"])  #Accessing list inside dictionary
print(info["ListOfSubjects"][1])     #Accessing 2nd element of list inside dictionary
print(info["Tuplesofmarks"])      #Accessing tuple inside dictionary

nulldict = {}   #Empty dictionary
print(nulldict)
nulldict["name"] ="Rushi"
nulldict["Add"] ="Pune"
nulldict["hobbiesList"] = ["Dancing","Swimming","Playing"]
nulldict["MobilenosTuples"] = (9422681512,9272047759,8007563667,7387423543)
print(nulldict)

#Nested Dictionary
student = {
    "name": "Rushikesh",
    "Subjectsdict": {"M1":78,"M2": 89,"M3" : 99,"M4": 95},  #Dictionary inside dictionary
    "Age" :21 }
print(student)
print(student["Subjectsdict"])   #Accessing inner dictionary
print(student["Subjectsdict"]["M3"])  #Accessing value of key M3    

#Dictionary Methods
Dict = {
    "NAme":"Rohit",
    "Age" :22,
    "City" : "Pune",
    "Gender" :"Male" 
}
print(Dict)
print(Dict.keys())    #Returns all keys of dictionary
print(Dict.values())   #Returns all values of dictionary
print(Dict.items())    #Returns all key:value pairs as tuples in a list
print(Dict.get("NAme"))  #Returns value of key NAme
Dict.update({"Age":23})   #Updates value of key Age to 23
print(Dict)
print(len(Dict))   #Returns number of key:value pairs in dictionary

#SETS IN PYTHON
#Sets are unordered collection of unique items ie, we can't store duplicate values in sets
# just like strings and tuples sets are also immutable 
set = {1,2,3,4,"name","Rushiii", 21.00,6465, True,"Rushiii","name"} #Duplicate will be stored only once
print(set)
print(type(set)) 
print(len(set))  #Length of set by ignoring duplicate ones


set1 = set()  #Converting set to empty set
print(type(set1))

# Set Methods
set2={4,1,3,7,8}
set2.add(21)   #Adds 21 to set
set2.add("Ruush")  #Adds "Rush" to set
print(set2)
set2.remove(4)  
print(set2)
set2.pop() #remove a random value from set
print(set2) 
set2.clear() #empties the set
print(set2)

s1= {1,2,3}
s2 = {3,4,5}
print(s1.union(s2))  #Union of two sets 
 #union method returns a new set with all items from both sets by writing duplicate values only once
print(s1.intersection(s2))  #Intersection of two sets
#Intersection method retrun only the common values from both the sets

D ={
    "cat" : "A Samll animal",
    "Table" :["A furniture with flat top and one or more legs",
               "Used for eating,writing etc"],
}
print(D)
print(type(D["Table"]))


S = {"Python" ,"Java" , "C++" , "JavaScript","Python"," Java","C++","C++","Java"}
print(S)
print(len(S))
print(type(S))

DICT = {}
MS1=int(input("Enter Marks of Subject 1: "))
MS2=int(input("Enter Marks of Subject 2: "))
MS3 = int(input("Eneter marks of Subject 3: "))
DICT["SUB1M"] = MS1
DICT["SUB2M"] = MS2
DICT["SUB3M"] = MS3
print(DICT)
