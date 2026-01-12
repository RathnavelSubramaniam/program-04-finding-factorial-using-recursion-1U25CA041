def factorial(n):
    if n==0 or n==1:
        return 1
    else:
             return n*factorial(n-1)
number=int(input("Enter a number:"))
if number<0:
      print("\nError:factorial is not defined fornegative numbers.")
else:
    result=factorial(number)
    print(f"\nThe factorial of {number} is {result}")  