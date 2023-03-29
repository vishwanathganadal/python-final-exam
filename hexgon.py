while True:
  size = input("Enter a size for the hexagon: ")
  try:
    size = int(size)
    if size > 0:
        break
    else:
      print("Error: Size must be a positive integer.")
  except ValueError:
   print("Error: Invalid input. Size must be a positive integer.")

for i in range(size):
 print(" "*(size-i-1) + "* "*(i+1))

for i in range(size-1):
 print(" "*(i+1) + "* "*(size-i-1))