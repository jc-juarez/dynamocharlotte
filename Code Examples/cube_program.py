import dynamocharlotte as dc 

dc.run('''

// Cube Program - Example Program 
// Author: Juan Carlos Juárez https://github.com/JC-Juarez
// Date: May 2021
// Dynamo Charlotte 

var i as number
var j as number
var k as number

cube(2,3,2) myCube

main

print("Enter 12 values: ")
for i = 0 to 1
    for j = 0 to 2
        for k = 0 to 1
            input(myCube[i][j][k])
        next
    next
next

print(endl)

for i = 0 to 1
    for j = 0 to 2
        for k = 0 to 1
            print(myCube[i][j][k])
        next
    next
next

end

''')