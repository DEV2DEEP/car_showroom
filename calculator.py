a = float(input("Enter 1st number :"))
b = float(input("Enter 2nd number :"))
print("Choose the operation : \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
c = input("Enter the operation :")
if c == 1:
  print("Addition value of given number: ",a+b)
elif c == 2:
  print("Subtraction value of given number: ",a-b)
elif c == 3:
  print("Multiplication value of given number: ",a*b)
elif c == 4:
  print("Division value of given number: ",a/b)
else :
  print("Choose a valid operation!")
  print(c)
  while c >= 5:
    print(a)
    print(b)
