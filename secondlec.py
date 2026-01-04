st1 ="Hello Guys I Am Rush Pleasure to Meet You All OF\tall"   #\t is used to give tab space.
print(st1)
str2= "How Are You karan?\nHope You are Dooing Well."    #\n is used to jump on next line
print(str2)      # \t and \n are escape sequences characters.
str3= "This is a backslash \\ "   # to print backslash we use double backslash
print(str3)

# Basic String Operations
#Concatenation
str1="Rushe"
str2 ="kesh"
Result= str1 + str2  # "+" is used for concatenation in strings
print(Result)
print(len(str1))   # len() function is used to find length of string
#INDEXING
st1="Rushikesh"
print(st1[0])   # R
print(st1[4])   # i
print(st1[-1])  # h
print(st1[-3])  # k
#SCLICING
temp = "Khannaji"
print(temp[0:5])
print(temp[1:6])
print(temp[-4:])

#STRING FUNCTIONS
st="rushikesh"
print(st.endswith("sh"))   # checks whether string ends with given character or not
print(st.count("s"))      # counts number of times given character appears in string
print(st.capitalize())    # capitalizes first character of string
print(st.find("k"))       # returns index of given character
print(st.replace("r","R"))  # replaces given character with another character
print(st.lower())         # converts string to lowercase
print(st.upper())         # converts string to uppercase


s=input("Enter a sting: ")
print(len(s))
sr="Dasda%ghwk%kgnj%;rgek5flge%"
print(sr.count("%"))

#CONDITIONAL STATEMENTS 
# 1)if-elif-else
age=int(input("Enter Your age: "))
if(age>=18 and age<=100):
    print("Can Vote")
elif(age>100):
    print("Your Are More Tahn Normal Age")
elif(age<18):
    print("Sry Can't Vote")
else:
    print("Invalid Input")
    
marks=int(input("Enter Your Marks: "))
if(marks>=90 and marks<=80):
    print("A Garde")
elif(marks<=80 and marks>=70):
    print("B Grade")
elif(marks<=70 and marks>=60):
    print("C Garde")
elif(marks<=60  and marks>=50):
    print("D Garde")
else:
    print("Fail")