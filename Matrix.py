class Matrix:
    elements = []
    '''
        Constructor.
    '''
    def __init__(self, num_row, num_col):
        for i in range(num_row):
            columns = []
            for j in range(num_col):
                columns.append(float(input(f"Enter the value for element ({i}, {j}):")))
            self.elements.append(columns)


    def __str__(self):
        element_str_rep = ""
        for row in self.elements:
            element_str_rep += str(row) + "\n"
        return element_str_rep




'''
elements look like:

[[* * *],
 [* * *],
 [* * *],
 [* * *],]
'''



