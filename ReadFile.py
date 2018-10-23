#function to read lines from file and store
def read_file(input, exp):
    # open file
    file = open(input)

    # loop through file
    for line in file:
        # if line is blank then append 'blank'
        if line == '\n':
            exp.append("$")

        # clean up the line by removing delimeters
        else:
            clean_line = line.replace(' ', '').replace('\n', '')

            # append to the expressions list for parsing
            exp.append(clean_line)

    file.close()