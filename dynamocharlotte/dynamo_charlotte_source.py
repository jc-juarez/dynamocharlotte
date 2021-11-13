# Dynamo Charlotte 
# 'dynamo_charlotte_source.py'
# Author: Juan Carlos Juárez
# Version: 1.0.0
# MVP Released Version

# Licensed under MPL 2.0. 
# All rights reserved.

import dynamocharlotte.ply.lex as lex
import dynamocharlotte.ply.yacc as yacc
import sys
from collections import deque
from inspect import getframeinfo, stack

# Notes about the Language:
# - Booleans are handled inside the Lnaguage Source Code by 1's and 0's.

# Revision : May 23rd 2021
# - When obtaining a value for an error check if value is a Temporal in avail to obtain its value
# - In Arithmetic Expressions Check that Variables and Object Variables Position correspond to Floats
# - Add Print and Read Quadruple

# Changes made to Update in Documentation:
# - Erased THEN from If Statement
# - Erased ID after NEXT from For Loop
# - Changed gosub to call
# - Changed Program (from begin) to main
# - Changed Dim to var 
# - Changed Subprocedure to Function
# - Added Println (prints in same Line)
# - Print Allows to Sum strings = print("hello " + "world!")
# - Print no longer supports arithmetic inside
# - Changed float to number
# - Changed word to string
# - Added Unitary Operators: id++ and id--
# - Added Binary Operators: id+=, id-=, id*=, id/=, id%= (Only for Numbers, not Strings)
# - Changed Different from <> to !=

# Detects if an input or ouput exists
gio = False

# _________________LEXIS____________________

tokens = [
	'VAR',
	'AS',
	'NUMBER',
	'NUMBER_KEYWORD',
	'STRING',
	'STRING_KEYWORD',
	'VECTOR_KEYWORD',
	'MAT_KEYWORD',
    'CUBE_KEYWORD',
	'FUNCTION', 
	'RETURN', 
	'MAIN', 
    'CALL',
	'END',  
	'IF', 
	'ENDIF', 
	'ELSE', 
	'PRINT',
    'PRINTLN', 
	'INPUT', 
	'LEFTPAR', 
	'RIGHTPAR', 
	'COMMA',
	'ID',
	'PLUS',
	'MINUS',
	'DIVIDE',
	'MULTIPLY',
	'EQUALS',
    'MODULO',
    'WHILE', 
    'WEND', 
    'DO', 
    'LOOPWHILE', 
    'FOR', 
    'TO', 
    'NEXT', 
    'SAME', 
    'DIFFERENT', 
    'GREATERTHAN', 
    'LESSTHAN', 
    'GREATEREQUAL', 
    'LESSEQUAL',
    'DOT',
    'RESIZE',
    'ADD',
    'ADDROW',
    'ADDCOL',
    'ADDX',
    'ADDY',
    'ADDZ',
    'AND',
    'OR',
    'LEFTBRACKET',
    'RIGHTBRACKET',
    'ENDL'
]

# Ignored Characters and Comments

t_ignore = " \t"
t_ignore_COMMENTS = r'\/\/.*'

# Defined One-Character-Tokens

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_COMMA = r'\,'
t_MODULO = r'\%'
t_DOT = r'\.'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r'\]'

# Static Tokens

def t_ENDIF(t):
	r'\b(endif)\b'
	t.type = 'ENDIF'
	return t

def t_WEND(t):
    r'\b(endwhile)\b'
    t.type = 'WEND'
    return t

def t_ENDL(t):
	r'\b(endl)\b'
	t.type = 'ENDL'
	return t

def t_VAR(t):
	r'\b(var)\b'
	t.type = 'VAR'
	return t

def t_AS(t):
	r'\b(as)\b'
	t.type = 'AS'
	return t

def t_NUMBER_KEYWORD(t):
	r'\b(number)\b'
	t.type = 'NUMBER_KEYWORD'
	return t

def t_STRING_KEYWORD(t):
	r'\b(string)\b'
	t.type = 'STRING_KEYWORD'
	return t

def t_VECTOR_KEYWORD(t):
	r'\b(vector)\b'
	t.type = 'VECTOR_KEYWORD'
	return t

def t_MAT_KEYWORD(t):
	r'\b(matrix)\b'
	t.type = 'MAT_KEYWORD'
	return t

def t_CUBE_KEYWORD(t):
	r'\b(cube)\b'
	t.type = 'CUBE_KEYWORD'
	return t

def t_FUNCTION(t):
	r'\b(function)\b'
	t.type = 'FUNCTION'
	return t

def t_RETURN(t):
	r'\b(return)\b'
	t.type = 'RETURN'
	return t

def t_MAIN(t):
	r'\b(Main)\b\<\>'
	t.type = 'MAIN'
	return t

def t_END(t):
	r'\b(End)\b\<\>'
	t.type = 'END'
	return t

def t_IF(t):
	r'\b(if)\b'
	t.type = 'IF'
	return t

def t_ELSE(t):
	r'\b(else)\b'
	t.type = 'ELSE'
	return t

def t_PRINTLN(t):
	r'\b(println)\b'
	t.type = 'PRINTLN'
	return t

def t_PRINT(t):
	r'\b(print)\b'
	t.type = 'PRINT'
	return t

def t_INPUT(t):
	r'\b(input)\b'
	t.type = 'INPUT'
	return t

def t_CALL(t):
    r'\b(call)\b'
    t.type = 'CALL'
    return t

def t_WHILE(t):
    r'\b(while)\b'
    t.type = 'WHILE'
    return t

def t_DO(t):
    r'\b(do)\b'
    t.type = 'DO'
    return t

def t_LOOPWHILE(t):
    r'\b(loopwhile)\b'
    t.type = 'LOOPWHILE'
    return t

def t_FOR(t):
    r'\b(for)\b'
    t.type = 'FOR'
    return t

def t_TO(t):
    r'\b(to)\b'
    t.type = 'TO'
    return t

def t_NEXT(t):
    r'\b(next)\b'
    t.type = 'NEXT'
    return t

def t_SAME(t):
    r'=='
    t.type = 'SAME'
    return t

def t_DIFFERENT(t):
    r'!='
    t.type = 'DIFFERENT'
    return t

def t_GREATEREQUAL(t):
    r'>='
    t.type = 'GREATEREQUAL'
    return t

def t_LESSEQUAL(t):
    r'<='
    t.type = 'LESSEQUAL'
    return t

def t_GREATERTHAN(t):
    r'>'
    t.type = 'GREATERTHAN'
    return t

def t_LESSTHAN(t):
    r'<'
    t.type = 'LESSTHAN'
    return t

def t_RESIZE(t):
    r'\b(resize)\b'
    t.type = 'RESIZE'
    return t

def t_ADDROW(t):
    r'\b(addRow)\b'
    t.type = 'ADDROW'
    return t

def t_ADDCOL(t):
    r'\b(addCol)\b'
    t.type = 'ADDCOL'
    return t
def t_ADDX(t):
    r'\b(addX)\b'
    t.type = 'ADDX'
    return t

def t_ADDY(t):
    r'\b(addY)\b'
    t.type = 'ADDY'
    return t

def t_ADDZ(t):
    r'\b(addZ)\b'
    t.type = 'ADDZ'
    return t

def t_ADD(t):
    r'\b(add)\b'
    t.type = 'ADD'
    return t

def t_AND(t):
    r'\b(and)\b'
    t.type = 'AND'
    return t

def t_OR(t):
    r'\b(or)\b'
    t.type = 'OR'
    return t

# Variable Tokens

def t_NUMBER(t):
    r'(\-|)\d+((\.\d+)|)'
    try:
    	t.value = float(t.value)
    except ValueError:
        print("\n<!> Error in Dynamo Charlotte: Float value not supported %d", t.value)
        t.value = 0
    return t

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type = 'ID'
	return t

def t_STRING(t):
	r'\".+?(")'
	curr = str(t.value)
	curr = curr[1:]
	curr = curr[:-1]
	t.value = curr
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    global gio
    gio = True
    print("\n<!> Error in Dynamo Charlotte: '%s' is not a defined Keyword.\n" % t.value[0])
    t.lexer.skip(1)
    sys.exit()

# Lexer Construction

lexer = lex.lex()

# Operations Precedence

precedence = (
	('left', 'PLUS', 'MINUS'),
	('left', 'MULTIPLY', 'DIVIDE', 'MODULO'),
    ('left', 'AND', 'OR')
)

# _______PROGRAM MEMORY AND VARIABLES_________

# Variables Memory

varMemory = {}

# Subprocedures Memory

subMemory = {}

# Object Variables Memory Array

objectVar = []

# Object Variables Start Position in Memory (True Memory; used to check if object exists)

objectStart = {}

# Object Variables Memory Position

objectPos = 0

# Traditional Variables Memory Position

varPosition = 0

# Quadruples Expressions Memory

