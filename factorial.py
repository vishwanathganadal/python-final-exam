def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
         return n * factorial(n - 1)
while True:
 n = input("Enter a non-negative integer: ")
 try:
    n = int(n)
    if n < 0:
        print("enter a non-negative integer.")
    else:
      break
 except ValueError:
   print("enter a valid integer.")

result = factorial(n)
if result is not None:
 print(f"The factorial of {n} is {result}.")
else:
 print("Invalid input.")






