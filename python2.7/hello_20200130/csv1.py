import csv

reader = csv.reader(file, delimeter=",")
for row in reader:
    print(row)

writer = csv.writer(file, delimeter=",")
writer.writerow(['aaa', 'bbb'])