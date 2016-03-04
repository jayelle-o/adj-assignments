import csv

csvfile = open('./data/cleanme.csv', 'r')
outfile = open('./data/allclean.csv', 'w')

#print csvfile.read()

reader = csv.DictReader(csvfile)
writer = csv.DictWriter(outfile, reader.fieldnames)

writer.writeheader()

for row in reader:

    # uppercase all fields:
    # first_name,mid_init,last_name,addr,city,state,zip,check_no,check_date,amount
    row['first_name'] = row['first_name'].upper()
    row['mid_init'] = row['mid_init'].upper()
    row['last_name'] = row['last_name'].upper()
    row['addr'] = row['addr'].upper()
    row['city'] = row['city'].upper()
    row['state'] = row['state'].upper()

    row['zip'] = row['zip'].zfill(5)  # add zeroes to any ZIP codes
    row['city'] = row['city'].replace("&NBSP;", " ") # delete non-breaking spaces


    if int(row['amount']) >= 1000:

        print row
        writer.writerow(row)