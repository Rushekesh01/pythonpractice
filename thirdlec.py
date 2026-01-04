# LIST IN PYTHON
#List are ordered collection of items which can be of different data types
marks= [10, 85.36, "Rushi", "01-02-2005"]         #List are mutable i.e we can change the values but Tuples and strings are immutable
print(marks[1])  #85.36
print(marks[2])  #Rushi
marks[2]="Rushikesh"  #Updating value at index 2
print(marks)
print(type(marks))
print(len(marks))  #length of list
marks[2]= "Karan"  #Updating value at index 2
print(marks)
print(marks[0:3])
print(marks[-3:-1])

#List  Methods
list=[4,1,3,8]
list.append(10)   #Adds 10 at the end of list
print(list)
list.sort()         #Sorts list in ascending order  
print(list)
list.sort(reverse=True) #Sorts list in descending order
print(list)
list.reverse()  #Reverses the list          
print(list)

list1=[1,3,4,5]
list1.insert(1,2)  #Inserts 2 at index 1                     list.insert(index,value)
print(list1)

list2 = [1,2,3,2,7,2]
list2.remove(2)  #Removes first occurance of 2 from list
print(list2)
l=[1,3,6,4,5 ]
l.pop(0)   #Removes element on index 0 from list                list.pop(index)
print(l)    

#TUPLES IN PYTHON
#Tuples are immutable i.e we cannot change the values once assigned
tup=(1,"Rush",12.32,"01-02-2005")
print(tup)
print(tup[1])   #Rush   
print(tup[-1])  #01-02-2005
print(tup[0:3]) # (1,"Rush",12.32)
print(type(tup)) 
# tup[1]="Rushi"  #This will give error as tuples are immutable

#TUPLE METHODS
t=(1,2,3,2,4,2,5)
print(t.count(2))   #Counts number of times 2 appears in tuple
print(t.index(4))   #Returns index of first occurance of 4 in tuple

m1=input("Enter 1st fav movie name: ")
m2=input("Enter l2nd fav movie name: ")
m3=input("Enter 3rd fav movie name: ")
list=[m1,m2,m3]
print(list)

