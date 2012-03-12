
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

MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']



#### MODEL HELPER METHODS ####

def tdlist_date2string(d):
    return str(d.year) + "-" + MONTHS[d.month - 1] + "-" + str(d.day).zfill(2)

def td_todict(td):
    return {"status": td.status, "number": td.number, "text": td.text}

def tdlist_todict(tdlist):
    result =  {"date": tdlist_date2string(tdlist.date),
               "realdate": tdlist.date,
               "tds": []}
    for td in tdlist.tds:
        result["tds"].append(td_todict(td))
    return result

def show(tdlist):
    print "  ===== " + tdlist_date2string(tdlist.date) + " ====="
    for td in tdlist.tds:
        print "  " + td.status + " " + str(td.number) + ", " + repr(td.text)

def showdict(tdlist):
    print "  ===== " + tdlist["date"] + " ====="
    for td in tdlist["tds"]:
        print "  " + td["status"] + " " + str(td["number"]) + ", " + repr(td["text"])


#### EXCEPTIONS #####

class DuplicateNumberError(RuntimeError):
    pass

class MissingNumberError(RuntimeError):
    pass

class IncorrectFileName(RuntimeError):
    pass