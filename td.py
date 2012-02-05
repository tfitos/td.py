import sys
import re

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

def parse(path):
    f = open(path, 'r+')
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
    for i in range(1,maxnum):
        try:
            tds[i]
        except KeyError as ke:
            raise MissingNumberError(ke.message)
        


def process(line):
    p = re.compile('^\s*(PIPA|DONE|SKIP)?\s*(\d+),\s+([a-zA-Z0-9_ ]+)$')
    m = p.match(line)
    if m:
        # print m.group(1)
        # print m.group(2)
        # print m.group(3)
        td = TD(m.group(1), int(m.group(2)), m.group(3))
        return td


class TD:
    def __init__(self, status, number, text):
        self.status = status
        self.number = number
        self.text = text
    def __str__(self):
        return "TD[" + (self.status if self.status else "----" )+ ";" + str(self.number)  +";" + self.text[:20]+"]" 

class DuplicateNumberError(RuntimeError):
    pass

class MissingNumberError(RuntimeError):
    pass

if __name__ == "__main__":
    main()