quadruplesArithmeticLocal = []
quadruplesLogicLocal = []
quadruplesAll = []

# Quadruples Operands

operands = deque()

# Quadruples Avail

avail = {}
avail["T1"] = None
avail["T2"] = None
avail["T3"] = None
avail["T4"] = None
avail["T5"] = None
avail["T6"] = None
avail["T7"] = None
avail["T8"] = None
avail["T9"] = None
avail["T10"] = None
avail["T11"] = None
avail["T12"] = None

# Available Temporals 

availSet = ["T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9", "T10", "T11", "T12"]

# Jump Stack

jumpstack = deque()

# Execution Stack

execstack = deque()

# Quadruples Generation Counter

cont = 0

# Program Counter

PC = 0

# Position Offset of dc.run 

offsetPos = 0

# _________________GRAMMAR____________________

# Main Production

def p_maindc(t):
    'maindc 			: firstQuadruple dc_compound_program'
    global varMemory
    global subMemory
    global quadruplesAll
    global cont
    global PC
    global execstack
    global avail
    global availSet
    global objectStart
    global objectPos
    global objectVar
    global offsetPos
    #print(">>> Correct Code <<<")
    #print("")
    ##print("<<< Symbol Table >>>\n")
    #if(len(varMemory)>0):
    #    for key in varMemory:
    #        print(key, ' : ', varMemory[key])
    #print("")
    #print("<<< Functions Table >>>\n")
    #for key in subMemory:
    #        print(key, ' : ', subMemory[key])
    #print("")
    #print("<<< Quadruples Expressions >>>\n")
    #varCont = 0
    #for i in quadruplesAll:
    #    print(str(varCont) + " - " + str(i))
    #    varCont+=1
    #print(cont)
    #res = avail.index(['T5'])
    #print(res)
    #print(availSet)
    print("")
    print("------------------------------------------------")
    print("         <<< © Dynamo Charlotte >>> ")
    print("            By Juan Carlos Juárez       ")
    print("Learn more at https://juancarlosjuarez.epizy.com")
    print("------------------------------------------------")
    print("")
    #___________________________________________
    #______________EXECUTION____________________
    #___________________________________________
    PC = 0
    opcode = 0
    flagSameLine = 0
    while(opcode!="PROGRAMEND"):
        quadruple = quadruplesAll[PC]
        opcode = quadruple[0]
        if(opcode == "goto"):
            PC = quadruple[1]
        elif(opcode == "gotoF"):
            logicVar = avail[quadruple[1]]
            if(not logicVar):
                PC = quadruple[2]
            else:
                PC+=1
        elif(opcode == "gotoT"):
            logicVar = avail[quadruple[1]]
            if(logicVar):
                PC = quadruple[2]
            else:
                PC+=1
        elif(opcode == "CALL"):
            execstack.append(PC+1)
            PC = quadruple[1]
        elif(opcode == "endprocedure"):
            PC = execstack.pop()
        elif(opcode == "PRINT"):
            op1 = quadruple[1]
            if(op1 in avail):
                op1 = avail[op1]
            if(op1 in varMemory):
                op1 = varMemory[op1][1]
            if(type(op1)==float and op1.is_integer()):
                op1 = int(op1)
            if(flagSameLine==0):
                print(">> "+str(op1))
            else:
                print(str(op1))
            PC+=1
        elif(opcode == "PRINTLN"):
            op1 = quadruple[1]
            if(op1 in avail):
                op1 = avail[op1]
            if(op1 in varMemory):
                op1 = varMemory[op1][1]
            if(type(op1)==float and op1.is_integer()):
                op1 = int(op1)
            if(flagSameLine == 0):
                flagSameLine = 1
                print(">> "+str(op1), end='')
            else:
                print(str(op1), end='')
            PC+=1
        elif(opcode == "PRINTENDL"):
            print("")
            flagSameLine = 0
            PC+=1
        elif(opcode == "INPUT"):
            currVal = ""
            if(flagSameLine == 1):
                currVal = input()
                flagSameLine = 0
            else:
                currVal = input("<< ")
            if(varMemory[quadruple[1]][0]=="number"):
                try:
                    currVal = float(currVal)
                    varMemory[quadruple[1]][1] = currVal
                except ValueError:
                    print("<!> Error in Dynamo Charlotte: Input '" + str(currVal) + "' does not match with '" + str(quadruple[1]) + "' Data Type [ " + str(varMemory[quadruple[1]][0]) + " ].\n")
                    sys.exit()
            elif(varMemory[quadruple[1]][0]=="string"):
                varMemory[quadruple[1]][1] = currVal
            PC+=1
        elif(opcode == "==" or opcode == "!=" or opcode == "<" or opcode == ">" or opcode == "<=" or opcode == ">="):
            # Restrict Word Types
            op1 = quadruple[1]
            op2 = quadruple[2]
            if(op1 in avail):
                op1 = avail[op1]
            if(op2 in avail):
                op2 = avail[op2]
            if(op1 in varMemory):
                op1 = varMemory[op1][1]
            if(op2 in varMemory):
                op2 = varMemory[op2][1]
            if(opcode == "==" and (op1 == op2)):
                avail[quadruple[3]] = True
            elif(opcode == "!=" and (op1 != op2)):
                avail[quadruple[3]] = True
            elif(opcode == "<" and (op1 < op2)):
                avail[quadruple[3]] = True
            elif(opcode == ">" and (op1 > op2)):
                avail[quadruple[3]] = True
            elif(opcode == "<=" and (op1 <= op2)):
                avail[quadruple[3]] = True
            elif(opcode == ">=" and (op1 >= op2)):
                avail[quadruple[3]] = True
            else:
                avail[quadruple[3]] = False
            PC+=1
        elif(opcode == "or" or opcode == "and"):
            # Restrict Word Types
            op1 = quadruple[1]
            op2 = quadruple[2]
            if(op1 in avail):
                op1 = avail[op1]
            if(op2 in avail):
                op2 = avail[op2]
            if(op1 in varMemory):
                op1 = varMemory[op1][1]
            if(op2 in varMemory):
                op2 = varMemory[op2][1]
            if(opcode == "or"):
                avail[quadruple[3]] = op1 or op2
            elif(opcode == "and"):
                avail[quadruple[3]] = op1 and op2    
            PC+=1
        elif(opcode == "="):
            op1 = quadruple[1]
            if(op1 in avail):
                op1 = avail[op1]
            if(op1 in varMemory):
                op1 = varMemory[op1][1]
            varMemory[str(quadruple[2])][1] = op1
            PC+=1
        elif(opcode == "+" or opcode == "-" or opcode == "*" or opcode == "/" or opcode == "%"):
            # Restrict Word Types
            op1 = quadruple[1]
            op2 = quadruple[2]
            if(op1 in avail):
                op1 = avail[op1]
            if(op2 in avail):
                op2 = avail[op2]
            if(op1 in varMemory):
                op1 = varMemory[op1][1]
            if(op2 in varMemory):
                op2 = varMemory[op2][1]
            op1 = float(op1)
            op2 = float(op2)
            if(opcode == "+"):
                avail[quadruple[3]] = op1 + op2
            elif(opcode == "-"):
                avail[quadruple[3]] = op1 - op2
            elif(opcode == "*"):
                avail[quadruple[3]] = op1 * op2
            elif(opcode == "/"):
                avail[quadruple[3]] = op1 / op2
            elif(opcode == "%"):
                avail[quadruple[3]] = op1 % op2
            PC+=1
        elif(opcode == "PRINTAPPEND"):
            # Restrict Word Types
            op1 = quadruple[1]
            op2 = quadruple[2]
            if(op1 in avail):
                op1 = (avail[op1])
            if(op2 in avail):
                op2 = (avail[op2])
            if(op1 in varMemory):
                op1 = (varMemory[op1][1])
            if(op2 in varMemory):
                op2 = (varMemory[op2][1])
            if(type(op1)==float and op1.is_integer()):
                op1 = int(op1)
            if(type(op2)==float and op2.is_integer()):
                op2 = int(op2)
            op1 = str(op1)
            op2 = str(op2)
            avail[quadruple[3]] = op1 + op2
            PC+=1
        elif(opcode == "=Vec"):
            assign = quadruple[1]
            offset = quadruple[3]
            if(assign in avail):
                assign = (avail[assign])
            if(assign in varMemory):
                assign = (varMemory[assign][1])
            if(offset in avail):
                offset = (avail[offset])
            if(offset in varMemory):
                offset = (varMemory[offset][1])
            # Missing extract from object Var array
            startPos = objectStart[quadruple[2]][0]
            try:
                offset = float(offset)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[5])+offsetPos) +": Vector Index must be an Integer Value.\n")
                sys.exit()
            if(not(type(offset)==float and offset.is_integer())):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[5])+offsetPos) +": Vector Index must be an Integer Value.\n")
                sys.exit()
            if(offset >= objectStart[quadruple[2]][1] or offset < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[5])+offsetPos) +": Vector Index is Out of Bounds.\n")
                sys.exit()
            posVal = 0
            offset = int(offset)
            startPos = int(startPos)
            try:
                assign = float(assign)
                posVal = "number"
            except ValueError:
                posVal = "string"
            objectVar[startPos+offset][1] = assign
            objectVar[startPos+offset][0] = posVal
            PC+=1
        elif(opcode == "InputVec"):
            assign = 0
            offset = quadruple[2]
            if(offset in avail):
                offset = (avail[offset])
            if(offset in varMemory):
                offset = (varMemory[offset][1])
            # Missing extract from object Var array
            startPos = objectStart[quadruple[1]][0]
            try:
                offset = float(offset)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[4])+offsetPos) +": Vector Index must be an Integer Value.\n")
                sys.exit()
            if(not(type(offset)==float and offset.is_integer())):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[4])+offsetPos) +": Vector Index must be an Integer Value.\n")
                sys.exit()
            if(offset >= objectStart[quadruple[1]][1] or offset < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[4])+offsetPos) +": Vector Index is Out of Bounds.\n")
                sys.exit()
            if(flagSameLine == 1):
                assign = input()
                flagSameLine = 0
            else:
                assign = input("<< ")
            posVal = 0
            offset = int(offset)
            startPos = int(startPos)
            try:
                assign = float(assign)
                posVal = "number"
            except ValueError:
                posVal = "string"
            objectVar[startPos+offset][1] = assign
            objectVar[startPos+offset][0] = posVal
            PC+=1
        elif(opcode == "getVec"):
            offset = quadruple[2]
            if(offset in avail):
                offset = (avail[offset])
            if(offset in varMemory):
                offset = (varMemory[offset][1])
            startPos = objectStart[quadruple[1]][0]
            startPos = int(startPos)
            offset = int(offset)
            avail[quadruple[3]] = objectVar[startPos+offset][1]
            # Error Catching
            startPos = objectStart[quadruple[1]][0]
            try:
                offset = float(offset)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[4])+offsetPos) +": Vector Index must be an Integer Value.\n")
                sys.exit()
            if(not(type(offset)==float and offset.is_integer())):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[4])+offsetPos) +": Vector Index must be an Integer Value.\n")
                sys.exit()
            if(offset >= objectStart[quadruple[1]][1] or offset < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[4])+offsetPos) +": Vector Index is Out of Bounds.\n")
                sys.exit()
            offset = int(offset)
            startPos = int(startPos)
            avail[quadruple[3]] = objectVar[startPos+offset][1]
            PC+=1
        elif(opcode == "=Mat"):
            assign = quadruple[1]
            offsetRen = quadruple[3]
            offsetCol = quadruple[4]
            if(assign in avail):
                assign = (avail[assign])
            if(assign in varMemory):
                assign = (varMemory[assign][1])
            if(offsetRen in avail):
                offsetRen = (avail[offsetRen])
            if(offsetRen in varMemory):
                offsetRen = (varMemory[offsetRen][1])
            if(offsetCol in avail):
                offsetCol = (avail[offsetCol])
            if(offsetCol in varMemory):
                offsetCol = (varMemory[offsetCol][1])
            # Missing extract from object Var array
            startPos = objectStart[quadruple[2]][0]
            try:
                offsetRen = float(offsetRen)
                offsetCol = float(offsetCol)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Matrix Index must be an Integer Value.\n")
                sys.exit()
            if(not((type(offsetRen)==float and offsetRen.is_integer())and(type(offsetCol)==float and offsetCol.is_integer()))):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Matrix Index must be an Integer Value.\n")
                sys.exit()
            if(offsetRen >= objectStart[quadruple[2]][1] or offsetRen < 0 or offsetCol >= objectStart[quadruple[2]][2] or offsetCol < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Matrix Index is Out of Bounds.\n")
                sys.exit()
            posVal = 0
            offsetRen = int(offsetRen)
            offsetCol = int(offsetCol)
            startPos = int(startPos)
            try:
                assign = float(assign)
                posVal = "number"
            except ValueError:
                posVal = "string"
            objectVar[(offsetRen*objectStart[quadruple[2]][2])+offsetCol+startPos][1] = assign
            objectVar[(offsetRen*objectStart[quadruple[2]][2])+offsetCol+startPos][0] = posVal
            PC+=1
        elif(opcode == "InputMat"):
            assign = 0
            offsetRen = quadruple[2]
            offsetCol = quadruple[3]
            if(offsetRen in avail):
                offsetRen = (avail[offsetRen])
            if(offsetRen in varMemory):
                offsetRen = (varMemory[offsetRen][1])
            if(offsetCol in avail):
                offsetCol = (avail[offsetCol])
            if(offsetCol in varMemory):
                offsetCol = (varMemory[offsetCol][1])
            # Missing extract from object Var array
            startPos = objectStart[quadruple[1]][0]
            try:
                offsetRen = float(offsetRen)
                offsetCol = float(offsetCol)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[5])+offsetPos) +": Matrix Index must be an Integer Value.\n")
                sys.exit()
            if(not((type(offsetRen)==float and offsetRen.is_integer())and(type(offsetCol)==float and offsetCol.is_integer()))):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[5])+offsetPos) +": Matrix Index must be an Integer Value.\n")
                sys.exit()
            if(offsetRen >= objectStart[quadruple[1]][1] or offsetRen < 0 or offsetCol >= objectStart[quadruple[1]][2] or offsetCol < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[5])+offsetPos) +": Matrix Index is Out of Bounds.\n")
                sys.exit()
            if(flagSameLine == 1):
                assign = input()
                flagSameLine = 0
            else:
                assign = input("<< ")
            posVal = 0
            offsetRen = int(offsetRen)
            offsetCol = int(offsetCol)
            startPos = int(startPos)
            try:
                assign = float(assign)
                posVal = "number"
            except ValueError:
                posVal = "string"
            objectVar[(offsetRen*objectStart[quadruple[1]][2])+offsetCol+startPos][1] = assign
            objectVar[(offsetRen*objectStart[quadruple[1]][2])+offsetCol+startPos][0] = posVal
            PC+=1
        elif(opcode == "getMat"):
            offsetRen = quadruple[2]
            offsetCol = quadruple[3]
            if(offsetRen in avail):
                offsetRen = (avail[offsetRen])
            if(offsetRen in varMemory):
                offsetRen = (varMemory[offsetRen][1])
            if(offsetCol in avail):
                offsetCol = (avail[offsetCol])
            if(offsetCol in varMemory):
                offsetCol = (varMemory[offsetCol][1])
            startPos = objectStart[quadruple[1]][0]
            startPos = int(startPos)
            offsetRen = int(offsetRen)
            offsetCol = int(offsetCol)
            # Error Catching
            try:
                offsetRen = float(offsetRen)
                offsetCol = float(offsetCol)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Matrix Index must be an Integer Value.\n")
                sys.exit()
            if(not((type(offsetRen)==float and offsetRen.is_integer())and(type(offsetCol)==float and offsetCol.is_integer()))):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Matrix Index must be an Integer Value.\n")
                sys.exit()
            if(offsetRen >= objectStart[quadruple[1]][1] or offsetRen < 0 or offsetCol >= objectStart[quadruple[1]][2] or offsetCol < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Matrix Index is Out of Bounds.\n")
                sys.exit()
            offsetRen = int(offsetRen)
            offsetCol = int(offsetCol)
            startPos = int(startPos)
            avail[quadruple[4]] = objectVar[(offsetRen*objectStart[quadruple[1]][2])+offsetCol+startPos][1]
            PC+=1
        elif(opcode == "=Cube"):
            assign = quadruple[1]
            offsetX = quadruple[3]
            offsetY = quadruple[4]
            offsetZ = quadruple[5]
            if(assign in avail):
                assign = (avail[assign])
            if(assign in varMemory):
                assign = (varMemory[assign][1])
            if(offsetX in avail):
                offsetX = (avail[offsetX])
            if(offsetX in varMemory):
                offsetX = (varMemory[offsetX][1])
            if(offsetY in avail):
                offsetY = (avail[offsetY])
            if(offsetY in varMemory):
                offsetY = (varMemory[offsetY][1])
            if(offsetZ in avail):
                offsetZ = (avail[offsetZ])
            if(offsetZ in varMemory):
                offsetZ = (varMemory[offsetZ][1])
            # Missing extract from object Var array
            startPos = objectStart[quadruple[2]][0]
            try:
                offsetX = float(offsetX)
                offsetY = float(offsetY)
                offsetZ = float(offsetZ)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[7])+offsetPos) +": Cube Index must be an Integer Value.\n")
                sys.exit()
            if(not(((type(offsetX)==float and offsetX.is_integer()))and((type(offsetY)==float and offsetY.is_integer()))and((type(offsetZ)==float and offsetZ.is_integer())))):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[7])+offsetPos) +": Cube Index must be an Integer Value.\n")
                sys.exit()
            if(offsetX >= objectStart[quadruple[2]][1] or offsetX < 0 or offsetY >= objectStart[quadruple[2]][2] or offsetY < 0 or offsetZ >= objectStart[quadruple[2]][3] or offsetZ < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[7])+offsetPos) +": Cube Index is Out of Bounds.\n")
                sys.exit()
            posVal = 0
            offsetX = int(offsetX)
            offsetY = int(offsetY)
            offsetZ = int(offsetZ)
            startPos = int(startPos)
            try:
                assign = float(assign)
                posVal = "number"
            except ValueError:
                posVal = "string"
            Y = objectStart[quadruple[2]][2]
            Z = objectStart[quadruple[2]][3]
            objectVar[offsetX*(Y*Z)+offsetY*Z+offsetZ+startPos][1] = assign
            objectVar[offsetX*(Y*Z)+offsetY*Z+offsetZ+startPos][0] = posVal
            PC+=1
        elif(opcode == "InputCube"):
            assign = 0
            offsetX = quadruple[2]
            offsetY = quadruple[3]
            offsetZ = quadruple[4]
            if(offsetX in avail):
                offsetX = (avail[offsetX])
            if(offsetX in varMemory):
                offsetX = (varMemory[offsetX][1])
            if(offsetY in avail):
                offsetY = (avail[offsetY])
            if(offsetY in varMemory):
                offsetY = (varMemory[offsetY][1])
            if(offsetZ in avail):
                offsetZ = (avail[offsetZ])
            if(offsetZ in varMemory):
                offsetZ = (varMemory[offsetZ][1])
            # Missing extract from object Var array
            startPos = objectStart[quadruple[1]][0]
            try:
                offsetX = float(offsetX)
                offsetY = float(offsetY)
                offsetZ = float(offsetZ)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Cube Index must be an Integer Value.\n")
                sys.exit()
            if(not(((type(offsetX)==float and offsetX.is_integer()))and((type(offsetY)==float and offsetY.is_integer()))and((type(offsetZ)==float and offsetZ.is_integer())))):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Cube Index must be an Integer Value.\n")
                sys.exit()
            if(offsetX >= objectStart[quadruple[1]][1] or offsetX < 0 or offsetY >= objectStart[quadruple[1]][2] or offsetY < 0 or offsetZ >= objectStart[quadruple[1]][3] or offsetZ < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[6])+offsetPos) +": Cube Index is Out of Bounds.\n")
                sys.exit()
            if(flagSameLine == 1):
                assign = input()
                flagSameLine = 0
            else:
                assign = input("<< ")
            posVal = 0
            offsetX = int(offsetX)
            offsetY = int(offsetY)
            offsetZ = int(offsetZ)
            startPos = int(startPos)
            try:
                assign = float(assign)
                posVal = "number"
            except ValueError:
                posVal = "string"
            Y = objectStart[quadruple[1]][2]
            Z = objectStart[quadruple[1]][3]
            objectVar[offsetX*(Y*Z)+offsetY*Z+offsetZ+startPos][1] = assign
            objectVar[offsetX*(Y*Z)+offsetY*Z+offsetZ+startPos][0] = posVal
            PC+=1
        elif(opcode == "getCube"):
            offsetX = quadruple[2]
            offsetY = quadruple[3]
            offsetZ = quadruple[4]
            if(offsetX in avail):
                offsetX = (avail[offsetX])
            if(offsetX in varMemory):
                offsetX = (varMemory[offsetX][1])
            if(offsetY in avail):
                offsetY = (avail[offsetY])
            if(offsetY in varMemory):
                offsetY = (varMemory[offsetY][1])
            if(offsetZ in avail):
                offsetZ = (avail[offsetZ])
            if(offsetZ in varMemory):
                offsetZ = (varMemory[offsetZ][1])
            startPos = objectStart[quadruple[1]][0]
            startPos = int(startPos)
            offsetX = int(offsetX)
            offsetY = int(offsetY)
            offsetZ = int(offsetZ)
            # Error Catching
            try:
                offsetX = float(offsetX)
                offsetY = float(offsetY)
                offsetZ = float(offsetZ)
            except ValueError:
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[7])+offsetPos) +": Cube Index must be an Integer Value.\n")
                sys.exit()
            if(not(((type(offsetX)==float and offsetX.is_integer()))and((type(offsetY)==float and offsetY.is_integer()))and((type(offsetZ)==float and offsetZ.is_integer())))):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[7])+offsetPos) +": Cube Index must be an Integer Value.\n")
                sys.exit()
            if(offsetX >= objectStart[quadruple[1]][1] or offsetX < 0 or offsetY >= objectStart[quadruple[1]][2] or offsetY < 0 or offsetZ >= objectStart[quadruple[1]][3] or offsetZ < 0):
                print("<!> Error in Dynamo Charlotte at line " + str(int(quadruple[7])+offsetPos) +": Cube Index is Out of Bounds.\n")
                sys.exit()
            offsetX = int(offsetX)
            offsetY = int(offsetY)
            offsetZ = int(offsetZ)
            startPos = int(startPos)
            Y = objectStart[quadruple[1]][2]
            Z = objectStart[quadruple[1]][3]
            avail[quadruple[5]] = objectVar[offsetX*(Y*Z)+offsetY*Z+offsetZ+startPos][1]
            PC+=1
    #print("")
    #print("<<< Object Variables >>>\n")
    #print(objectVar)
    #print(objectStart)
    #print(objectPos)

        

