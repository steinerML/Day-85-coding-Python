import csv

# We read the entire CSV, with special encoding and print it with a loop
filename = 'realestate.csv'
with open (filename, encoding = 'utf-8-sig') as f:
    reader = csv.reader(f) #Default delimiter is a comma, wrong delimiter returns IndexError.
    # next(reader)

    for col in reader:
        print(col[0],col[2])
        # print(row[1],row[5],row[9])


