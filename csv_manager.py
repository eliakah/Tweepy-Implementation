# * Created by Eliakah kakou
# csv manager.
# This class runs all of the modules in the right sequential
# order depending on the input

import csv

#def main():

class csv_manager:
    #constructor, r = read, w = write
    def __init__(self, path, flag, fieldnames):
        self.fieldnames = fieldnames
        if flag == 'r':
            with open('names.csv') as csvfile:
                self.reader = csv.DictReader(csvfile)
            for row in self.reader:
                for i in len(fieldnames):
                    print(row[fieldnames[i]] + " ,")

        if flag == 'w':
            self.path = path
            with open(path, 'w') as csvfile:
                #fieldnames = ['first_name', 'last_name']
                self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                self.writer.writeheader()
    #this adds
    def addRow(self, row, fieldvalues):

