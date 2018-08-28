# importing csv module
import csv
import whois
import os

os.system('python permutation.py')
filename = "permu.csv"
 
fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)    
    fields = csvreader.next() 
    for row in csvreader:
        rows.append(row)

filename = "output.csv"
fields = ['Domain name','Creation','Expiration','ID','Location','IP']
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)

    for row in rows:
   	for col in row:
		try:
			x=whois.whois(col)
			rowww=[]
			try:
				csvwriter.writerow([(x.domain_name[1]),(x.creation_date[0]),(x.expiration_date[0]),(x.registry_domain_id),
			(x.state),
			(x.registrar_url)])
			except TypeError:
				csvwriter.writerow([(x.domain_name),(x.creation_date),(x.expiration_date),(x.registry_domain_id),
			(x.state),
			(x.registrar_url)])
		except(whois.parser.PywhoisError):
			print('\n')
	print('\n')

