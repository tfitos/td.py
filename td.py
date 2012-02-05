import sys, re, os, datetime


def main():
    """" 
    Process todo files
    """
    if(len(sys.argv) < 2):
        print "Missing argument"
        sys.exit(1)
    try:
        parse(sys.argv[1])
    except DuplicateNumberError as dne:
        print "The TODO number already exists: " + str(dne.message)
    except MissingNumberError as mne:
        print "The TODO number missed: " + str(mne.message)
    except IncorrectFileName as ifn:
        print "Incorrect file name: " + str(ifn.message)
    except IOError as ioe:
        print ioe.strerror + ": " + ioe.filename

def parse(path):
    """
    opens the file and parses it to TDList
    can raise DuplicateNumberError, MissingNumberError, IncorrectFileName, IOError
    """
    f = open(path, 'r+')
    date = parsefilename(path)
    tdlist = TDList(date)
    lines = f.readlines()
    tds = {}
    maxnum = 0
    for line in lines:
        td = process(line.strip())
        if td is not None:
            try:
                tds[td.number]
                # tds dictionary already contains this number
                raise DuplicateNumberError(td.number)
            except KeyError:
                tds[td.number] = td
                if td.number > maxnum:
                    maxnum = td.number
        else:
            print "Line skipped: " + line.strip()
    
    # validate if there is a missing number in the todolist
    for i in range(1,maxnum+1):
        try:
            tds[i]
        except KeyError as ke:
            raise MissingNumberError(ke.message)
    try:
        tdlist.tds.append(tds[0])
    except KeyError:
        # there was no elem with number 0
        pass
    for i in range(1, maxnum+1):
        tdlist.tds.append(tds[i])
    
    show(tdlist)
    
def parsefilename(path):
    """
    parses filename to date; path is e.g. 'c:/todos/2012-FEB-05.txt'
    can raise IncorrectFileName
    """
    basename = os.path.basename(path)
    base = os.path.splitext(basename)[0]
    p = re.compile('^(\d\d\d\d)-(\w\w\w)-(\d\d)$')
    m = p.match(base)
    if m:
        # datetime.date(m.group(1), months.index(m.group(2)), m.group(3))
        return datetime.date(int(m.group(1)), months.index(m.group(2)) + 1, int(m.group(3)))
    else:
        raise IncorrectFileName(basename)


def process(line):
    """
    processes one td line and makes TD object; example: 'DONE 2, finish the first version of todo app'
    """
    p = re.compile('^\s*(PIPA|DONE|SKIP|TODO)?\s*(\d+),\s+([a-zA-Z0-9_ ]+)$')
    m = p.match(line)
    if m:
        td = TD(m.group(1), int(m.group(2)), m.group(3))
        return td

def show(tdlist):
    print "==== " + str(tdlist.date) + " ===="
    for td in tdlist.tds:
        print td.status + " " + str(td.number) + ", " + td.text


#### MODEL #####

class TD:
    def __init__(self, status, number, text):
        st = status if status else "TODO"
        st = "DONE" if st == "PIPA" else st
        self.status = st
        self.number = number
        self.text = text
    def __str__(self):
        return "TD[" + (self.status if self.status else "----" )+ ";" + str(self.number)  +";" + self.text[:20]+"]"
    
class TDList:
    def __init__(self, date):
        self.date = date
        self.tds = []
    def __str__(self):
        return "TDList[" + self.date +"]"

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAJ', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

#### EXCEPTIONS #####

class DuplicateNumberError(RuntimeError):
    pass

class MissingNumberError(RuntimeError):
    pass

class IncorrectFileName(RuntimeError):
    pass

if __name__ == "__main__":
    main()