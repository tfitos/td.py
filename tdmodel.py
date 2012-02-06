
#### MODEL #####

class TD:
    def __init__(self, status, number, text):
        st = status if status else "TODO"
        st = "DONE" if st == "PIPA" else st
        self.status = st
        self.number = number
        self.text = text
    def __str__(self):
        return "TD[" + self.status + ";" + str(self.number)  +";" + self.text[:20]+"]"
    
class TDList:
    def __init__(self, date):
        self.date = date
        self.tds = []
    def __str__(self):
        return "TDList[" + self.date +"]"

MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAJ', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']



#### MODEL HELPER METHODS ####

def show(tdlist):
    print "==== " + str(tdlist.date) + " ===="
    for td in tdlist.tds:
        print td.status + " " + str(td.number) + ", " + td.text


#### EXCEPTIONS #####

class DuplicateNumberError(RuntimeError):
    pass

class MissingNumberError(RuntimeError):
    pass

class IncorrectFileName(RuntimeError):
    pass