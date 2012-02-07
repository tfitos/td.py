import sys
from tdmodel import *
from tdfileparser import parse
from tdpersistence import persist


def main():
    """" 
    Processes todo files and persists them.
    """
    if(len(sys.argv) < 2):
        print "Missing argument"
        sys.exit(1)
    try:
        tdlist = parse(sys.argv[1])
        show(tdlist)
        # print tdlist_todict(tdlist)
        answer = raw_input ("Do you want to store this TD list (yes/no)? ")
        if answer == "yes":
            persist(tdlist)
            print "TD list stored."
        else:
            print "td.py exits"
            sys.exit(0)
        
        
    except DuplicateNumberError as dne:
        print "The TODO number already exists: " + str(dne.message)
    except MissingNumberError as mne:
        print "The TODO number missed: " + str(mne.message)
    except IncorrectFileName as ifn:
        print "Incorrect file name: " + str(ifn.message)
    except IOError as ioe:
        print ioe.strerror + ": " + ioe.filename
        
    


if __name__ == "__main__":
    main()