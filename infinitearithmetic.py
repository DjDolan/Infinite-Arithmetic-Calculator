import getopt, sys
from ReadFile import *

def main():
    #create containers for expressions
    #must be using lists
    expressions = []        #list for expressions

    read_file("pycode.txt", expressions)

    # for x in expressions:
    #     print(x)

#runs main program
if __name__ == "__main__":
    main();