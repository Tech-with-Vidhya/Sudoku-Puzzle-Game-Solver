# Length of the Sudo Board is 9 rows and 9 columns....
sudo = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],        # Row 0
    [6, 0, 0, 0, 7, 5, 0, 0, 9],        # Row 1
    [0, 0, 0, 6, 0, 1, 0, 7, 8],        # Row 2
    [0, 0, 7, 0, 4, 0, 2, 6, 0],        # Row 3
    [0, 0, 1, 0, 5, 0, 9, 3, 0],        # Row 4
    [9, 0, 4, 0, 6, 0, 0, 0, 5],        # Row 5
    [0, 7, 0, 3, 0, 0, 0, 1, 2],        # Row 6
    [1, 2, 0, 0, 0, 7, 4, 0, 0],        # Row 7
    [0, 4, 9, 2, 0, 6, 0, 0, 7]         # Row 8
]


# To display the Sudo Board list as a 9x9 Matrix Board in order to have good visual representation...
def Display_Sudo_Board(sudo):

    for i in range (len(sudo)):

        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range (len(sudo)):

            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j != 8:
                print(str(sudo[i][j]) + " ", end="")
            else:
                print(str(sudo[i][j]))


# Function to check whether num is a duplicate in row or column or 3x3 matrix, or it is unique
def Sudo_Evaluator(sudo, i, j, num):
    for p in range (0, 9):
        if sudo[i][p] == num and p != j:
            return False                                    # Number already exists in a given row

    for p in range (0, 9):
        if sudo[p][j] == num and p != i:                    # Number already exists in a given column
            return False

    x = (i // 3) * 3
    y = (j // 3) * 3
    for a in range (x, x+3, 1):
        for b in range (y, y+3, 1):
            if sudo[a][b] == num and a != i and b != j:
                return False                                # Number already exists in a given 3x3 small matrix

    return True                                             # Number is validated and unique



def Sudo_Solver(sudo):
    for i in range (0, 9):
        for j in range (0, 9):
            if sudo[i][j] == 0:
                for num in range (1, 10, 1):
                    if Sudo_Evaluator(sudo, i, j, num):
                        sudo[i][j] = num

                        if Sudo_Solver(sudo):
                            return True

                    sudo[i][j] = 0

                return
    #print(Display_Sudo_Board(sudo))
    return True


Display_Sudo_Board(sudo)
Sudo_Solver(sudo)
print("..............................")
print("..............................")
print("..............................")
Display_Sudo_Board(sudo)