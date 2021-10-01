import dynamocharlotte as dc

dc.run('''

// Factorial Recursive Function - Example Program 
// Author: Juan Carlos Juárez https://github.com/JC-Juarez
// Date: May 2021
// Dynamo Charlotte 

var fact as number
var x as number
var y as number

function getFactorial
    if(x > 1)
        fact*= x
        x--
        call getFactorial
    endif
return

main

do
    print("*** Factorial Calculator ***")
    println("Please insert a number: ")
    input(x)
loopwhile(x < 0)
y = x
fact = 1
call getFactorial
print("The Factorial of " + y + " is " + fact)

end

''')