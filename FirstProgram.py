print("hello world")
print("Hello Rush.","How are you?")
print(25)
print(25+33)

#Variables

name="Rush"
age=25
price=19.99
a=None
old =True
print(type(age))
print(type(price))
print(type(price))
print(type(a))
print(type(old))

print("My name is",name)
print("My name is "+name)
print("My name is",name,"and my age is",age)
age2=age+5
print(age2)

a=2
b=5
sum=a+b
print(sum)

#OPERATORS
#Arithematic Operators (+ ,-, *, /, %, //, **)
a=2
b=10
print(a+b)
print(a-b)
print(a*b)
print(b/a)
print(b%a)
print(b//a)  # floor divison  ie, gives floor value
print(a**b)  #a raised to the power b


# Relational Operators (==, !=, >, <, >=, <=)
a=5
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Assignment Operators (=, +=, -=, *=, /=, %=, //=, **=)
num=10
num= num+5  
print(num)
    #num=num+5 is same as num +=5
num=5
num +=5
print(num)

a=5
a -=2   # is same as a=a-2
print(a)

b=8
b *=2   # is same as b=b*2
print(b)

c=20
c /=4   # is same as c=c/4
print(c)

d=10
d %=4   # is same as d=d%4
print(d)

e=15
e //=4   # is same as e=e//4
print(e)

f=2
f **=3   # is same as f=f**3
print(f)

#Logical Operators (and, or, not)

print(not True)
print(not False)
print((5>3) and (10>5))   #OR favours to TRUE     &      And Favours to FALSE
print((5>3) or (10<5))
print(not(5>3))
print(not(5<3))


#Type Conversion
a=5
b=2.5
print(type(a))
print(type(b))
a=float(a)
b=int(b)
print(type(a))
print(type(b))
print(a)
print(b)

a=3.45
a=str(a)
print(type(a))

#Inputs In Python
input=input()
print(input)
print(type(input))  #default type of input is string


name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hello",name,"Your age is",age)

num=int(input())
print(num)

decimalnum = float(input())
print(decimalnum)

name = input("Enter your name: ")
age=int(input("Enter your age: "))
marks=float(input("Enter your marks: "))
print("Hello",name,"Your age is",age,"and your marks are",marks)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum=a+b
print("The sum is:",sum)

