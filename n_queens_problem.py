"""
Problem Definition:
    Place 8 queens on an 8*8 board so that the two queens do not attack each other. As an additional
    constraint, each spaces is either empty or reserved. Reserved space does not prevent queens from
    attacking each other And only empty spaces can be placed on queens. How many possible ways to place
    a queens?
    implementation using deep search algorythm

Input: 
    8 lines, each line containing 8 characters. each space is reserved(*) or empty(.)
Output:
    Print only one integer : the number of ways to place a queens.
"""


countSol = 0            # counts the number of possible solutions
solutionStack = []      # stack to keep the trace of the state tree
 
def isSafe(chessTable, row, col):
    """
    This function checks the left and right upper diagonals,
    the upper part of the column and left side of the row 
    - if we encounter 1 somewhere, the functions returns False - the Queen cannot be placed at that (row, column)
    - if we don't encounter 1 anywhere, the function returns True.4
    """
    
    global solutionStack
    
    # checks the upper part of the column     
    for i in range(0, row):
        if chessTable[i][col] == 1:
            return False
    
    # checks the left upper diagonal    
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if chessTable[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    
    # checks the right upper diagonal  
    i = row - 1
    j = col + 1
    while i >= 0 and j <= 7:
        if chessTable[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
        
    # check the left side of the row
    for i in range(0, col):
        if chessTable[row][i] == 1:
            return False
              
    
    pair = (row, col)
    solutionStack.append(pair) # pair is a feasible solution, therefore we add it to the stack 

    return True
        

def SolveNQueen(chessTable, testData, row, col):
    """
    This function finds one feasible solution using depth first search algorithm.

    Input:
        chessTable ( 2D list array) : 
        testData () : 
        row:
        col:
    Returns: "True" if solution is found and "False" otherwise 
        
    """
    global countSol, solutionStack
        
    if(row > 7):
        solutionStack.pop()     # we reached the bootom of the state tree,
                                # a possible solution was found
                                # the last element is poped from the stack
        # countSol = countSol + 1
        return True
    
    for i in range(col, 8):
        if testData[row][i] == "*":     # * is for a reserved place, therefore if we encounter *, we skip this position
            continue
        else:   
            if isSafe(chessTable, row, i) == True:
                chessTable[row][i] = 1
                                
                if(SolveNQueen(chessTable, testData, row + 1, 0)):
                    return True
                                        
                chessTable[row][i] = 0      # chessTable[row][i] is not possible solution, 
                solutionStack.pop()         # so we remove it from the stack
                               
    return False    
            
def NQueenAllSolutions(chessTable, testData):
    """
    This function finds and counts all possible solutions
    Input:
        chessTable: 2D list array, initially initialized only with 0s
        testData: 2D list array, containing the inputed chess table
    """  
    global countSol, solutionStack
    
    if SolveNQueen(chessTable, testData, 0, 0) == True:
        countSol += 1
    
    while(len(solutionStack) > 0):
        pair = solutionStack.pop()      # pair[0] = row, pair[1] = column
        startRow = pair[0]              # back track to the last possible pair on the state tree
        startCol = pair[1]              # and continue to explore the tree
        
        for i in range(startRow, 8):
            for j in range(8):
                chessTable[i][j] = 0                  
        if SolveNQueen(chessTable, testData, startRow, startCol + 1) == True:
            countSol += 1

    
def main():

    f = open("3-1_ex1.txt",'r')
    testData = []
    lines = f.read().splitlines()
    # print(list(lines))
    for line in lines:
        line = list(line)
        array = [i for i in line]
        testData.append(array)
    
    # testData = []
    # for i in range(8):
    #     data = input()
    #     data = list(data)
    #     array = [i for i in data]
    #     testData.append(array)
    
    chessTable = [[0 for i in range(8)] for j in range(8)]      # initialize the 2D array with 0s,
                                                                # later if we find a possible position,
                                                                # it will be changed to 1

    NQueenAllSolutions(chessTable, testData)
    print(countSol)    
    
if __name__ == "__main__":
    main()

