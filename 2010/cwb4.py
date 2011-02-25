# cwb4.py
# choose data structure (list

try:
    # open resource file for input
    resource_file = open("RESOURCE.DAT" , "r")

    # get resource number, title, resource type
    # get resource details
    detail_lines = resource_file.readlines()

    # initialize resource list
    resource_list = []

    # loop through each resource
    for record_line in detail_lines:
    
        # clean each record line
        record_line = record_line.rstrip("\n")

        # get and store record info
        resource_no = record_line[0:5]
        title = record_line[5:35]
        resource_type = record_line[41:]

    # resource list - ["00001", "The Planets Suite", "C"]
        resource_list.append([[resource_no, title, resource_type]])

    # open loan file for input
    loan_file = open("LOAN.DAT" , "r")

    # get date due back, student id, student name, evaluation
    # get resource details
    detail_lines = resource_file.readlines()

    # initialize resource list
    loan_list = []

    # loop through each resource
    for record_line in detail_lines:
    
        # clean each record line
        record_line = record_line.rstrip("\n")

        # get and store record info
        studentid = record_line[4:9]
        studentname = record_line[9:38]
        datedueback = record_line[38:43]
        evaluation = record_line[43:92]


#   loan_list = [["00001", "S0001", "J Cho", "150211", " " * 50]]
        loan_list.append([[studentid, studentname, datedueback, evaluation]])
        

    ddb_list = [] # take ealiest and latest ddb
    for loan in loan_list:
        if loan[3] not in ddb_list:
            ddb_list.append(loan[3])
    print(db_list)

    ddb_list = []


    print(min(ddb_list))
    print(max(ddb_list))

    # initialize dictionary of date due back
    ddb_dict = {}

    for date_due_back in ddb_list:
        ddb_dict[date_due_back] =
    final_rec = []

    # set up data structure to hold merged record
    # compare resource no. in loan_list with resource no. in resource_list
    for loan in loan_list: # looping - loan[0] directly reads first element
        for resource in resource_list:
            if(loan[0] == resource_list[0]):
                if resource[2] == "C":
                    resource_type = "CD"
                else:
                    resource_type = "DVD"
                if loan[4] == (" " * 50):
                    final_rec.append([resource[0], resource[1], resource_type, loan[1], loan[2]])
    print(final_rec)

    # process

    # order by date due back?

    # report list - ["01001", "Wuthering Heights", "DVD", "S0237", "J Cho"]

    # display report

    # close files


except IOError:
    # display file input/output errors
    print("Error! Cannot read from input file or write to output file.")

