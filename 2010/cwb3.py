# Filename: cwb3.py
# Author: Name
# Center Number/Index Number: 3024/
# Description: Append validated loan record to loan file

import datetime
from datetime import timedelta

def LOANRESOURCE():
    
    try:
        # open loan file to append
        loan_file = open("LOAN.DAT", "a")
        
        # open uresource.dat to read
        uresource_file = open("URESOURCE.DAT", "r")
        
        # skip heading line
        heading_line = uresource_file.readline()
        heading_line = heading_line.rstrip("\n")

        # initialise ResourceNo list
        resourceno_list = []
        
        # read record details
        detail_lines = uresource_file.readlines()

        # loop through all records
        for resource_line in detail_lines:
            
            # get ResourceNo
            resourceno = resource_line[0:5]
            
            # append ResourceNo to list
            resourceno_list.append(resourceno)
            
        # get and validate NoOfResource
        valid_NoOfResource = False
        while not valid_NoOfResource:
            NoOfResource = input("Enter number of resources: ")
            if len(NoOfResource) == 0:
                print("Error, number of resources cannot be empty.")
            elif not NoOfResource.isdigit():
                print("Error, number of resources must be in digits.")
            elif not 0 < int(NoOfResource) < 4:
                print("Error, a maximum of only 3 resources can be taken out at one time.")
            else:
                valid_NoOfResource = True

        for record in range(int(NoOfResource)):
                
            # get and validate ResourceNo
            valid_resourceno = False
            while not valid_resourceno:
                resourceno = input("Enter resource number: ")
                if len(resourceno) == 0: # presence check
                    print("Error, resource number cannot be empty.")
                elif len(resourceno) != 5: # length check
                    print("Error, resource number must be 5 digits.")
                elif not resourceno.isdigit(): # data type check
                    print("Error, resource number must be in digits.")
                elif resourceno not in resourceno_list:
                    print("Error, resource number does not exist.")
                else:
                    valid_resourceno = True
                # assume resource is not loaned
                    

            # get and validate StudentID
            valid_studentid = False
            while not valid_studentid:
                studentid = input("Enter student ID: ")
                if len(studentid) == 0: # presence check
                    print("Error, student ID cannot be empty.")
                elif len(studentid) != 5: # length check
                    print("Error, student ID must be 5 digits.")
                elif not studentid[0:1].upper() == 'S': # data type (first character) check
                    print("Error, first character must be S.")
                elif not studentid[1:5].isdigit(): # data type (last 4 characters) check
                    print("Error, last 4 characters must be digits.")
                elif not 0 < int(studentid[1:5]) < 10000: # range check
                    print("Error, student ID must be from S0001 to S9999.")
                else:
                    valid_studentid = True
                

            # get and validate StudentName
            valid_studentname = False
            while not valid_studentname:
                studentname = input("Enter student name: ")
                if len(studentname) == 0: # presence check
                    print("Error, student name cannot be empty.")
                elif len(studentname) > 30: # length check
                    print("Error, student name must be less than 30 characters.")
                else:
                    valid_studentname = True


            # compute DateDueBack
            # get system current date
            DateLoaned = datetime.date.today()
            # add 7 days to get date due back
            DateDueBack = DateLoaned + datetime.timedelta(days=7)
            DateDueBack = DateDueBack.strftime("%d%m%y")

            # validate evaluation
            evaluation = " " * 50


            # write validated record to loan file
            loan = ((resourceno + studentid + studentname + (" " * (30 - len(studentname))) + DateDueBack + evaluation + (" " * (50 - len(evaluation))) + "\n"))
            loan_file.write(loan)


        # close files
        loan_file.close()
        uresource_file.close()

    except IOError: # I/O error message
        print("Error, cannot read from input or appen to output file.")
        

# main
if __name__ == "__main__":
    LOANRESOURCE()
