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


#  matchpoint is title, since many titles do not have issn
kb_matchpoint = []
# kb_issns = [] access via element 9
kb_each_row = []
for f in listdir(kb):
    my_file = join(kb, f)
    with codecs.open(my_file, 'r', 'utf-16') as contents:
        kb_rows = csv.reader(contents, delimiter="\t", quotechar='"')
        for cnt, line in enumerate(kb_rows):
            if cnt == 0:
                kb_headers = line
            if cnt >= 1:
                print(line[0].upper())
                kb_matchpoint.append(line[0].upper())
                kb_each_row.append(line)


sub_matchpoint = [] 
# sub_issns = []
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
                sub_matchpoint.append(line[0].upper())
                sub_each_row.append(line)

print("kb matchpoints")
print(len(kb_matchpoint))
print("sub matchpoints")
print(len(sub_matchpoint))


# headers for files
kb_not_sub = open('./comparison/kb_not_sub.txt', 'w')
for cnt, header in enumerate(kb_headers):
    if (cnt + 1) < len(kb_headers):
        kb_not_sub.write('%s\t' % (header))
    else:
        kb_not_sub.write('%s\n' % (header))

kb_in_sub = open('./comparison/kb_in_sub.txt', 'w')
for cnt, header in enumerate(kb_headers):
    if (cnt + 1) < len(kb_headers):
        kb_in_sub.write('%s\t' % (header))
    else:
        kb_in_sub.write('%s\n' % (header))

sub_not_kb = open('./comparison/sub_not_kb.txt', 'w')
for cnt, header in enumerate(sub_headers):
    if (cnt + 1) < len(sub_headers):
        sub_not_kb.write('%s\t' % (header))
    else:
        sub_not_kb.write('%s\n' % (header))

sub_in_kb = open('./comparison/sub_in_kb.txt', 'w')
for cnt, header in enumerate(sub_headers):
    if (cnt + 1) < len(sub_headers):
        sub_in_kb.write('%s\t' % (header))
    else:
        sub_in_kb.write('%s\n' % (header))


# four sets we are interested in


for cnt, sub in enumerate(sub_matchpoint):
    if sub not in kb_matchpoint:
        sub_row = list(sub_each_row[cnt])
        for cnt, data in enumerate(sub_row):
            if (cnt + 1) < len(sub_row):
                sub_not_kb.write('%s\t' % (data))
            else:
                sub_not_kb.write('%s\n' % (data))

    if sub in kb_matchpoint:
        sub_row = list(sub_each_row[cnt])
        for cnt, data in enumerate(sub_row):
            if (cnt + 1) < len(sub_row):
                sub_in_kb.write('%s\t' % (data))
            else:
                sub_in_kb.write('%s\n' % (data))

count = 0
for cnt, kb in enumerate(kb_matchpoint):
    kb_row = list(kb_each_row[cnt])
    if kb not in sub_matchpoint:
        # count += 1        
        for cnt, data in enumerate(kb_row):
            if (cnt + 1) < len(kb_row):
                kb_not_sub.write('%s\t' % (data.encode('utf8')))
            else:
                kb_not_sub.write('%s\n' % (data.encode('utf8')))
    else:
        for cnt, data in enumerate(kb_row):
            if (cnt + 1) < len(kb_row):
                kb_in_sub.write('%s\t' % (data.encode('utf8')))
            else:
                kb_in_sub.write('%s\n' % (data.encode('utf8')))



    # if kb in sub_matchpoint:
    #     count += 1
    #     kb_row = list(kb_each_row[cnt])
    #     for cnt, data in enumerate(kb_row):
    #         if (cnt + 1) < len(kb_row):
    #             kb_in_sub.write('%s\t' % (data.encode('utf8')))
    #         else:
    #             kb_in_sub.write('%s\n' % (data.encode('utf8')))




# print(len(kb_issns))
# print(len(sub_issns))
# print(sub_issns)
# print(kb_issns)
# count = 0
# kb_set = set(kb_issns).difference(sub_issns)
# print(len(list(kb_set)))
# for cnt, kb in enumerate(kb_issns):
#     # print(cnt)
#     if kb not in sub_issns:
#         count += 1
#         # print(count)
#         kb_row = list(kb_each_row[cnt])
#         for cnt, data in enumerate(kb_row):
#             if (cnt + 1) < len(kb_row):
#                 kb_not_sub.write('%s\t' % (data.encode("utf8")))
#             else:
#                 kb_not_sub.write('%s\n' % (data.encode("utf8")))


    












            


    
