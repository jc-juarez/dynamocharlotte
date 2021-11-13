import dynamocharlotte as dc

dc.run('''

// Matrix Sum - Example Program 
// Author: Juan Carlos Juárez https://github.com/JC-Juarez
// Date: May 2021
// Dynamo Charlotte

var sizeRen1 as number
var sizeCol1 as number
var sizeRen2 as number
var sizeCol2 as number
var i as number
var j as number
var x as number
matrix(50,50) myMat1
matrix(50,50) myMat2
matrix(50,50) myMat3

function fillMat1
    for i = 0 to (sizeRen1 - 1)
        for j = 0 to (sizeCol1 - 1)
            input(x)
            myMat1[i][j] = x
        next
    next
return

function fillMat2
    for i = 0 to (sizeRen2 - 1)
        for j = 0 to (sizeCol2 - 1)
            input(x)
            myMat2[i][j] = x
        next
    next
return

function sumMat
    for i = 0 to (sizeRen1 - 1)
        for j = 0 to (sizeCol1 - 1)
            myMat3[i][j] = myMat1[i][j] + myMat2[i][j]
        next
    next
return

function displayMat
    print(endl)
    for i = 0 to (sizeRen1 - 1)
        for j = 0 to (sizeCol1 - 1)
            println(myMat3[i][j] + " ")
        next
        print(endl)
    next
return

Main<>

print("Matrix Sum")
print(endl)
do
    println("Please enter row size of first matrix: ")
    input(sizeRen1)
    println("Please enter column size of first matrix: ")
    input(sizeCol1)
    println("Please enter row size of second matrix: ")
    input(sizeRen2)
    println("Please enter column size of second matrix: ")
    input(sizeCol2)
loopwhile(sizeRen1 != sizeRen2 or sizeCol1 != sizeCol2)
call fillMat1
call fillMat2
call sumMat
call displayMat

End<>

''')