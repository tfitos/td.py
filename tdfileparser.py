import re, os, datetime
from tdmodel import *

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
            print "Skipped: " + line.strip()
    
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
    
    return tdlist
    
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
        return datetime.date(int(m.group(1)), MONTHS.index(m.group(2)) + 1, int(m.group(3)))
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
