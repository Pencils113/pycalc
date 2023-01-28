"""
===============================================================================
ENGR 13000 Fall 2022

Program Description
    Calculator, interface in console, constantly accepts user input, cleans it, interprets it, and outputs the result.
    Several defined functions exist in a library sorted by math subject. 

Assignment Information
    Assignment:     Proj 4
    Author:         Rohan Ojha, ojhar@purdue.edu
    Team ID:        18

ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""
import math
from evaluateExpression import evaluateExpression


def main():
    
    print("Welcome to PyCalc")
    print("Follow the printed instructions to navigate menus")
    
    printInstructions()
    userInput = ''
    
    while userInput.lower()!='exit': #terminates code when exit is inputted
        userInput = input("\n> ")
        if userInput.strip() == '0' or userInput.lower().strip() == 'help': #if elif else structure divies up submenu code
            printInstructions()
        elif userInput.strip() == '1':
            calculus(userInput)
            printInstructions() #once calculus code is run, reprints instructons when submenu is exited
        elif userInput.strip() == '2':
            linAlg(userInput)
            printInstructions() #once linAlg code is run, reprints instructons when submenu is exited
        elif userInput.strip() == '3':
            complexAnalysis(userInput)
            printInstructions() #once complex code is run, reprints instructons when submenu is exited
        else:
            print(evaluateExpression(cleanInput(userInput.lower()))) #if not otherwise recognized as menu navigation, evaluates input
        
        
        
def printInstructions(): #prints general menu instructions
    print("\n< Main Menu Instructions:\n")
    print("< Enter 0 or 'help' to print these instructions")
    print("< Enter 1 for Calc I, II, or III features")
    print("< Enter 2 for Linear Algebra features")
    print("< Enter 3 for Complex Analysis features")
    print("< Enter 'exit' to leave")
    
def calculusInstructions(): #prints calculus menu instructions
    print("\n< Calculus:\n")
    print("< Enter 0 or 'help' to print these instructions")
    print("< Enter 1 to calculate a limit")
    print("< Enter 2 to calculate a derivative")
    print("< Enter 3 to calculate an integral")
    print("< Enter 'exit' to return to main menu")

def linAlgInstructions(): #prints linear algebra menu instructions
    print("\n< Linear Algebra:\n")
    print("< Enter 0 or 'help' to print these instructions")
    print("< Enter 1 to reduce to REF and RREF")
    print("< Enter 2 to find a determinant")
    print("< Enter 3 to perform matrix multiplication")
    print("< Enter 'exit' to return to main menu")

def complexInstructions(): #prints complex menu instructions
    print("\n< Complex Analysis:\n")
    print("< Enter 0 or 'help' to print these instructions")
    print("< Enter 1 to caculate modulus")
    print("< Enter 2 to obtain exponential form")
    print("< Enter any expression involving complex numbers")
    print("< Enter 'exit' to return to main menu")

def calculus(userInput):
    calculusInstructions() #prints instructions
    while userInput.lower()!='exit':
        userInput = input("\n> ")
        if userInput.strip() == '0' or userInput.lower().strip() == 'help': #prints instructions
            calculusInstructions()
        elif userInput.strip() == '1':
            print(". Limit")
            f = cleanInput(input(". Enter function of one variable: ")) #obtain and clean necessary user input
            x = input(". Enter function variable (e.g. 'x', 't'): ")
            n = cleanInput(input(f". Enter number which {x} appproaches: "))
            output = lim(x, n, f)
            if type(output) == str: #needed since derivative could output string, and isnan causes errors for strings. 
                print(f"< {output}")
            elif math.isnan(output): #""
                print("< Limit DNE")
            else:
                print(f"< {output}")
        elif userInput.strip() == '2':
            print(". Derivative")
            f = cleanInput(input(". Enter function of one variable: "))#obtain and clean necessary user input
            x = input(". Enter function variable (e.g. 'x', 't'): ")
            n = cleanInput(input(f". Enter value for {x}: "))
            output = derivative(x, n, f)
            if type(output) == str: #needed since derivative could output string, and isnan causes errors for strings. 
                print(f"< {output}")
            elif math.isnan(output):
                print("< Derivative DNE")
            else:
                print(f"< {output}")
        elif userInput.strip() == '3':
            print(". Definite Integral")
            f = cleanInput(input(". Enter function of one variable: "))#obtain and clean necessary user input
            x = input(". Enter function variable (e.g. 'x', 't'): ")
            a = cleanInput(input(". Enter lower bound of integration: "))
            b = cleanInput(input(". Enter upper bound of integration: "))
            output = defInt(a, b, x, f)
            if type(output) == str: #needed since derivative could output string, and isnan causes errors for strings. 
                print(f"< {output}")
            elif math.isnan(output):
                print("< Derivative DNE")
            else:
                print(f"< {output}")
        else:
            print(evaluateExpression(cleanInput(userInput.lower()))) #if not otherwise recognized as menu navigation, evaluates input
    
def linAlg(userInput):
    linAlgInstructions() #prints instructions
    while userInput.lower()!='exit':
        userInput = input("\n> ")
        if userInput.strip() == '0' or userInput.lower().strip() == 'help': #prints instructions
            linAlgInstructions()
        elif userInput.strip() == '1':
            print(". REF and RREF")
            m = cleanInput(input(". Enter the number of rows in the matrix: ")) #obtain and clean necessary user input
            n = cleanInput(input(". Enter the number of columns in the matrix: "))
            matrix = matrixInput(m, n)
            output1 = ref(matrix)
            print("< REF Matrix:") #prints REF and RREF matrices separately using printMatrix function
            printMatrix(output1)
            output2 = rref(output1)
            print("< RREF Matrix:")
            printMatrix(output2)
        elif userInput.strip() == '2':
            print(". Determinant")
            m = cleanInput(input(". Enter the number of rows in the matrix: ")) #obtain and clean necessary user input
            n = cleanInput(input(". Enter the number of columns in the matrix: "))
            if m!= n:
                print("< Error: Determinant requires square matrix")
                continue
            matrix = matrixInput(m, n)
            output = determinant(matrix)
            print(f"< {output}")
        elif userInput.strip() == '3':
            print(". Matrix Multiplication (AxB)")
            m = cleanInput(input(". Enter the number of rows in A: ")) #obtain and clean necessary user input
            n = cleanInput(input(". Enter the number of columns in A: "))
            m2 = cleanInput(input(". Enter the number of rows in B: "))
            n2 = cleanInput(input(". Enter the number of columns in B: "))
            if n != m2:
                print("< Error: Incorrect dimensions for matrix multiplication")
                continue
            print(". Matrix A")
            matrix = matrixInput(m, n)
            print(". Matrix B")
            matrix2 = matrixInput(m2, n2)
            output = matrixMult(matrix, matrix2)
            printMatrix(output)
        else:
            print(evaluateExpression(cleanInput(userInput.lower()))) #if not otherwise recognized as menu navigation, evaluates input
    
def complexAnalysis(userInput):
    complexInstructions() #prints instructions
    while userInput.lower()!='exit':
        userInput = input("\n> ")
        if userInput.strip() == '0' or userInput.lower().strip() == 'help': #prints instructions
            complexInstructions()
        elif userInput.strip() == '1':
            print('. Modulus')
            try:
                z = cleanComplexInput(input("Enter complex number: ")) #obtain and clean necessary user input
                output = abs(z)
                print(f'< {output}')
            except:
                print("< Error: Input not Recognized")
        elif userInput.strip() == '2':
            print('. Exponential Form')
            try:
                z = cleanComplexInput(input(". Enter complex number: ")) #obtain and clean necessary user input
                modul = abs(z)
                if z.real == 0: #separately considers when complex number is 0 or purely imaginary since atan will yield errors otherwise
                    if z.imag > 0:
                        arg = math.pi / 2
                    elif z.imag < 0:
                        arg = -math.pi / 2
                    else:
                        arg = "Undefined"
                else:
                    arg = math.atan(z.imag/z.real) #calclates arg or theta in exponential form
                if z.imag == 0 and z.real < 0:
                    arg = -math.pi
                print(f'< {modul} * exp({arg} * j)') #prints exponential form
            except:
                print("< Error: Input not Recognized")
        else:
            evaluateComplexExpression(userInput) #if not otherwise recognized as menu navigation, evaluates input
    
def lim(x, nString, f, threshold = 0.00000001): #threshold is the threhsold for function input similarity (delta)

    threshold2 = 0.001 #threshold for function output (epsilon)
    fAssigned = 0 #number of f_n variables initialized, used to figure out where error ocuurred if it did
    
    if x not in f:
        print("< Warning: variable not found in function") #warning, to be ignored if function is constant
    try:
        n = eval(nString) #separately evaluates the n string input for more specific error message
    except:
        print("< Problem with input for number approached")
        return math.nan
    
    try:
        f_n = eval(f.replace(x, '(' + str(n) + ')')) #evaluates the valueu at the function. In try statement since f(x) doesn't have to exist
        fAssigned += 1 #number of f_n variables initialized, used to figure out where error ocuurred if it did
        f_n2 = eval(f.replace(x, '(' + str(n + threshold) + ')')) #evaluates f(x+epsilon))
        fAssigned += 1 #number of f_n variables initialized, used to figure out where error ocuurred if it did
        f_n3 = eval(f.replace(x, '(' + str(n - threshold) + ')')) #evaluates f(x-epsilon))
        fAssigned += 1 #number of f_n variables initialized, used to figure out where error ocuurred if it did
        if abs(f_n - f_n2) < threshold2 and abs(f_n - f_n3 < threshold2): #if function is continuous at n / not an asymptote
            return f_n
        else: #f is discontinuous or asymptotic at n
            if f_n != 0: #the lines in this if statement check if the limit approaches positive or negative infinity
                leftRatio = f_n2 / f_n #considers the relative "slope" on either side of limit to separate diverging limits
                rightRatio = f_n3 / f_n
                if (leftRatio < threshold2) and (f_n3 > 0): #if elif else statements used to separate positive, negative, and cross-sign asymptotes
                    if (rightRatio < threshold2) and (f_n2 > 0):
                        return math.inf
                    else:
                        return math.nan
                elif (leftRatio < threshold2) and (f_n3 < 0):
                    if (rightRatio < threshold2) and (f_n2 < 0):
                        return -math.inf
                    else:
                        return math.nan
            if abs(f_n2 - f_n3) < threshold2 * 2: #if limit on left and right side is equal (similar based on delta), return average
                return (f_n2 + f_n3) / 2
            else:
                return math.nan #if limits on left and right sides are different, limit DNE
        
    except (ValueError, ZeroDivisionError): #only handles errors brought up by the functioin not existing at x
        if fAssigned == 2 or fAssigned == 1: #if either the assignment of f_n2 or f_n3 failed
            return math.nan
        elif fAssigned == 0: #if failure was in evaluating f(x)
            try:
                f_n2 = eval(f.replace(x, '(' + str(n + threshold) + ')')) #tries to consider nearby points without considering f(x))
                f_n3 = eval(f.replace(x, '(' + str(n - threshold) + ')'))
                
                #check for asymptotes
                f_n4 = eval(f.replace(x, '(' + str(n + threshold ** 2) + ')')) #threshold squared is much closer to n, gives threshold for divergence
                f_n5 = eval(f.replace(x, '(' + str(n - threshold ** 2) + ')'))
                
                if f_n4 != 0 and f_n5 != 0: #to eliminate risk of divide by zero error
                    leftRatio = f_n2 / f_n4 #the following checks asymptotes the same way as before, only without explicitly evaluatinig f(x)
                    rightRatio = f_n3 / f_n5
                    if (leftRatio < threshold2) and (f_n3 > 0):
                        if (rightRatio < threshold2) and (f_n2 > 0):
                            return math.inf
                        else:
                            return math.nan
                    elif (leftRatio < threshold2) and (f_n3 < 0):
                        if (rightRatio < threshold2) and (f_n2 < 0):
                            return -math.inf
                        else:
                            return math.nan
                
                if abs(f_n2 - f_n3) < threshold2 * 2: #if limit on left and right side is equal (similar), return average
                    return (f_n2 + f_n3) / 2
                else:
                    return math.nan #if limits on left and right sides are different, limit DNE
            except (ValueError, ZeroDivisionError):
                return math.nan
            except:
                return "Input Error"
    except: #all other errors are treated as input error
        return "Input Error"
    
def derivative(x, nString, f):
    try:
        n = eval(nString)
        f_n = eval(f.replace(x, '(' + str(n) + ')'))
        f_n2 = f.replace(x, '((' + str(n) + ')+' + x + ')') #sets up string to call to limit function to find derivative
        return lim(x, '0', '(' + f_n2 + '- (' + str(f_n) + ')) / ' + x) #calls limit definition of derivative
    except (ValueError, ZeroDivisionError): #implies derivative DNE
        return math.nan
    except:
        return "Input Error"
    
def rsum(a, b, f, x, w): #helper function for definite integral, done using riemann sum
    sum = 0
    i = eval(a)
    if w == 0: #w is rectangle width, 0 means the loop would go on forever
        return math.nan
    if w < 0: #make w positive so limit function considers limit from left equal to limit from right
        w = abs(w) 
    while i <= eval(b): #performs riemann suum, adding in each "box"
        sum += eval(f.replace(x, str(i))) * w
        i += w
    return sum
    
def defInt(aString, bString, x, f):
     try:
         
         a = eval(aString)
         b = eval(bString)
         if b < a: #if variables of integration are switched, negate function and switch a and b
             temp = a
             a = b
             b = temp
             f = '-1 * (' + f + ')' #have to negate function since a and b are switched
         riemannSum = "rsum('" + str(a) + "','" + str(b) + "','" + f.replace(x, "(" + x + ")") + "','" + x + "',i)"
         #the above line sets up another call to the lim function with separate threshold inputted for run time issues
         return lim('i', '0', riemannSum, 0.0001) #threshold is 0.0001 since otherwise loop takes a long time
     except (ValueError, ZeroDivisionError): #separately consider cases where int does not exist for whatever reason
         return math.nan
     except:
         if 'i' in f: #since i is the string used in the limit, it cannot appear in the function, so this is printed
             print("< Caution, function cannot contain the letter 'i'")
         return "Input Error"
     
def matrixInput(mStr, nStr): #helper function for linear algebra functions, gets input for matrix
    try:
        m = eval(mStr)
        n = eval(nStr)    
        matrix = [[0] * n for i in range(m)] #for i in range notation used since otherwise updating one element would update each in its column
        row = 0
        
        while row < m: #loops through each element in array
            col = 0
            while col < n:
                try:
                    matrix[row][col] = eval(cleanInput(input(f". Enter {row+1}x{col+1} element: "))) #gets user input
                    col += 1
                except:
                    print(". Error, please enter a valid number or expression") #if wrong syntax is enterred, it tries again
            row += 1
        return matrix
    except:
        pass

def printMatrix(matrix): #helper function for linear algebra functions, prints matrix
    try:
        for row in matrix:
            print('< ', end = " ") #starts each line
            for item in row:
                if item == 0: #this makes it not print -0 sometimes 
                    item = abs(item)
                if item >= 0: #this if statement aligns columns by shifting values without a '-' sign to the right. 
                    print(" ", end = "")
                print("%.5f" % (item), end = " ") #%f so item is always printed with decimal to 5 decimal places
            print() #new line
    except:
        pass

def transpose(matrix):
     m = len(matrix)
     n = len(matrix[0])
     newMatrix = [[0] * m for i in range(n)] #for i in range notation used since otherwise updating one element would update each in its column
     for row in range(m): #loops through each element in input, initializing corresponding value in output
         for col in range(n):
             newMatrix[col][row] = matrix[row][col]
     return newMatrix
 
def orderRows(matrix): #orders the rows of the matrix so pivots are staircasing (each row goes down), helper function for REF
    firstNonZeros = [] #list of positions of pivots in each row
    for row in matrix:
        nonZeroFound = False #false until nonzero value found
        for item in range(len(row)):
            if row[item] != 0 and not nonZeroFound: #initializes if first nonzero value in row
                nonZeroFound = True
                firstNonZeros.append(item)
                continue #it would be a waste of time to do the rest of the iteration of the loop
        if not nonZeroFound:
            firstNonZeros.append(len(matrix)+1) #all 0 rows should be the last row, guaranteed if len(matrix) + 1
            
    for a in range(len(firstNonZeros) - 1): #this loop sorts through firstNonZero list, makes it in asceding order, switching rows as it goes
        b = a + 1
        while b < len(firstNonZeros):
            if firstNonZeros[a] > firstNonZeros[b]: #if out of order, switch values in list as well as rows
                temp = firstNonZeros[a]
                firstNonZeros[a] = firstNonZeros[b]
                firstNonZeros[b] = temp
                
                temp = matrix[a] #performs row op, new temp variable
                matrix[a] = matrix[b]
                matrix[b] = temp
                
                print(f'. Row {a + 1} <-> Row {b + 1}') #print row op performed
            b += 1
            
    return matrix
                
        
def ref(matrix):
    try:
        tMatrix = transpose(matrix) #for easy access of individual columns
        thisPivot = 0 #location of current pivot 
        doneRows = [] #list of rows which are reduced 
        for col in range(len(tMatrix)-1):
            i = 0 #loop control variable
            nonZeroFound = False #used to locate pivot
            while i < len(tMatrix[col]):
                item = tMatrix[col][i]
                if item != 0 and not nonZeroFound and i not in doneRows: #if nonzero value is in a non reduced row it is a pivot
                    nonZeroFound = True
                    thisPivot = i
                    i = 0
                elif nonZeroFound and i != thisPivot and item != 0 and i not in doneRows: #if nonzero value is found after a pivot, replace row
                    rowReplaceCoeff = matrix[i][col] / matrix[thisPivot][col] #to multiply row by
                    
                    for subItem in range(len(matrix[i])): #replaces each value in row
                        matrix[i][subItem] -= rowReplaceCoeff * matrix[thisPivot][subItem]
                    
                    printChar = '-' #prints + or - for row replacement, in an easy to read format
                    if rowReplaceCoeff < 0:
                        printChar = '+'
                    print(f'. Row {i + 1} -> Row {i + 1} {printChar} %.5f * Row {thisPivot + 1}' % (abs(rowReplaceCoeff)))
                        
                    #for subItem in range(len(matrix[thisPivot])): #this code is optional and makes the pivots of each row 1
                        #matrix[thisPivot][subItem] /= thisPivotValue
                    
                    tMatrix = transpose(matrix) #updates tMatrix
                    doneRows.append(thisPivot) #adds current row to doneRows
                i += 1
        return orderRows(matrix) #orderRows ensures pivots are staircasing, necessary for REF form.
    except:
        return "Input Error"
        
def rref(matrix): #rref accepts a matrxi in ref form
    try:
        m = len(matrix)
        n = len(matrix[0])
        minDim = int(((m + n) / 2) - (abs(m - n) / 2)) #minimum matrix dimension, smallest out of m or n
        pivotLocList = [] #list of locations of each pivot col
       
        diagonal = 0 #diagonal along with pivot loop through the matrix, starting with (0, 0), then (1, 1), (2, 2), etc.
        adjust = 0 #adjust starts as 0, but if a zero value is found, it is incremented by 1 (e.g. if (1,1) is zero, the code loops to (1,2) to check if its a pivot)
        
        while diagonal < minDim and diagonal + adjust < n:
            thisPivot = matrix[diagonal][diagonal + adjust]
            if thisPivot == 0:
                adjust += 1
            else:
                pivotLocList.append([diagonal, diagonal + adjust]) #adds location of pivot withni matrix to list
                diagonal += 1
        
        for pivot in range(len(pivotLocList)):
            pivot += 1 #want to take last element of pivot list first, so add one and then access negative index
            pivotRow = pivotLocList[-pivot][0]
            pivotCol = pivotLocList[-pivot][1]
            
            currentRow = 0
            while currentRow < pivotRow: #loops through each row
                if matrix[currentRow][pivotCol] != 0: #same idea as the row replacement code in ref except working behind each pivot
                    rowReplaceCoeff = (matrix[currentRow][pivotCol] / matrix[pivotRow][pivotCol]) #find coeff to multiply row by
                    
                    for item in range(len(matrix[currentRow])): #replaces each element in row
                        matrix[currentRow][item] -= rowReplaceCoeff * matrix[pivotRow][item] 
                    
                    printChar = '-' #printChar priints row replacement in easy to read format
                    if rowReplaceCoeff < 0:
                        printChar = '+'
                    print(f'. Row {currentRow + 1} -> Row {currentRow + 1} {printChar} %.5f * Row {pivotRow + 1}' % (abs(rowReplaceCoeff)))
                currentRow += 1

        for pivot in pivotLocList: #scales rows so each pivot has a value of 1, one of the rref requirements
            rowScalingCoeff = matrix[pivot[0]][pivot[1]]
            if rowScalingCoeff == 1:
                continue
            for item in range(len(matrix[pivot[0]])):
                matrix[pivot[0]][item] /= rowScalingCoeff #divivde by pivot number at end to make leading number in each row = 1
            print(f'. Row {pivot[0] + 1} -> Row {pivot[0] + 1} / %.5f' % (rowScalingCoeff))
            
        return matrix
        
    except:
        return "Input Error"
    
def determinant(matrix): #finds determinant of square matrix recursively
    try:
        if len(matrix) == 2 and len(matrix[0]) == 2: #if matrix of length 2, simply finds determinant using definition
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        elif len(matrix) == 1 and len(matrix[0]) == 1: #if only 1 element, this is the determinant
            return matrix[0][0]
        else: #if more than two, return linear combo of minor matrices
            answer = 0
            for item in range(len(matrix[0])):
                coeff = (-1) ** item #coeff alternates positive and negative
                
                subMatrix = matrix[1:] #the following lines of code design subMatrix to be matrix without the first row or 'item' column
                subMatrix = transpose(subMatrix)
                tempMatrix = subMatrix[item+1: len(matrix)] 
                subMatrix = subMatrix[0:item]
                for item2 in tempMatrix:
                    subMatrix.append(item2)
                subMatrix = transpose(subMatrix)
                
                answer += coeff * determinant(subMatrix) * matrix[0][item] #adds this minor multiplied by removed element with proper sign
            return answer
    except:
        return "Input Error"

def matrixMult(matrix, matrix2):
    try:
        answer = [[0] * len(matrix2[0]) for i in range(len(matrix))] #for i in range notation used since otherwise updating one element would update each in its column
        matrix2 = transpose(matrix2) #transpose so its easier to reference the second matrice's values
        
        for row in range(len(matrix)): #loops through each element of answer list
            for col in range(len(matrix2)): #no [0] necessary since matrix2 was transposed
                linSum = 0
                for item in range(len(matrix[0])): #goes through the linear combo elements
                    linSum += matrix[row][item] * matrix2[col][item]
                answer[row][col] = linSum
        
        return answer
    except:
        return "Input Error" 
        
#makes a series of replacements to input strings to make code work with a wider array of input syntax
def cleanInput(messy):
    #functions
    clean = messy.replace('sin','math.sin') #handle inputs, replace specified values which require math. to include math.
    clean = clean.replace('cos','math.cos')
    clean = clean.replace('tan','math.tan')
    clean = clean.replace('asin','math.asin')
    clean = clean.replace('acos','math.acos')
    clean = clean.replace('atan','math.atan')
    clean = clean.replace('sinh','math.sinh')
    clean = clean.replace('cosh','math.cosh')
    clean = clean.replace('tanh','math.tanh')
    clean = clean.replace('asinh','math.asinh')
    clean = clean.replace('acosh','math.acosh')
    clean = clean.replace('atanh','math.atanh')
    clean = clean.replace('sqrt','math.sqrt')
    clean = clean.replace('cbrt','math.cbrt')
    clean = clean.replace('floor','math.floor')
    clean = clean.replace('ceil','math.ceil')
    clean = clean.replace('fabs','math.fabs')
    clean = clean.replace('exp','math.exp')
    clean = clean.replace('log','math.log')
    clean = clean.replace('log10','math.log10')
    clean = clean.replace('pow','math.pow')
    clean = clean.replace('degrees','math.degrees')
    clean = clean.replace('radians','math.radians')
    clean = clean.replace('factorial','math.factorial')
    
    #constants
    clean = clean.replace('pi','math.pi')
    clean = clean.replace('inf','math.inf')
    clean = clean.replace('tau','math.tau')
    try: #replacement of e constant needs to be in try so it doesn't replace the e's in 'ceil', 'degrees', etc.
        cleanTemp = clean.replace('e','math.e')
        eval(cleanTemp)
        clean = cleanTemp
    except:
        pass
    
    clean = clean.replace('math.math.','math.') #if user already put the math. in then this will handle the doubling up
    if clean != messy: #if changes were made, print the interpretted result
        print(f". {clean}")
    return clean.strip()

def cleanComplexInput(exp):
    try:
        return eval(cleanInput(exp).lower().replace('i','j')) #in addition to cleanInput, this replaces the normal imaginary var i with the one used in python 'j'
    except:
        return eval(cleanInput(exp)) #if this leads to an error, just use cleanInput
            
def evaluateComplexExpression(exp): #same as evaluateExpression except with special handling of complex expressions using python's complex class
    try:
        print(f"< {eval(cleanInput(exp.lower()))}")  #same try except structure as evaluateComplexExpression
    except ValueError:
        print("< Value Error: check domain")
    except:
        try:
            print(f"< {eval(cleanInput(exp.lower().replace('i','j')))}") #replaces i with j for eevaluuation
        except:
            pass
        if exp.lower() != 'exit':
            print("< Input not recognized. Enter 0 or 'help' to print instructions")
    

if __name__ == '__main__': #call main function
    main()