# First Quadruple
    
def p_firstQuadruple(t):
    'firstQuadruple : '
    global quadruplesAll
    global cont
    currQuadruple = []
    currQuadruple.append("goto")
    currQuadruple.append(None)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Main Block

def p_dc_compound_program(t):
    '''dc_compound_program           : varDeclaration subprocedures mainblock'''

# Variables Declaration

def p_varDeclaration(t):
    '''varDeclaration       : variables_dc varDeclaration
                            | objectvariables_dc varDeclaration
                            | empty'''

# Subprocedures 

def p_subprocedures(t):
    '''subprocedures         : FUNCTION seen_SubId statements_dc endProcedure RETURN subprocedures
                             | empty'''

# Subprocedures // Seen ID

def p_seen_SubId(t):
    'seen_SubId : ID'
    global subMemory
    global cont
    global offsetPos
    currSub = []
    if((t[1] not in subMemory)):
        subMemory[t[1]] = cont
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Function '" + str(t[1]) + "' has already been declared.\n")
        sys.exit()

# Subprocedures // End Procedure

def p_endProcedure(t):
    'endProcedure : '
    global quadruplesAll
    global cont
    currQuadruple = []
    currQuadruple.append("endprocedure")
    quadruplesAll.append(currQuadruple)
    cont+=1

