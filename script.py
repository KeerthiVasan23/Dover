# importing csv module
import csv
import whois
 
filename = "input.csv"
 
fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)    
    fields = csvreader.next() 
    for row in csvreader:
        rows.append(row)

filename = "output.csv"
fields = ['Domain name','Creation','ID','Location','IP','Expiration']
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    for row in rows:
   	for col in row:
		x=whois.whois(col)
		csvwriter.writerow([(x.domain_name[1]),
		(x.creation_date[0]),
		(x.registry_domain_id),
		(x.state),
		(x.registrar_url),
		(x.expiration_date[0])])
	print('\n')

