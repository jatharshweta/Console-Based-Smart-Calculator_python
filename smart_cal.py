import numpy as np

def menu():
  print("\n---Smart Calculator---")
  print("1. Addition")
  print("2. Subtration")
  print("3. Multiplication")
  print("4. Division")
  print("5. Power")
  print("6. Modulus")
  print("7. Exit",end="")

def get_number(msg):
    while True:
        val = input(msg)
        if val == "":
            print("Please enter a number only!!")
        else:
            try:
                return int(val)
            except:
                print("Invalid input!!! Enter a valid number.")

while True:
  menu()
  ch = get_number("\nEnter operation number: ")
  if ch == 7:#to stop next process
        print("Exit")
        break


  num1=get_number("Enter Number1: ")
  num2=get_number("Enter Number2: ")
  #as per requirement numbers are stored in numpy array
  arr = np.array([num1, num2])
  if ch == 1:
      print("Result:", np.sum(arr))#here we used sum of array

  elif ch == 2:
      print("Result:", num1 - num2)

  elif ch == 3:
      print("Result:", num1 * num2)

  elif ch == 4:
      if num2 != 0:
          print("Result:", num1 / num2)
      else:
          print("Division by zero error")
  elif ch == 5:
      print("Result:", num1 ** num2)

  elif ch == 6:
      print("Result:", num1 % num2)
  else:
      print("Invalid choice")