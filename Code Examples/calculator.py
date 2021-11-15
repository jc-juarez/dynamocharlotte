import dynamocharlotte as dc

dc.run('''

// Basic Calculator - Example Program 
// Author: Juan Carlos Juárez https://github.com/JC-Juarez
// Date: November 2021
// Dynamo Charlotte

var option as string
var num1 as number
var num2 as number
var res as number

function getNumbers
  println("Please insert the first Number: ")
  input(num1)
  println("Please insert the second Number: ")
  input(num2)
return

Main<>

print("*** Welcome to Dynamo Calculator ***")

do
  print(endl)
  print("Choose an option:")
  print("a) Sum")
  print("b) Subtraction")
  print("c) Multiplication")
  print("d) division")
  print("e) Exit")
  print(endl)
  println("Your Option: ")
  input(option)
  if(option == "a")
    print("* Sum *")
    call getNumbers
    res = num1 + num2
    println("The Result of " + num1 + " + " + num2 + " is: ")
  endif
  if(option == "b")
    print("* Subtraction *")
    call getNumbers
    res = num1 - num2
    println("The Result of " + num1 + " - " + num2 + " is: ")
  endif
  if(option == "c")
     print("* Multiplication *")
     call getNumbers
     res = num1 * num2
     println("The Result of " + num1 + " * " + num2 + " is: ")
  endif
  if(option == "d")
    print("* Division *")
    call getNumbers
    res = num1 / num2
    println("The Result of " + num1 + " / " + num2 + " is: ")
  endif
  if(option != "a" and option != "b" and option != "c" and option != "d" and option != "e")
    print("Please choose a valid option.")
  endif
  if(option == "a" or option == "b" or option == "c" or option == "d")
    print(res)
  endif
loopwhile(option != "e")

print(endl)
print("*** Thank you for using Dyanmo Calculator ***")

End<>

''')