# Exercise 1
# Expected outputs: 1x hello, 2x Python, 3x fun, 1x 2022
student = 0

while (student < 7):
    if (student < 1):
        print("hello")
    elif (student < 3):
        print("Python")
    elif (student < 0):
        print("bye")
    elif (student <= 5):
        print("fun")
    else:
        print("2022")

    student += 1

## Convert while loop into for loop 

for x in range(7): 
  if (x < 1):
      print("hello")
  elif (x < 3):
      print("Python")
  elif (x < 0):
      print("bye")
  elif (x <= 5):
      print("fun")
  else:
      print("2022")

## Exercise 2 
## Outputs: 1x hello, 2x Python, 1x New Year, 1x Bye, 2x 2022
for x in range(4, 11): # [4, 5, 6, 7, 8, 9, 10]
  if(x < 5):
    print("hello")
  elif(x < 7): 
    print("Python")
  elif(x < 8): 
    print("New Year")
  elif(x < 9): 
    print("bye")
  else: 
    print(2022)


#Exercise 3 
# Outputs: 2x hello, 1x Python, 1x New Year, 2x Bye, 2x, 2022
for x in range(7, 29, 3): # [7, 10, 13, 16, 19, 22, 25, 28]
  if(x < 12): # 11, 12, 13 
    print("hello")
  elif(x < 16): # 14, 15, 16 
    print("Python")
  elif(x < 19): # 17, 18, 19 
    print("New Year")
  elif(x < 25): # 23, 24, 25 
    print("bye")
  else: 
    print(2022)


