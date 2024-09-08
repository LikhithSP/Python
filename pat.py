def ast_pyd():
  print("<<<< Pyramid * Patterns >>>")
  n = int(input("Enter Row for your pyramid : "))
  for i in range(1,n+1):
    for j in range(n-i):
      print(" ",end="")
    for k in range(1,2*i):
      print("*",end="")
    print()

def ast_invt_pyd():
  print("<<<< Pyramid * Patterns (Inverted) >>>")
  n = int(input("Enter Row for your pyramid : "))
  for i in range(n,0,-1):
    for j in range(n-i):
      print(" ",end="")
    for k in range(2*i-1): 
      print("*",end="")
    print()


def alp_pyd():
  print("<<<< Alphabet Pyramid Pattern >>>>")
  n = int(input("Enter no row: "))
  alph = 65
  for i in range(0,n):
    print(" "*(n-i), end=" ")
    for j in range(0,i+1):
      print(chr(alph),end=" ")
      alph+=1
    alph = 65
    print()

def num_pyd():
  print("<<<< Number Pyramid Pattern >>>>")
  n = int(input("Enter Rows : "))
  for i in range(1,n+1):
    for j in range(n-i):
      print(" ",end="")
    for j in range(2*i-1):
      print(j+1,end="")
    print()

def hollow_pyd():
  n = int(input("Enter Rows : "))
  for i in range(1,n+1):
    for j in range(1,2*n):
      if j == n -i + 1 or j == n+i-1 or i==n:
        print("*",end="")
      else:
        print(" ",end="")
    print()

def half_pyd():
  n = int(input("Enter Rows : "))
  for i in range(1,n+1):
    for j in range(1,i+1):
      print("*",end="")
    print("")

def half_num_pyd():
  n = int(input("Enter Rows : "))
  num = 1
  for i in range(0,n):
    num =1
    for j in range(0,i+1):
      print(num,end=" ")
      num+=1
    print("")
half_num_pyd()