# Main Program

def p_mainblock(t):
    'mainblock           : MAIN startPosition statements_dc endPosition END'

# Start Position

def p_startPosition(t):
    'startPosition : '
    global cont
    global quadruplesAll
    quadruplesAll[0][1] = cont

def p_endPosition(t):
    'endPosition : '
    global quadruplesAll
    currQuadruple = []
    currQuadruple.append("PROGRAMEND")
    quadruplesAll.append(currQuadruple)

# Statements

def p_statements_dc(t):
    '''statements_dc    : assign_dc statements_dc
						| input_dc statements_dc
                        | print_dc statements_dc
                        | if_dc statements_dc
                        | while_dc statements_dc
                        | dowhile_dc statements_dc
                        | for_dc statements_dc
                        | call_dc statements_dc
                        | unitary_dc statements_dc
                        | binary_dc statements_dc
                        | resize_dc statements_dc
                        | add_dc statements_dc
						| empty '''

# Documentation:
# 1. [Check Official in Dynamo Charlotte Execution Environment for Execution Code]
# 2. [In Object variables save vectors as value / type]
# 3. [Check for Float Value when needed from ID or Object Variable Position in General Expressions]

# ****************************
# ***** Statements Rules *****
# ****************************

# Traditional Variables Declaration

def p_variables_dc(t):
    '''variables_dc		: VAR ID AS NUMBER_KEYWORD
                        | VAR ID AS STRING_KEYWORD'''
    global varMemory
    global varPosition
    global offsetPos
    currVar = []
    if((t[2] not in varMemory)):
        if(t[4]=="number"):
            currVar = [t[4], float(0), varPosition]
        elif(t[4]=="string"):
            currVar = [t[4], str(""), varPosition]
        varMemory[t[2]] = currVar
        varPosition+=1
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(2))+offsetPos) +": Variable '" + str(t[2]) + "' has already been declared.\n")
        sys.exit()

# Object Variables Declaration - Vector

