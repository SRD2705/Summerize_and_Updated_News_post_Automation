import csv

def check(file,url):
    with open(file,'r+') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if url == row[0]:
                return True
        return False