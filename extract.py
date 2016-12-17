from textblob.classifiers import NaiveBayesClassifier

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


def extract(fileName):
    records = []
    file = open(fileName, 'r')
    lines = file.read().splitlines()
    start = False
    breachCategory = ''
    breachType = ''
    state = ''
    for line in lines:
        #line = line.decode('utf-8').strip()
        line = unicode(line, errors='ignore')
        if len(line) != 0:
            if checkStart(line):
                start = True
            if checkEnd(line):
                start = False
                breachCategory = ""
            #print(start)
            if start and 'ITRC' not in line:
                infoLine = False
                #if "Medical/Healthcare" in words:
                if checkCategory(line)[0]:
                    breachCategory = checkCategory(line)[1]
                    infoLine = True
                    if infoLine:
                        breachType = 'Paper Data' if 'Paper' and 'Data' in line else 'Electronic'
                        state = findState(line)
                        #print(breachType)
                line += breachType
                line += state
                lineCategory = (line, breachCategory)
                if (len(breachCategory) != 0 or breachCategory != None):
                    records.append((lineCategory))
    return records

def checkStart(line):
    return 'ITRC' and 'Breach' and 'ID' in line

def checkEnd(line):
    return 'Attribute' and '1' and 'Publication:' in line

def checkCategory(line):
    categories = ['Medical/Healthcare', 'Business', 'Educational', 'Government/Military', 'Banking/Credit/Financial']
    for category in categories:
        if category in line:
            return (True, category)
    return (False, '')

def findState(line):
    for state in states:
        if state in line:
            return state

if __name__ == '__main__':
    train = extract('test.txt')
    test = extract('train.txt')
    cl = NaiveBayesClassifier(train)
    print(cl.classify("Recently, we became aware of an unauthorized intrusion into a:database used "
                      "by the Wisconsin National Guard Association (WINGA) in connection with their "
                      "group life insurance program. New York Life Insurance Company is the insurer "
                      "for the program. The program is administered by WINGA. The breach occurred to "
                      "the system of a vendor retained by WINGA. "))
    print("Accuracy: {0}".format(cl.accuracy(test)))