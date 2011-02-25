# Filename: cwb1.py
# Author: Esther Hong
# Centre No/ Index No: 3024 /
# Description: Read data from RESOURCE.DAT, format and output to screen

# check encoding of RESOURCE.DAT to be ANSI to prevent weird characters

import time # for date formatting

def DISPLAYRESOURCE():

    try:
        # open file for reading
        resource_file = open("RESOURCE.DAT", "r")
        
        # read in first line (creation date and number of records)
        heading_line = resource_file.readline()
        heading_line = heading_line.rstrip("\n") # remove white spaces
        
        # store creation date and number of records
        creation_date = heading_line[0:10] # read first 10 characters of line
        num_records = heading_line[10:] # read from the 10th character, possible not to specify end
        
        # display heading lines with creation date and number of records
        print("Creation date: " + creation_date)
        print("#Records: " + num_records)
        
        # display subheadings
        print("{0:13s}{1:17s}{2:32s}{3}".format("Resource No", "Resource Type", "Title", "Date Acquired")) #{0:13s} Placeholder: Spaces: Type
        print("-" * 75)

        #read in all record detail lines
        detail_lines = resource_file.readlines()
    
        # loop through number of records
        for record_line in detail_lines:
            
            # read record detail line
            record_line = record_line.rstrip("\n")
            
            # store resource no, title, date acquired and resource type
            resource_no = record_line[0:5]
            title = record_line[5:35]
            date_acquired = record_line[35:41]
            resource_type = record_line[41:]

            # format date from DDMMYY to DDMMYYYY
            date_acquired = time.strptime(date_acquired, "%d%m%y") # small y - 2 digit year # strp: read numbers and convert to date, divide into D M Y
            date_acquired = time.strftime("%d-%m-%Y", date_acquired) # strf: specify format 
            
            
            # format and display record detail line
            print("{0:13s}{1:17s}{2:32s}{3}".format(resource_no, resource_type, title, date_acquired))
            
        # close file
        resource_file.close()

    except IOError:
        #display input file error
        print("Error! Input file does not exist or is corrupted.")

# main - file to contain main program
if __name__ == "__main__":
    DISPLAYRESOURCE()
