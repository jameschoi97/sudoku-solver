class square:

    def __init__(self, row, column, number):
        """
        attributes:
        state: "fixed" for squares that had a pre-assigned value and "blank" for an empty square that needs to be assigned a number
        position: a tuple that consists of the square's row, column, and block value
        number: number that is assigned to the square. (0 if no number is assigned)
        options: a list of numbers that can be assigned to the square if it is blank. The list starts with all 9 numbers in the start of the program
        tried: a list of numbers that has been tried on a square if it is blank. The list starts with no element in the start of the program
        """
        if number == 0:
            self.state = "blank"
            self.number = 0
            self.options = [1,2,3,4,5,6,7,8,9]
            self.tried = []
        else:
            self.state = "fixed"
            self.number = number

        block = (row//3)*3+(column//3)
        self.position = (row, column, block)
        

    #a function that adds a number to the square's tried list
    def add_tried(self, number):

        self.tried.append(number)


    #a function that resets the square's tried list
    def reset_tried(self):

        self.tried = []
        

        