def p_objectvariables_dc_vector(t):
    'objectvariables_dc  : VECTOR_KEYWORD LEFTPAR NUMBER RIGHTPAR ID'
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    vectorSize = t[3]
    try:
        vectorSize = float(vectorSize)
    except ValueError:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(5))+offsetPos) +": Vector Size must be an Integer Value.\n")
        sys.exit()
    if(not(type(vectorSize)==float and vectorSize.is_integer())):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(5))+offsetPos) +": Vector Size must be an Integer Value.\n")
        sys.exit()
    if((t[5] not in objectStart)):
        vectorSize = int(vectorSize)
        currVal = []
        currVal.append(objectPos)
        currVal.append(vectorSize)
        objectStart[t[5]] = currVal
        for i in range(vectorSize):
            currVal = []
            currVal.append("number")
            currVal.append(0)
            objectVar.append(currVal)
            objectPos+=1
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(5))+offsetPos) +": Vector '" + str(t[5]) + "' has already been declared.\n")
        sys.exit()
    
# Object Variables Declaration - Matrix

def p_objectvariables_dc_matrix(t):
    'objectvariables_dc  : MAT_KEYWORD LEFTPAR NUMBER COMMA NUMBER RIGHTPAR ID'
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    matSizeX = t[3]
    matSizeY = t[5]
    try:
        matSizeX = float(matSizeX)
        matSizeY = float(matSizeY)
    except ValueError:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(7))+offsetPos) +": Matrix Size must be an Integer Value.\n")
        sys.exit()
    if(not(((type(matSizeX)==float and matSizeX.is_integer()))and((type(matSizeY)==float and matSizeY.is_integer())))):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(7))+offsetPos) +": Matrix Size must be an Integer Value.\n")
        sys.exit()
    if((t[7] not in objectStart)):
        matSize = int(matSizeX) * int(matSizeY)
        matSize = int(matSize)
        matSizeX = int(matSizeX)
        matSizeY = int(matSizeY)
        currVal = []
        # For Matrix we save size
        currVal.append(objectPos)
        currVal.append(matSizeX)
        currVal.append(matSizeY)
        objectStart[t[7]] = currVal
        for i in range(matSize):
            currVal = []
            currVal.append("number")
            currVal.append(0)
            objectVar.append(currVal)
            objectPos+=1
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(7))+offsetPos) +": Matrix '" + str(t[7]) + "' has already been declared.\n")
        sys.exit()

# Object Variables Declaration - Cube

def p_objectvariables_dc_cube(t):
    'objectvariables_dc  : CUBE_KEYWORD LEFTPAR NUMBER COMMA NUMBER COMMA NUMBER RIGHTPAR ID'
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    cubeSizeX = t[3]
    cubeSizeY = t[5]
    cubeSizeZ = t[7]
    try:
        cubeSizeX = float(cubeSizeX)
        cubeSizeY = float(cubeSizeY)
        cubeSizeZ = float(cubeSizeZ)
    except ValueError:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(9))+offsetPos) +": Cube Size must be an Integer Value.\n")
        sys.exit()
    if(not(((type(cubeSizeX)==float and cubeSizeX.is_integer()))and((type(cubeSizeY)==float and cubeSizeY.is_integer()))and((type(cubeSizeZ)==float and cubeSizeZ.is_integer())))):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(9))+offsetPos) +": Cube Size must be an Integer Value.\n")
        sys.exit()
    if((t[9] not in objectStart)):
        cubeSize = int(cubeSizeX) * int(cubeSizeY) * int(cubeSizeZ)
        cubeSize = int(cubeSize)
        cubeSizeX = int(cubeSizeX)
        cubeSizeY = int(cubeSizeY)
        cubeSizeZ = int(cubeSizeZ)
        currVal = []
        # For Matrix we save size
        currVal.append(objectPos)
        currVal.append(cubeSizeX)
        currVal.append(cubeSizeY)
        currVal.append(cubeSizeZ)
        objectStart[t[9]] = currVal
        for i in range(cubeSize):
            currVal = []
            currVal.append("number")
            currVal.append(0)
            objectVar.append(currVal)
            objectPos+=1
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(9))+offsetPos) +": Cube '" + str(t[9]) + "' has already been declared.\n")
        sys.exit()

# Traditional Variables Assignment

def p_assign_dc_id(t):
    'assign_dc  : ID EQUALS generalexpression'
    global operands
    global avail
    global quadruplesAll
    global varMemory
    global cont
    global availSet
    global offsetPos
    if(t[1] not in varMemory):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    opDet = t[3]
    lastOperand = operands.pop()
    currVal = lastOperand
    if((varMemory[t[1]][0]=="number" and not(opDet=="arithmetic")) or (varMemory[t[1]][0]=="string" and not(opDet=="string"))):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Assignment '" + str(currVal) + "' does not match with '" + str(t[1]) + "' Data Type [ " + str(varMemory[t[1]][0]) + " ].\n")
        sys.exit()
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Vector Position Assignment

def p_assign_dc_vector(t):
    'assign_dc  : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET EQUALS generalexpression'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    assignOperand = operands.pop()
    offsetOperand = operands.pop()
    offset = offsetOperand
    assign = assignOperand
    if(assignOperand in avail):
        availSet.append(assignOperand)
        avail[assignOperand] = None
    if(offsetOperand in avail):
        availSet.append(offsetOperand)
        avail[offsetOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Vector '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("=Vec")
    currQuadruple.append(assign)
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offset)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Matrix Position Assignment - Will need to have mid-grammars for various arithmetic expressions

def p_assign_dc_mat(t):
    'assign_dc  : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET EQUALS generalexpression'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    assignOperand = operands.pop()
    offsetColOperand = operands.pop()
    offsetRenOperand = operands.pop()
    offsetRen = offsetRenOperand
    offsetCol = offsetColOperand
    assign = assignOperand
    if(assignOperand in avail):
        availSet.append(assignOperand)
        avail[assignOperand] = None
    if(offsetRenOperand in avail):
        availSet.append(offsetRenOperand)
        avail[offsetRenOperand] = None
    if(offsetColOperand in avail):
        availSet.append(offsetColOperand)
        avail[offsetColOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Matrix '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("=Mat")
    currQuadruple.append(assign)
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetRen)
    currQuadruple.append(offsetCol)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    quadruplesAll.append(currQuadruple)
    cont+=1
    

# Cube Position Assignment - Will need to have mid-grammars for various arithmetic expressions

def p_assign_dc_cube(t):
    'assign_dc  : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET EQUALS generalexpression'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    assignOperand = operands.pop()
    offsetZOperand = operands.pop()
    offsetYOperand = operands.pop()
    offsetXOperand = operands.pop()
    offsetX = offsetXOperand
    offsetY = offsetYOperand
    offsetZ = offsetZOperand
    assign = assignOperand
    if(assignOperand in avail):
        availSet.append(assignOperand)
        avail[assignOperand] = None
    if(offsetXOperand in avail):
        availSet.append(offsetXOperand)
        avail[offsetXOperand] = None
    if(offsetYOperand in avail):
        availSet.append(offsetYOperand)
        avail[offsetYOperand] = None
    if(offsetZOperand in avail):
        availSet.append(offsetZOperand)
        avail[offsetZOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Cube '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("=Cube")
    currQuadruple.append(assign)
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetX)
    currQuadruple.append(offsetY)
    currQuadruple.append(offsetZ)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Traditional Variables Input

def p_input_dc_id(t):
    'input_dc           : INPUT LEFTPAR ID RIGHTPAR'
    global quadruplesAll
    global cont
    global varMemory
    global offsetPos
    if(not(t[3] not in varMemory)):
        currQuadruple = []
        currQuadruple.append("INPUT")
        currQuadruple.append(str(t[3]))
        quadruplesAll.append(currQuadruple)
        cont+=1
    else:
        print("\n<!> Error in Dynamo Charlotte at line " +str(int(t.lineno(3))+offsetPos) +": Variable '" + str(t[3]) + "' does not exist.\n")
        sys.exit()

# Vector Position Input

def p_input_dc_vector(t):
    'input_dc  : INPUT LEFTPAR ID LEFTBRACKET arithmeticexpression RIGHTBRACKET RIGHTPAR'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetOperand = operands.pop()
    offset = offsetOperand
    if(offsetOperand in avail):
        availSet.append(offsetOperand)
        avail[offsetOperand] = None
    if(t[3] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(3))+offsetPos) +": Vector '" + str(t[3]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("InputVec")
    currQuadruple.append(str(t[3]))
    currQuadruple.append(offset)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(3)))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Matrix Position Input

