#1.Arithmetic operators: +, -, *, / etc.

a = 7 
b = 4
c = a+b
print(c)

#2. Assignment operators: =, +=, -= etc.

a = 4-2 #assign 4-2 in a 
print(a)
b = 5
print(b)
b += 5 #Increment value of b by 5 and then assign it to b 
print(b)
b -= 3 #Decrement value of b by 3 and then assign it to b
print(b)

#3. Comparison operators: ==, >, >=, <, != etc.

d = 5>4
print("d = 5>4 is",d)
#Comparation operators return True or Flase 
d=5>=6
print("d=5>=6 is",d)

d= 5!=7
print(d)    

#4. Logical operators: and, or, not.
e = True or False #if either of condition is true it will return True
print(e)
f = True and False #If both of condition is true it will return True else False
print(f)
#Truth table of 'or'
print("True or False is ",True or False)
print("True or True is ",True or True)
print("false or true is ",False or True)
print("False or False is ",False or False)

#Truth table of 'and'
print("True And False is ",True and False)
print("True And True is ",True and True)
print("False And true is ",False and True)
print("False And False is ",False and False)

print(not(False)) #not operator