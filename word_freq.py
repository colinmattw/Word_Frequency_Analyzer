import csv
import sys

word_list = []
with open(sys.argv[1], 'r') as file:
    file_as_str = file.read().replace(',','').replace('.','').replace('\n','').replace('-','').replace('?','').replace('!','').replace(';','').replace(':','').lower()
    word_list = file_as_str.split(' ')

buckets = {}
for i in word_list:
    if(i in buckets):
        buckets[i] += 1
    else:
        buckets.update({i : 1})

pairs_list = []
for i in buckets:
    pairs_list.append([i, buckets[i]])

pairs_list.sort(key=lambda x : x[1], reverse=True)
with open(sys.argv[2], 'w', newline='') as export:
    writer = csv.writer(export)
    for i in range(int(sys.argv[3])):
        writer.writerow([pairs_list[i][0], pairs_list[i][1]])