def p_input_dc_mat(t):
    'input_dc           : INPUT LEFTPAR ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET RIGHTPAR'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetColOperand = operands.pop()
    offsetRenOperand = operands.pop()
    offsetRen = offsetRenOperand
    offsetCol = offsetColOperand
    if(offsetRenOperand in avail):
        availSet.append(offsetRenOperand)
        avail[offsetRenOperand] = None
    if(offsetColOperand in avail):
        availSet.append(offsetColOperand)
        avail[offsetColOperand] = None
    if(t[3] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(3))+offsetPos) +": Matrix '" + str(t[3]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("InputMat")
    currQuadruple.append(str(t[3]))
    currQuadruple.append(offsetRen)
    currQuadruple.append(offsetCol)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(3)))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Cube Position Input

def p_input_dc_cube(t):
    'input_dc           : INPUT LEFTPAR ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET RIGHTPAR'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetZOperand = operands.pop()
    offsetYOperand = operands.pop()
    offsetXOperand = operands.pop()
    offsetX = offsetXOperand
    offsetY = offsetYOperand
    offsetZ = offsetZOperand
    if(offsetXOperand in avail):
        availSet.append(offsetXOperand)
        avail[offsetXOperand] = None
    if(offsetYOperand in avail):
        availSet.append(offsetYOperand)
        avail[offsetYOperand] = None
    if(offsetZOperand in avail):
        availSet.append(offsetZOperand)
        avail[offsetZOperand] = None
    if(t[3] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(3))+offsetPos) +": Cube '" + str(t[3]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("InputCube")
    currQuadruple.append(str(t[3]))
    currQuadruple.append(offsetX)
    currQuadruple.append(offsetY)
    currQuadruple.append(offsetZ)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(3)))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Print in Same Line - General Expression

def p_print_dc_sameline(t):
    'print_dc  : PRINTLN LEFTPAR printarithmetic RIGHTPAR'
    global operands
    global avail
    global quadruplesAll
    global cont
    global availSet
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("PRINTLN")
    currQuadruple.append(currVal)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Print with Endl - General Expression

def p_print_dc_generalexpression(t):
    'print_dc  : PRINT LEFTPAR printarithmetic RIGHTPAR'
    global operands
    global avail
    global quadruplesAll
    global cont
    global availSet
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("PRINT")
    currQuadruple.append(currVal)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Print Expression

def p_printarithmetic_quadruple(t):
    'printarithmetic : printarithmetic PLUS printarithmetic'
    currQuadruple = []
    global avail
    global operands
    global quadruplesArithmeticLocal
    global quadruplesAll
    global cont
    global availSet
    currQuadruple.append("PRINTAPPEND")
    currRes = availSet.pop(0)
    firstOp = operands.pop()
    # The following commented code is to get the value from the Temporal
    if(firstOp in avail):
        availSet.append(firstOp)
        avail[firstOp] = None
    secondOp = operands.pop()
    if(secondOp in avail):
        availSet.append(secondOp)
        avail[secondOp] = None
    currQuadruple.append(secondOp)
    currQuadruple.append(firstOp)
    operands.append(currRes)
    currQuadruple.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

def p_printarithmetic_id(t):
    'printarithmetic  : ID'
    global operands
    global varMemory
    global offsetPos
    if(not(t[1] not in varMemory)):
        operands.append(str(t[1]))
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit() 

def p_printarithmetic_value(t):
    '''printarithmetic    : NUMBER'''
    global operands
    operands.append(float(t[1]))

def p_printarithmetic_word(t):
    'printarithmetic      : STRING'
    global operands
    operands.append(str(t[1]))

def p_printarithmetic_vector(t):
    'printarithmetic      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetOperand = operands.pop()
    offset = offsetOperand
    if(offsetOperand in avail):
        availSet.append(offsetOperand)
        avail[offsetOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Vector '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getVec")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offset)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

def p_printarithmetic_mat(t):
    'printarithmetic      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetColOperand = operands.pop()
    offsetRenOperand = operands.pop()
    offsetRen = offsetRenOperand
    offsetCol = offsetColOperand
    if(offsetColOperand in avail):
        availSet.append(offsetColOperand)
        avail[offsetColOperand] = None
    if(offsetRenOperand in avail):
        availSet.append(offsetRenOperand)
        avail[offsetRenOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Matrix '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getMat")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetRen)
    currQuadruple.append(offsetCol)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

def p_printarithmetic_cube(t):
    'printarithmetic      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetZOperand = operands.pop()
    offsetYOperand = operands.pop()
    offsetXOperand = operands.pop()
    offsetX = offsetXOperand
    offsetY = offsetYOperand
    offsetZ = offsetZOperand
    if(offsetXOperand in avail):
        availSet.append(offsetXOperand)
        avail[offsetXOperand] = None
    if(offsetYOperand in avail):
        availSet.append(offsetYOperand)
        avail[offsetYOperand] = None
    if(offsetZOperand in avail):
        availSet.append(offsetZOperand)
        avail[offsetZOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Cube '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getCube")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetX)
    currQuadruple.append(offsetY)
    currQuadruple.append(offsetZ)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Print - Endl

def p_print_dc_(t):
    'print_dc  : PRINT LEFTPAR ENDL RIGHTPAR'
    global quadruplesAll
    global cont
    currQuadruple = []
    currQuadruple.append("PRINTENDL")
    quadruplesAll.append(currQuadruple)
    cont+=1

# If Statement - If Part

def p_if_dc(t):
    'if_dc              : IF LEFTPAR logicresult seen_LogicResultIf RIGHTPAR statements_dc if_elsepart seen_IfEnd ENDIF' 

# If Statement // Seen Logic Result

def p_seen_LogicResultIf(t):
    'seen_LogicResultIf : '
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("gotoF")
    currQuadruple.append(currVal)
    currQuadruple.append(None)
    quadruplesAll.append(currQuadruple)
    cont+=1
    jumpstack.append(cont-1)

# If Statement - Else Part

def p_if_elsepart(t):
    '''if_elsepart      : ELSE seen_Else statements_dc
                        | empty'''

# If Statement // Seen Else

def p_seen_Else(t):
    'seen_Else : '
    global quadruplesAll
    global cont
    global jumpstack
    currAddress = jumpstack.pop()
    fillQuadruple = quadruplesAll[currAddress]
    if(fillQuadruple[0] == "gotoF"):
        fillQuadruple[2] = cont+1
    else:
        fillQuadruple[1] = cont+1
    currQuadruple = []
    currQuadruple.append("goto")
    currQuadruple.append(None)
    quadruplesAll.append(currQuadruple)
    cont+=1
    jumpstack.append(cont-1)

# If Statement // Seen If End

def p_seen_IfEnd(t):
    'seen_IfEnd : '
    global quadruplesAll
    global cont
    global jumpstack
    currAddress = jumpstack.pop()
    fillQuadruple = quadruplesAll[currAddress]
    if(fillQuadruple[0] == "gotoF"):
        fillQuadruple[2] = cont
    else:
        fillQuadruple[1] = cont

# While Statement

def p_while_dc(t):
    'while_dc           : WHILE seen_While LEFTPAR logicresult seen_LogicResultWhile RIGHTPAR statements_dc seen_WhileEnd WEND'

# While Statement // Seen While

def p_seen_While(t):
    'seen_While : '
    global jumpstack
    global cont
    jumpstack.append(cont)

# While Statement // Seen Logic Result

def p_seen_LogicResultWhile(t):
    'seen_LogicResultWhile : '
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("gotoF")
    currQuadruple.append(currVal)
    currQuadruple.append(None)
    quadruplesAll.append(currQuadruple)
    cont+=1
    jumpstack.append(cont-1)

# While Statement // Seen While End

def p_seen_WhileEnd(t):
    'seen_WhileEnd : '
    global jumpstack
    global cont
    global quadruplesAll
    address1 = jumpstack.pop()
    address2 = jumpstack.pop()
    fillQuadruple = quadruplesAll[address1]
    if(fillQuadruple[0] == "gotoF"):
        fillQuadruple[2] = cont+1
    else:
        fillQuadruple[1] = cont+1
    currQuadruple = []
    currQuadruple.append("goto")
    currQuadruple.append(address2)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Do While Statement

def p_dowhile_dc(t):
    'dowhile_dc         : DO seen_Do statements_dc LOOPWHILE LEFTPAR logicresult seen_LogicResultDoWhile RIGHTPAR'

# Do While Statement // Seen Do

def p_seen_Do(t):
    'seen_Do : '
    global jumpstack
    global cont
    jumpstack.append(cont)

# Do While Statement // Seen Logic Result

def p_seen_LogicResultDoWhile(t):
    'seen_LogicResultDoWhile : '
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    address = jumpstack.pop()
    currQuadruple = []
    currQuadruple.append("gotoT")
    currQuadruple.append(currVal)
    currQuadruple.append(address)
    quadruplesAll.append(currQuadruple)
    cont+=1


# For Statement

def p_for_dc(t):
    'for_dc             : FOR seen_ID EQUALS arithmeticexpression seen_AE1 TO arithmeticexpression seen_AE2 statements_dc seen_Next NEXT'

# For Statement // Seen ID

def p_seen_ID(t):
    'seen_ID : ID'
    global operands
    global varMemory
    global offsetPos
    if(not(t[1] not in varMemory)):
        operands.append(str(t[1]))
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit()

# For Statement // Seen AE1

def p_seen_AE1(t):
    'seen_AE1 : '
    global operands
    global quadruplesAll
    global cont
    global avail
    global availSet
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    finalID = operands.pop()
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(finalID)
    quadruplesAll.append(currQuadruple)
    cont+=1
    operands.append(finalID)

# For Statement // Seen AE2

def p_seen_AE2(t):
    'seen_AE2 : '
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    finalID = operands.pop()
    currQuadruple = []
    currQuadruple.append("<=")
    currQuadruple.append(finalID)
    currQuadruple.append(currVal)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    jumpstack.append(cont-1)
    currQuadruple = []
    currQuadruple.append("gotoF")
    currQuadruple.append(currVal)
    currQuadruple.append(None)
    quadruplesAll.append(currQuadruple)
    cont+=1
    jumpstack.append(cont-1)

# For Statement // Seen Next

def p_seen_Next(t):
    'seen_Next : '
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    address1 = jumpstack.pop()
    address2 = jumpstack.pop()
    currQuadruple = []
    currQuadruple.append("+")
    currQuadruple.append(quadruplesAll[address2][1])
    currQuadruple.append(1)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(quadruplesAll[address2][1])
    quadruplesAll.append(currQuadruple)
    cont+=1
    fillQuadruple = quadruplesAll[address1]
    if(fillQuadruple[0] == "gotoF"):
        fillQuadruple[2] = cont+1
    else:
        fillQuadruple[1] = cont+1
    currQuadruple = []
    currQuadruple.append("goto")
    currQuadruple.append(address2)
    quadruplesAll.append(currQuadruple)
    cont+=1


# Go Subprocedure

def p_call_dc(t):
    'call_dc           : CALL ID'
    global quadruplesAll
    global cont
    global subMemory
    global offsetPos
    currQuadruple = []
    if((t[2] in subMemory)):
        currQuadruple.append("CALL")
        currQuadruple.append(subMemory[t[2]])
        quadruplesAll.append(currQuadruple)
        cont+=1
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(2))+offsetPos) +": Function '" + str(t[2]) + "' does not exist.\n")
        sys.exit()

