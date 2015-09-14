import csv
with open('iowa-liquor-sample.csv','rb') as csvfile:
	liqreader = csv.reader(csvfile)
	count = 0
	for row in liqreader:
		if "single malt scotch" in ("".join(row)).lower():
			count += 1
	print count
 

