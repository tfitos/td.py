import sys
from tdmodel import *
from tdfileparser import parse
from tdpersistence import MongoPersistence


def main():
    """" 
    Processes todo files and persists them.
    """
    if(len(sys.argv) < 2):
        print "Missing argument"
        sys.exit(1)
    try:
        tdlist = parse(sys.argv[1])
        print 'Parsed TD list:'
        show(tdlist)
        print ''
        persistence = MongoPersistence()
        persistence.setup()
        resultdict = persistence.search(tdlist_date2string(tdlist.date))
        if resultdict:
            print 'There is an existing TD list to this date:'
            showdict(resultdict)
            print ''
            answer = raw_input ("Do you want to store this TD list even if there is an existing TD list (y/n)?")
            if answer == "y":
                persistence.remove(tdlist_date2string(tdlist.date))
                print 'Old TD list removed.'
        else:
            answer = raw_input ("Do you want to store this TD list (y/n)?")
        if answer == "y":
            persistence.persist(tdlist)
            print "New TD list stored (" + tdlist_date2string(tdlist.date) + ")"
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