# Unitary Operation - Add 1

def p_unitary_dc_add(t):
    'unitary_dc : ID PLUS PLUS'
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    currQuadruple = []
    currQuadruple.append("+")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(1)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Unitary Operation - Substract 1

def p_unitary_dc_sub(t):
    'unitary_dc : ID MINUS MINUS'
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    currQuadruple = []
    currQuadruple.append("-")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(1)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Binary Operation - Add Equal Number

def p_binary_dc_addequalNumber(t):
    'binary_dc : ID PLUS EQUALS arithmeticexpression'
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    global varMemory
    global offsetPos
    if(t[1] not in varMemory):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    if(varMemory[t[1]][0]=="string"):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Assignment does not match with '" + str(t[1]) + "' Data Type [ " + str(varMemory[t[1]][0]) + " ].\n")
        sys.exit()
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("+")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(currVal)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Binary Operation - Substract Equal Number

def p_binary_dc_subequalNumber(t):
    'binary_dc : ID MINUS EQUALS arithmeticexpression'
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    global varMemory
    global offsetPos
    if(t[1] not in varMemory):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    if(varMemory[t[1]][0]=="string"):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Assignment does not match with '" + str(t[1]) + "' Data Type [ " + str(varMemory[t[1]][0]) + " ].\n")
        sys.exit()
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("-")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(currVal)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Binary Operation - Multiply Equal Number

def p_binary_dc_multequalNumber(t):
    'binary_dc : ID MULTIPLY EQUALS arithmeticexpression'
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    global varMemory
    global offsetPos
    if(t[1] not in varMemory):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    if(varMemory[t[1]][0]=="string"):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Assignment does not match with '" + str(t[1]) + "' Data Type [ " + str(varMemory[t[1]][0]) + " ].\n")
        sys.exit()
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("*")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(currVal)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Binary Operation - Divide Equal Number

def p_binary_dc_divequalNumber(t):
    'binary_dc : ID DIVIDE EQUALS arithmeticexpression'
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    global varMemory
    global offsetPos
    if(t[1] not in varMemory):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    if(varMemory[t[1]][0]=="string"):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Assignment does not match with '" + str(t[1]) + "' Data Type [ " + str(varMemory[t[1]][0]) + " ].\n")
        sys.exit()
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("/")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(currVal)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Binary Operation - Modulo Equal Number

def p_binary_dc_moduloequalNumber(t):
    'binary_dc : ID MODULO EQUALS arithmeticexpression'
    global jumpstack
    global cont
    global quadruplesAll
    global avail
    global availSet
    global operands
    global varMemory
    global offsetPos
    if(t[1] not in varMemory):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    if(varMemory[t[1]][0]=="string"):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Assignment does not match with '" + str(t[1]) + "' Data Type [ " + str(varMemory[t[1]][0]) + " ].\n")
        sys.exit()
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    currQuadruple = []
    currQuadruple.append("%")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(currVal)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    operands.append(currRes)
    lastOperand = operands.pop()
    currVal = lastOperand
    if(lastOperand in avail):
        availSet.append(lastOperand)
        avail[lastOperand] = None
    quadruplesAll.append(currQuadruple)
    cont+=1
    currQuadruple = []
    currQuadruple.append("=")
    currQuadruple.append(currVal)
    currQuadruple.append(str(t[1]))
    quadruplesAll.append(currQuadruple)
    cont+=1

# Vector Resize

def p_vectorresize(t):
    'resize_dc          : ID DOT RESIZE LEFTPAR arithmeticexpression RIGHTPAR'

# Matrix Resize

def p_matresize(t):
    'resize_dc            : ID DOT RESIZE LEFTPAR arithmeticexpression COMMA arithmeticexpression RIGHTPAR'

# Cube Resize

def p_cuberesize(t):
    'resize_dc            : ID DOT RESIZE LEFTPAR arithmeticexpression COMMA arithmeticexpression COMMA arithmeticexpression RIGHTPAR'

# Vector Add

def p_add(t):
    'add_dc                   : ID DOT ADD LEFTPAR generalexpression RIGHTPAR'

# Matrix Add Row

def p_addrow(t):
    'add_dc                : ID DOT ADDROW LEFTPAR RIGHTPAR'

# Matrix Add Col

def p_addcol(t):
    'add_dc                : ID DOT ADDCOL LEFTPAR RIGHTPAR'

# Cube Add X

def p_addx(t):
    'add_dc                  : ID DOT ADDX LEFTPAR RIGHTPAR'

# Cube Add Y

def p_addy(t):
    'add_dc                  : ID DOT ADDY LEFTPAR RIGHTPAR'

# Cube Add Z

def p_addz(t):
    'add_dc                  : ID DOT ADDZ LEFTPAR RIGHTPAR'

# ****************************
# *** Sub-Statements Rules ***
# ****************************

# General Expression (Arithmetic Expression)

def p_generalexpression_arithmeticexpression(t):
    'generalexpression      : arithmeticexpression'
    t[0] = "arithmetic"
    # Here is where the execution is done by analyzing all the generated
    # expressions in the Quadruples List, and then sending the last Avail
    # back to the Avail List.

    # Important: Ask if you can stop using T's and instead just use simple values
    # and return simple values instead of those T's

# General Expression (Word Expression)

def p_generalexpression_word(t):
    'generalexpression      : STRING'
    global operands
    operands.append(str(t[1]))
    t[0] = "string"


# Arithmetic Expression - Arithmetic Operations

def p_arithmeticexpression(t):
    '''arithmeticexpression : arithmeticexpression PLUS arithmeticexpression
                            | arithmeticexpression MINUS arithmeticexpression
                            | arithmeticexpression MULTIPLY arithmeticexpression
                            | arithmeticexpression DIVIDE arithmeticexpression
                            | arithmeticexpression MODULO arithmeticexpression'''
    currQuadruple = []
    global avail
    global operands
    global quadruplesArithmeticLocal
    global quadruplesAll
    global cont
    global availSet
    currQuadruple.append(str(t[2]))
    currRes = availSet.pop(0)
    firstOp = operands.pop()

    # The following commented code is to get the value from the Temporal

    if(firstOp in avail):
        availSet.append(firstOp)
        avail[firstOp] = None
        
    secondOp = operands.pop()

    if(secondOp in avail):
        availSet.append(secondOp)
        avail[secondOp] = None

    currQuadruple.append(secondOp)
    currQuadruple.append(firstOp)
    operands.append(currRes)
    currQuadruple.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# *Arithmetic Expression - Float or Word Value. *(Can be used in Print or Assign Statement for Word Variables)

