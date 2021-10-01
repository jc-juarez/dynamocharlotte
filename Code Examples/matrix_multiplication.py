import dynamocharlotte as dc

dc.run('''

// Matrix Multiplication - Example Program 
// Author: Juan Carlos Juárez https://github.com/JC-Juarez
// Date: May 2021
// Dynamo Charlotte 

var sizeRen1 as number
var sizeCol1 as number
var sizeRen2 as number
var sizeCol2 as number
var i as number
var j as number
var k as number
matrix(50,50) myMat1
matrix(50,50) myMat2
matrix(50,50) myMat3

function getSizes
    do
        println("Please enter row size of first matrix: ")
        input(sizeRen1)
        println("Please enter column size of first matrix: ")
        input(sizeCol1)
        println("Please enter row size of second matrix: ")
        input(sizeRen2)
        println("Please enter column size of second matrix: ")
        input(sizeCol2)
    loopwhile(sizeCol1 != sizeRen2)
return

function fillMat1
    for i = 0 to (sizeRen1 - 1)
        for j = 0 to (sizeCol1 - 1)
            input(myMat1[i][j])
        next
    next
return

function fillMat2
    for i = 0 to (sizeRen2 - 1)
        for j = 0 to (sizeCol2 - 1)
            input(myMat2[i][j])
        next
    next
return

function multiplyMat
    for i = 0 to (sizeRen1 - 1)
        for j = 0 to (sizeCol2 - 1)
            for k = 0 to (sizeCol1 - 1)
                myMat3[i][j] = myMat3[i][j] + (myMat1[i][k] * myMat2[k][j]) 
            next
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

main

print("Matrix Sum")
print(endl)

call getSizes
call fillMat1
call fillMat2
call multiplyMat
call displayMat

end

''')