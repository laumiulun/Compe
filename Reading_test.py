import csv

"""
with open("out.csv") as f:
        out=[]
        for line in f:
            line = line.split(',\n')
            if line:
                line=[str(i) for i in line]  # convert to str
                out.append(line)


print(out)



out=[]
with open('out.csv', newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=',', quotechar='|')
    out=[]
    for line in csvfile:
        line=line.split()
        if line:
            line=[str(i) for i in line]
            out.append(line)
print(out)
"""
with open('out.csv') as csvfile:
    out=[]
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row:
            row=[str(i) for i in row]
            out.append(row)

NumRows=(len(out))                      # Number of Rows
NumColumns=(len(out[0]))                # Number of Columns


print(NumRows,'\n')
print(NumColumns)
print(out[0])
del out[0]
    
