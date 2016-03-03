import csv

# Open our input and output files with two arguments:
# (path where program is currently in, r for reading)
# Create outfile so that we don't override 
# the original file ('w' stands for writing)

csvfile = open('./data/sample.csv', 'r')
outfile = open('./data/sample-clean.csv', 'w')

#print csvfile.read()

# Now a DictReader and DictWriter
# DictReader and DictWriter are imported libraries
reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)
# DictWriter writes to outfile
#reader.fieldname refers to the headers

# Write headers
writer.writeheader()

# Clean and write the data to output
for row in reader:
    row['first_name'] = row['first_name'].upper()

    #we are overwriting something that already exists with the clean version
    print row
    writer.writerow(row)
