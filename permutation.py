from itertools import permutations
import csv


filename = "input.csv"
 
fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)    
    fields = csvreader.next() 
    for row in csvreader:
        rows.append(row)
filename="permu.csv"
with open(filename, 'w') as csvfile:
	csvwriter = csv.writer(csvfile)
	for row in rows:
		for col in row:
			p=col
			name, sep, domain = p.partition('.')
			xlist=[''.join(x)+sep+domain for x in permutations(name)]
		csvwriter.writerow(xlist)
			
	


