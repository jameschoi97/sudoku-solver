from copy import deepcopy
import rows
import squares
            
def main():
    global rows #a list of rows that are inputted
    rows = gather_data()
    global squares #a list of square objects that are made with make_squares function
    squares = make_squares()
    global blanks #a list of indexes of blank squares in the squares list
    blanks = []
    for square in squares:
        if square.state == "blank":
            blanks.append(squares.index(square))
    solve()
    print_solution()


#a function that receives input from the user and makes sure that the inputs are valid                
def gather_data():
    row_list = []
    for i in range(9):
        while True:
            row_string = input("Type in the numbers for the row number " + str(i+1) +" (0 for blank squares): ")
            if input_check(row_string) == True:
                new_row = rows.row(i, row_string, row_list)
                if new_row.row_check() == True and new_row.column_check() == True and new_row.block_check() == True:
                    row_list.append(new_row)
                    break
    return row_list


#a function that checks that the string inputted consists of 9 numbers    
def input_check(string):
    if not string.isdigit():
        print("Invalid input. Please only type in numbers.")
        return False
    elif len(string) != 9:
        print("Invalid input. Please type in 9 numbers.")
        return False
    else:
        return True


#a function that makes 81 square objects from the rows inputted
def make_squares():
    square_list = []
    for row in rows:
        for column in range(9):
            square = squares.square(row.row, column, row.numbers[column])
            square_list.append(square)
    return square_list
            

#a function that solves the sudoku puzzle
def solve():
    set_options()
    complete = False #complete value is set to True in the beginning of each iteration and is changed to False if the program gets stuck at a square and needs to call start_over function
    #the loop only ends if it goes through all the blank squares successfully without changing the complete value to False
    while complete == False:
        complete = True
        for i in blanks:
            if squares[i].number == 0:
                assign_number(squares[i])
                if squares[i].number == 0:
                    start_over(i)
                    complete = False
                    break
            

#a function that goes through each square and eliminates some options for each square's options list
def set_options():
    change = True #change value is set to False in each iteration and is changed to True if one of the squares change its state from blank to fixed
    #this is because with more fixed squares the program may be able to eliminate more options 
    while change == True:
        remove_list = [] #a list of indexes of squares which will change its state to fixed
        change = False
        for i in blanks:
            new_square = option_check(squares[i])
            if squares[i].options != new_square.options:
                squares[i] = new_square
                if len(squares[i].options) == 1:
                    squares[i].number = squares[i].options[0]
                    remove_list.append(i)
                    change = True
        for i in remove_list:
            set_fixed(squares[i])



#a function that goes through the options of a square and eliminate some of them based on other fixed squares that shares row, column, or block with the square
def option_check(square):
    new_square = deepcopy(square)
    remove_list = []
    for number in new_square.options:
        for another_square in squares:
            if new_square.position[0] == another_square.position[0] or new_square.position[1] == another_square.position[1] or new_square.position[2] == another_square.position[2]:
                if number == another_square.number and another_square.state == "fixed":
                    remove_list.append(number)
                    break
    for number in remove_list:
        new_square.options.remove(number)
    return new_square


#a function that changes a square's state to fixed and remove its index from the blanks list
def set_fixed(square):
    index = squares.index(square)
    squares[index].state = "fixed"
    blanks.remove(index)


#a function that assigns a viable number to a square; 0 will be assigned if no number can be assigned                    
def assign_number(square):
    num = 0
    for number in square.options:
        if number not in square.tried and check(square, number) == True:
            num = number
            break
    square.number = num


#a function that checks if a number is viable for a square based on other squares in the same row, column, or block
def check(square, number):
    for another_square in squares:
        if square.position[0] == another_square.position[0] or square.position[1] == another_square.position[1] or square.position[2] == another_square.position[2]:
            if number == another_square.number:
                return False
    return True


#this function is called when no number can be assigned to the ith square
#the function will go to the preceding blank square and add its current number to the tried list and then change its number to 0
#then it will reset the tried list of the ith square
def start_over(i):
    change = blanks[blanks.index(i)-1]
    squares[change].add_tried(squares[change].number)
    squares[change].number = 0
    squares[i].reset_tried()


#function that prints out the solution once the puzzle is solved    
def print_solution():
    for i in range(9):
        for j in range(9):
            print(squares[i*9+j].number, end="")
        print()    

main()
