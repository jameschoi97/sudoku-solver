class row:

    def __init__(self, row, string, row_list):
        """
        attributes:
        row: the row number of the row
        numbers: a list of numbers in the string which is inputted
        row_list: list of previously entered rows
        """
        self.row = row
        self.row_list = row_list
        self.numbers = []
        
        for i in range(9):
            self.numbers.append(int(string[i]))


    #a function that checks the row for a repeated number
    def row_check(self):
        for i in range(9):
            for j in range(9):
                if self.numbers[i] == self.numbers[j] and i != j and self.numbers[i] != 0:
                    print("Invalid input. There are duplicate numbers in the same row.")
                    return False
        return True

    #a function that accesses the previously inputted rows and checks each column for a repeated number
    def column_check(self):
        for i in range(9):
            for another_row in self.row_list:
                if self.numbers[i] == another_row.numbers[i] and self.numbers[i] != 0:
                    print("Invalid input. There are duplicate numbers in the same column.")
                    return False
        return True



    #a function that accesses the previously inptted rows and checks each block for a repeated number
    def block_check(self):
        if self.row < 3:
            return self.block_check1()
        elif self.row < 6:
            return self.block_check2()
        else:
            return self.block_check3()

    def block_check1(self):
        for i in range(3):
            for j in range(3):
                for another_row in self.row_list[:3]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        for i in range(3,6):
            for j in range(3,6):
                for another_row in self.row_list[:3]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        for i in range(6,9):
            for j in range(6,9):
                for another_row in self.row_list[:3]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        return True

    def block_check2(self):
        for i in range(3):
            for j in range (3):
                for another_row in self.row_list[3:6]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        for i in range(3,6):
            for j in range(3,6):
                for another_row in self.row_list[3:6]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        for i in range(6,9):
            for j in range(6,9):
                for another_row in self.row_list[3:6]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        return True

    def block_check3(self):
        for i in range(3):
            for j in range (3):
                for another_row in self.row_list[6:9]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        for i in range(3,6):
            for j in range(3,6):
                for another_row in self.row_list[6:9]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        for i in range(6,9):
            for j in range(6,9):
                for another_row in self.row_list[6:9]:
                    if self.numbers[i] == another_row.numbers[j] and self.numbers[i] != 0:
                        print("Invalid input. There are duplicate numbers in the same block")
                        return False
        return True