def p_arithmeticexpression_id(t):
    'arithmeticexpression  : ID'
    global operands
    global varMemory
    global offsetPos
    if(not(t[1] not in varMemory)):
        operands.append(str(t[1]))
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit() 

# Arithmetic Expression - Grouping

def p_arithmeticexpression_grouping(t):
    'arithmeticexpression : LEFTPAR arithmeticexpression RIGHTPAR'

# Arithmetic Expression - Float Value 

def p_arithmeticexpression_value(t):
    '''arithmeticexpression    : NUMBER'''
    global operands
    operands.append(float(t[1]))

# Arithmetic Expression - Vector Position Value // Missing Retrieval for Quadruple

def p_arithmeticexpression_vector(t):
    'arithmeticexpression      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetOperand = operands.pop()
    offset = offsetOperand
    if(offsetOperand in avail):
        availSet.append(offsetOperand)
        avail[offsetOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Vector '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getVec")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offset)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Arithmetic Expression - Matrix Position Value // Missing Retrieval for Quadruple

def p_arithmeticexpression_mat(t):
    'arithmeticexpression      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetColOperand = operands.pop()
    offsetRenOperand = operands.pop()
    offsetRen = offsetRenOperand
    offsetCol = offsetColOperand
    if(offsetColOperand in avail):
        availSet.append(offsetColOperand)
        avail[offsetColOperand] = None
    if(offsetRenOperand in avail):
        availSet.append(offsetRenOperand)
        avail[offsetRenOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Matrix '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getMat")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetRen)
    currQuadruple.append(offsetCol)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Arithmetic Expression - Cube Position Value // Missing Retrieval for Quadruple

def p_arithmeticexpression_cube(t):
    'arithmeticexpression      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetZOperand = operands.pop()
    offsetYOperand = operands.pop()
    offsetXOperand = operands.pop()
    offsetX = offsetXOperand
    offsetY = offsetYOperand
    offsetZ = offsetZOperand
    if(offsetXOperand in avail):
        availSet.append(offsetXOperand)
        avail[offsetXOperand] = None
    if(offsetYOperand in avail):
        availSet.append(offsetYOperand)
        avail[offsetYOperand] = None
    if(offsetZOperand in avail):
        availSet.append(offsetZOperand)
        avail[offsetZOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Cube '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getCube")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetX)
    currQuadruple.append(offsetY)
    currQuadruple.append(offsetZ)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Logic Result (Intermediary for Logic Expression in order to get the Result)

def p_logicresult(t):
    'logicresult           : logicexpression'

    # Here is where the execution is done by analyzing all the generated
    # expressions in the Quadruples List, and then sending the last Avail
    # back to the Avail List.

    # Important: Ask if you can stop using T's and instead just use simple values
    # and return simple values instead of those T's

# Logic Expression - And / Or

def p_logicexpression_and_or(t):
    '''logicexpression     : logicexpression AND logicexpression
                           | logicexpression OR logicexpression'''
    currQuadruple = []
    global avail
    global operands
    global quadruplesLogicLocal
    global quadruplesAll
    global cont
    global availSet
    currQuadruple.append(str(t[2]))
    currRes = availSet.pop(0)
    firstOp = operands.pop()

    # The following commented code is to get the value from the Temporal

    if(firstOp in avail):
        availSet.append(firstOp)
        avail[firstOp] = None
        
    secondOp = operands.pop()

    if(secondOp in avail):
        availSet.append(secondOp)
        avail[secondOp] = None

    currQuadruple.append(secondOp)
    currQuadruple.append(firstOp)
    operands.append(currRes)
    currQuadruple.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Logic Expression - Grouping

def p_logicexpression_grouping(t):
    'logicexpression   : LEFTPAR logicexpression RIGHTPAR'

# Logic Expression - Arithmetic Logic

def p_logicexpression(t):
    '''logicexpression : logicOption SAME logicOption
                          | logicOption DIFFERENT logicOption
                          | logicOption GREATERTHAN logicOption
                          | logicOption LESSTHAN logicOption
                          | logicOption GREATEREQUAL logicOption
                          | logicOption LESSEQUAL logicOption'''
    currQuadruple = []
    global avail
    global operands
    global quadruplesLogicLocal
    global quadruplesAll
    global cont
    global availSet
    currQuadruple.append(str(t[2]))
    currRes = availSet.pop(0)
    firstOp = operands.pop()

    # The following commented code is to get the value from the Temporal

    if(firstOp in avail):
        availSet.append(firstOp)
        avail[firstOp] = None
        
    secondOp = operands.pop()

    if(secondOp in avail):
        availSet.append(secondOp)
        avail[secondOp] = None

    currQuadruple.append(secondOp)
    currQuadruple.append(firstOp)
    operands.append(currRes)
    currQuadruple.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Logic Option - ID // Missing Vector, Matrix and Cube Positions 

def p_logicOption_ID(t):
    'logicOption   :    ID'
    global operands
    global varMemory
    global offsetPos
    if(not(t[1] not in varMemory)):
        operands.append(str(t[1]))
    else:
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Variable '" + str(t[1]) + "' does not exist.\n")
        sys.exit() 

def p_logicOption_Vector(t):
    'logicOption      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetOperand = operands.pop()
    offset = offsetOperand
    if(offsetOperand in avail):
        availSet.append(offsetOperand)
        avail[offsetOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Vector '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getVec")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offset)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1    

def p_logicOption_Mat(t):
    'logicOption      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetColOperand = operands.pop()
    offsetRenOperand = operands.pop()
    offsetRen = offsetRenOperand
    offsetCol = offsetColOperand
    if(offsetColOperand in avail):
        availSet.append(offsetColOperand)
        avail[offsetColOperand] = None
    if(offsetRenOperand in avail):
        availSet.append(offsetRenOperand)
        avail[offsetRenOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Matrix '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getMat")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetRen)
    currQuadruple.append(offsetCol)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

def p_logicOption_Cube(t):
    'logicOption      : ID LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET LEFTBRACKET arithmeticexpression RIGHTBRACKET'
    global operands
    global quadruplesAll
    global cont
    global jumpstack
    global avail
    global availSet
    global objectVar
    global objectPos
    global objectStart
    global offsetPos
    offsetZOperand = operands.pop()
    offsetYOperand = operands.pop()
    offsetXOperand = operands.pop()
    offsetX = offsetXOperand
    offsetY = offsetYOperand
    offsetZ = offsetZOperand
    if(offsetXOperand in avail):
        availSet.append(offsetXOperand)
        avail[offsetXOperand] = None
    if(offsetYOperand in avail):
        availSet.append(offsetYOperand)
        avail[offsetYOperand] = None
    if(offsetZOperand in avail):
        availSet.append(offsetZOperand)
        avail[offsetZOperand] = None
    if(t[1] not in objectStart):
        print("\n<!> Error in Dynamo Charlotte at line " + str(int(t.lineno(1))+offsetPos) +": Cube '" + str(t[1]) + "' does not exist.\n")
        sys.exit()
    currQuadruple = []
    currQuadruple.append("getCube")
    currQuadruple.append(str(t[1]))
    currQuadruple.append(offsetX)
    currQuadruple.append(offsetY)
    currQuadruple.append(offsetZ)
    currRes = availSet.pop(0)
    currQuadruple.append(currRes)
    currQuadruple.append("LineAt:")
    currQuadruple.append(str(t.lineno(1)))
    operands.append(currRes)
    quadruplesAll.append(currQuadruple)
    cont+=1

# Logic Option - Float 

def p_logicOption_Float(t):
    'logicOption :  NUMBER'
    global operands
    operands.append(float(t[1]))

# Logic Option - Word 

def p_logicOption_Word(t):
    'logicOption :  STRING'
    global operands
    operands.append(str(t[1]))

# Logic Option - Grouping (Not Necessary)

def p_logicOption_grouping(t):
    'logicOption   : LEFTPAR logicOption RIGHTPAR'

# ****************************
# ****** Default Rules *******
# ****************************

# Syntax Error

def p_error(t):
    global gio
    gio = True
    if(t is not None):
        print("\n<!> Error in Dynamo Charlotte: Syntax Error at '%s'.\n" % t.value)
    else:
        print("\n<!> Error in Dynamo Charlotte: Syntax Error.\n")
    sys.exit()

# Empty Rule

def p_empty(t):
	'''
	empty : 
	'''
	t[0] = None

parser = yacc.yacc()

# ___________________MAIN____________________

def run(data):
    global offsetPos
    global quadruplesAll
    caller = getframeinfo(stack()[1][0]) 
    offsetPos = caller.lineno - 1
    if(data != ""):
        parser.parse(data)
    if(len(quadruplesAll) <= 2): 
        print("<?> Feeling lost? Find Dynamo Charlotte Code Examples at https://github.com/JC-Juarez/dynamocharlotte/tree/main/Code%20Examples")
    print("")


