'''
Exercise 3: Print characters present at an even index number
Write a Python code to accept a string from the user 
and 
display characters present 
at an even index number.

For example, str = "PYnative". so your code should display P, n, t, v.

Expected Output:

Orginal String is  PYnative
Printing only even index chars
P
n
t
v
'''
stringinput = input("enter string")


#  find one more way to solve this. 







index = 0
while index < len(stringinput):
 print(stringinput[index])
 index+=2

for index in range(0,len(stringinput),2):
 print(stringinput[index])


x = len(stringinput)
for index in range(x):
 if index %2 == 0:
  print(stringinput[index])

index =0
while index < len(stringinput):
 if index %2 == 0:
  print(stringinput[index])
 index+=1




print("\n".join([stringinput[i] for i in range(len(stringinput)) if i%2 ==0]))