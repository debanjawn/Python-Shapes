#make a program that when run that will print out a 5x5 square or asterisk
'''
print('* * * * *')
print('* * * * *')
print('* * * * *')
print('* * * * *')
print('* * * * *')


hei = int(input('Height of Square? --->') )#number of lines there will be vertically
wid = int(input('Width of Square? --->') )#astrisk and space there will be 
for i in range(0,hei,1):
  for j in range(0, wid ,1):
    print ('*', end = ' ')
  print()



#now make right triangle
print('*')
print('* *')
print('* * *')
print('* * * *')
print()

#we need a variable that will change with
side = int(input('Side length of Triangle? ---> ') )
v = side #has to be side because the user might input anything
#v = v - 1 
for t in range(0, side ,1):#y axis
  for r in range(0, v , 1):#x axis
    print('*', end = ' ')
  v = v - 1 #we need this same level as interior loop, keeps first line same then slowly takes out an "*" for everyline
  print()


print('*')
print('* *')
print('* * *')
print('* * * *')
print()


side = int(input('Side length of Triangle? ---> ') )
v = 1
for t in range(0, side ,1 ):#y axis
  for r in range(0, v , 1):#x axis
   print('*', end = ' ')
  print()
  v = v + 1
  


print('        *')
print('      * *')
print('    * * *')
print('  * * * *')
print('* * * * *')

side = int(input('Side length of Triangle? ---> ') )
v = 1 
p = side - 1
for t in range(0 , side , 1 ):#y axis
  for s in range(0, p, 1):
    print(' ', end = ' ')
  for r in range(0 , v , 1):#x axis
    print('*', end = ' ')
  print()
  v = v + 1
  p = p - 1

'''
