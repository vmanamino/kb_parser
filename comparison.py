from os import listdir
from os.path import isfile, join
import chardet
import codecs
import csv
import sys

# kb_holdings = sys.argv[1]
# subscription = sys.argv[2]
# kb_holdings = './comparison'+kb_holdings
# subscription = './comparison'+subscription

# path = './comparison'
kb = './comparison/kb'
subscription = './comparison/subscription'

kb_issns = []
kb_each_row = []
for f in listdir(kb):
    my_file = join(kb, f)
    with codecs.open(my_file, 'r', 'utf-16') as contents:
        kb_rows = csv.reader(contents, delimiter="\t", quotechar='"')
        for cnt, line in enumerate(kb_rows):
            if cnt == 0:
                kb_headers = line
            if cnt >= 1:
                kb_issns.append(line[9])
                kb_each_row.append(line)

sub_issns = []
sub_each_row = []
for f in listdir(subscription):
    my_file = join(subscription, f)
    with open(my_file, 'r') as contents:
        sub_rows = csv.reader(contents, delimiter="\t", quotechar='"')
        print(sub_rows)
        for cnt, line in enumerate(sub_rows):            
            if cnt == 0:
                sub_headers = line
            if cnt >= 1:
                sub_issns.append(line[2])
                sub_each_row.append(line)


# match

kb_not_sub = open('kb_not_sub.txt', 'w')
# matches.write('%s\t' % ("header"))
for cnt, header in enumerate(kb_headers):
    if (cnt + 1) < len(kb_headers):
        kb_not_sub.write('%s\t' % (header))
    else:
        kb_not_sub.write('%s\n' % (header))

sub_not_kb = open('sub_not_kb.txt', 'w')
for cnt, header in enumerate(sub_headers):
    if (cnt + 1) < len(sub_headers):
        sub_not_kb.write('%s\t' % (header))
    else:
        sub_not_kb.write('%s\n' % (header))

sub_in_kb = open('sub_in_kb.txt', 'w')
for cnt, header in enumerate(sub_headers):
    if (cnt + 1) < len(sub_headers):
        sub_in_kb.write('%s\t' % (header))
    else:
        sub_in_kb.write('%s\n' % (header))



for cnt, sub in enumerate(sub_issns):
    if sub not in kb_issns:
        sub_row = list(sub_each_row[cnt])
        for cnt, data in enumerate(sub_row):
            if (cnt + 1) < len(sub_row):
                sub_not_kb.write('%s\t' % (data))
            else:
                sub_not_kb.write('%s\n' % (data))

    if sub in kb_issns:
        sub_row = list(sub_each_row[cnt])
        for cnt, data in enumerate(sub_row):
            if (cnt + 1) < len(sub_row):
                sub_in_kb.write('%s\t' % (data))
            else:
                sub_in_kb.write('%s\n' % (data))

print(len(kb_issns))
for cnt, kb in enumerate(kb_issns):
    print(cnt)
    if kb not in sub_issns:
        kb_row = list(kb_each_row[cnt])
        for cnt, data in enumerate(kb_row):
            if (cnt + 1) < len(kb_row):
                kb_not_sub.write('%s\t' % (data.encode("utf8")))
            else:
                kb_not_sub.write('%s\n' % (data.encode("utf8")))


    
sub_not_kb.close()











            


    
