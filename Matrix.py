class Matrix:
    elements = []

    def __init__(self, num_row, num_col):
        for i in range(num_row):
            columns = []
            for j in range(num_col):
                columns.append(float(input(f"Enter the value for element ({i}, {j}):")))
            self.elements.append(columns)
    #TODO: print() override
    #def __str__(self):
    #    for i in range(len(self.elements)):



'''
elements look like:

[[* * *],
 [* * *],
 [* * *],
 [* * *],]
'''



