//Left-aligned triangle
e= int(input("Please enter a number"))
for i in range(1,e+1):
  print("*" * i)
//Right-aligned triangle
e= int(input("Please enter a number"))
for i in range(1,e+1):
  print(" " * (e-i) + "*" * i)
// Hollow triangle
e = int(input("Please enter a number: "))
for i in range(1, e + 1):
    if i == 1:
      print(" " * (e - i) + "*")
    elif i == e:
      print("*" * (2 * e - 1))
    else:
       print(" " * (e - i) + "*" + " " * (2 * i - 3) + "*")
